import unittest

from edg import *
from .test_robotdriver import LipoConnector, MotorConnector, PwmConnector


class LedConnector(Block):
  def __init__(self):
    super().__init__()
    self.conn = self.Block(PassiveConnector())
    led_current = 36.6
    num_leds = 0

    self.vdd = self.Export(self.conn.pins.allocate('1').adapt_to(VoltageSink(
      current_draw=(-led_current*num_leds, led_current*num_leds)*mAmp)),
      [Power])
    self.din = self.Export(self.conn.pins.allocate('2').adapt_to(DigitalSink(
      current_draw=(-led_current*num_leds, led_current*num_leds)*mAmp
    )))
    self.gnd = self.Export(self.conn.pins.allocate('3').adapt_to(Ground()), [Common])


class RobotDriver2(JlcBoardTop):
  """Variant of robot driver that uses a ESP32 (non-C) chip and includes a few more blocks
  to use the extra available IOs
  """
  def contents(self) -> None:
    super().contents()

    self.batt = self.Block(LipoConnector(actual_voltage=(3.7, 4.2)*Volt))

    # actually on the 3V3 domain but need the battery output here
    self.isense = self.Block(OpampCurrentSensor(
      resistance=0.05*Ohm(tol=0.01),
      ratio=Range.from_tolerance(20, 0.05), input_impedance=10*kOhm(tol=0.05)
    ))
    self.connect(self.isense.pwr_in, self.batt.pwr)
    self.vbatt = self.connect(self.isense.pwr_out)

    self.gnd = self.connect(self.batt.gnd)

    self.tp_vbatt = self.Block(VoltageTestPoint()).connected(self.batt.pwr)
    self.tp_gnd = self.Block(VoltageTestPoint()).connected(self.batt.gnd)

    # POWER
    with self.implicit_connect(
        ImplicitConnect(self.gnd, [Common]),
    ) as imp:
      (self.reg_3v3, self.tp_3v3, self.prot_3v3), _ = self.chain(
        self.vbatt,
        imp.Block(BuckConverter(output_voltage=3.3*Volt(tol=0.05))),
        self.Block(VoltageTestPoint()),
        imp.Block(ProtectionZenerDiode(voltage=(3.45, 3.9)*Volt))
      )
      self.v3v3 = self.connect(self.reg_3v3.pwr_out)

    # 3V3 DOMAIN
    with self.implicit_connect(
        ImplicitConnect(self.v3v3, [Power]),
        ImplicitConnect(self.gnd, [Common]),
    ) as imp:
      self.mcu = imp.Block(IoController())
      self.i2c = self.mcu.i2c.allocate('i2c')

      self.tof = imp.Block(Vl53l0xArray(3))
      (self.i2c_pull, self.i2c_tp), self.i2c_chain = self.chain(
        self.i2c,
        imp.Block(I2cPullup()), imp.Block(I2cTestPoint()),
        self.tof.i2c)

      self.lcd = imp.Block(Er_Oled_091_3())
      self.connect(self.mcu.spi.allocate('spi'), self.lcd.spi)
      self.connect(self.lcd.cs, self.mcu.gpio.allocate('lcd_cs'))
      self.connect(self.lcd.reset, self.mcu.gpio.allocate('lcd_reset'))
      self.connect(self.lcd.dc, self.mcu.gpio.allocate('lcd_dc'))

      # IMU
      self.imu = imp.Block(Imu_Lsm6ds3trc())
      self.connect(self.i2c, self.imu.i2c)

      # Current sensor
      self.connect(self.isense.pwr, self.v3v3)
      self.connect(self.isense.gnd, self.gnd)
      self.connect(self.isense.ref, self.batt.gnd.as_analog_source())
      self.connect(self.isense.out, self.mcu.adc.allocate('isense'))

      self.expander = imp.Block(Pcf8574(0))
      self.connect(self.i2c, self.expander.i2c)
      # # TODO use pin assign util for IO expanders
      self.connect(self.expander.io.allocate_vector('tof_xshut'), self.tof.xshut)

      self.led = ElementDict[IndicatorLed]()
      for i in range(4):
        (self.led[i], ), _ = self.chain(self.expander.io.allocate('led'+str(i)), imp.Block(IndicatorLed()))

    # SPEAKER AND LOW POWER VBATT DOMAIN
    with self.implicit_connect(
            ImplicitConnect(self.vbatt, [Power]),
            ImplicitConnect(self.gnd, [Common]),
    ) as imp:
      (self.spk_tp, self.spk_drv, self.spk), self.spk_chain = self.chain(
        self.mcu.dac.allocate('spk'),
        self.Block(AnalogTestPoint()),
        imp.Block(Tpa2005d1(gain=Range.from_tolerance(10, 0.2))),
        self.Block(Speaker()))

      self.ws2812bArray = imp.Block(Ws2812bArray(5))
      self.connect(self.mcu.gpio.allocate('ledArray'), self.ws2812bArray.din)

      self.led_pixel = imp.Block(LedConnector())
      self.connect(self.ws2812bArray.dout, self.led_pixel.din)

    # MOTORS AND SERVOS
    with self.implicit_connect(
            ImplicitConnect(self.gnd, [Common]),
    ) as imp:
      self.motor_driver1 = imp.Block(Drv8833())
      self.connect(self.vbatt, self.motor_driver1.pwr)
      self.connect(self.mcu.gpio.allocate('motor_1a1'), self.motor_driver1.ain1)
      self.connect(self.mcu.gpio.allocate('motor_1a2'), self.motor_driver1.ain2)
      self.connect(self.mcu.gpio.allocate('motor_1b1'), self.motor_driver1.bin1)
      self.connect(self.mcu.gpio.allocate('motor_1b2'), self.motor_driver1.bin2)

      self.m1_a = self.Block(MotorConnector())
      self.connect(self.m1_a.a, self.motor_driver1.aout1)
      self.connect(self.m1_a.b, self.motor_driver1.aout2)
      self.m1_b = self.Block(MotorConnector())
      self.connect(self.m1_b.a, self.motor_driver1.bout1)
      self.connect(self.m1_b.b, self.motor_driver1.bout2)

      self.motor_driver2 = imp.Block(Drv8833())
      self.connect(self.vbatt, self.motor_driver2.pwr)
      self.connect(self.mcu.gpio.allocate('motor_2a1'), self.motor_driver2.ain1)
      self.connect(self.mcu.gpio.allocate('motor_2a2'), self.motor_driver2.ain2)
      self.connect(self.mcu.gpio.allocate('motor_2b1'), self.motor_driver2.bin1)
      self.connect(self.mcu.gpio.allocate('motor_2b2'), self.motor_driver2.bin2)
      self.connect(self.motor_driver1.sleep, self.motor_driver2.sleep, self.isense.pwr_out.as_digital_source())

      self.m2_a = self.Block(MotorConnector())
      self.connect(self.m2_a.a, self.motor_driver2.aout1)
      self.connect(self.m2_a.b, self.motor_driver2.aout2)
      self.m2_b = self.Block(MotorConnector())
      self.connect(self.m2_b.a, self.motor_driver2.bout1)
      self.connect(self.m2_b.b, self.motor_driver2.bout2)

    self.servo = self.Block(PwmConnector())
    self.connect(self.vbatt, self.servo.pwr)
    self.connect(self.gnd, self.servo.gnd)
    self.connect(self.mcu.gpio.allocate('pwm'), self.servo.pwm)

    # Misc board
    self.lemur = self.Block(LemurLogo())
    self.duck = self.Block(DuckLogo())
    self.leadfree = self.Block(LeadFreeIndicator())
    self.id = self.Block(IdDots4())

  def refinements(self) -> Refinements:
    return super().refinements() + Refinements(
      instance_refinements=[
        (['mcu'], Esp32_Wroom_32),
        (['reg_3v3'], Ap3418),

        (['mcu', 'uart0', 'conn'], PinHeader254),
      ],
      instance_values=[
        (['mcu', 'pin_assigns'], [
          'spi.miso=NC',
          'i2c.scl=13',
          'i2c.sda=12',

          'lcd_cs=11',
          # 'lcd_reset=10',
          # 'lcd_dc=9',
          'spi.sck=8',
          # 'spi.mosi=7',

          # 'ledArray=4',

          'isense=4',  # use an input only pin

          'motor_2a1=26',
          'motor_2a2=27',
          'motor_2b2=28',
          'motor_2b1=29',
          'motor_1a1=30',
          'motor_1a2=31',
          'motor_1b2=33',
          'motor_1b1=36',
          'pwm=37',
        ]),
        (['isense', 'sense', 'res', 'res', 'require_basic_part'], False),

        # JLC does not have frequency specs, must be checked TODO
        (['reg_3v3', 'power_path', 'inductor', 'frequency'], Range(0, 0)),
        (['reg_3v3', 'power_path', 'efficiency'], Range(1.0, 1.0)),  # waive this check
        (['lcd', 'device', 'vbat_min'], 3.0),  # datasheet seems to be overly pessimistic
      ],
      class_refinements=[
        (PassiveConnector, JstPhKVertical),  # default connector series unless otherwise specified
        (Vl53l0x, Vl53l0xConnector),
        (TestPoint, TeRc),
        (Speaker, ConnectorSpeaker),
      ],
    )


class RobotDriver2TestCase(unittest.TestCase):
  def test_design(self) -> None:
    compile_board_inplace(RobotDriver2)
