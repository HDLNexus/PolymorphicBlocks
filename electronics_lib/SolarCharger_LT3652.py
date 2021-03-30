from electronics_abstract_parts import *
from electronics_lib import SmtInductor


class SolarCharger_LT3652(DiscreteChip, CircuitBlock):
  def __init__(self):
    super().__init__()

    # only required pins are Vcc, GND, DOUT, DIN
    # also need RTS, DTR for serial firmware updates
    # DNC pins that are not in use
    self.vin = self.Port(ElectricalSink(
      voltage_limits=(4.95, 32) * Volt,
      current_draw=(0, 3.5) * mAmp  # 2.5uA sleep, 29mA receive, 290 mA max transmit
    ), [Power])
    self.gnd = self.Port(Ground(), [Common])

    digital_model = DigitalBidir.from_supply(
      self.gnd, self.vin,
      voltage_limit_tolerance=(-0.3, 0.3)*Volt,  # TODO speculative default
      current_draw=(0, 0),  # TODO actually an unspecified default
      current_limits=(-2, 2) * mAmp,
      input_threshold_factor=(0.3, 0.7),
      output_threshold_factor=(0.05, 0.95)
    )

    adc_model = AnalogSink(
      voltage_limits=(2.65, 2.75) * Volt,
      current_draw=(35, 100) * nAmp,
      impedance=100*kOhm  # TODO no specs
    )

    pull_up_model = DigitalSink.from_supply(
      self.vin, self.gnd,
      voltage_limit_tolerance=(-0.3, 0.3)*Volt,  # TODO: FIX
      current_draw=(0, 0)*Amp,
      input_threshold_abs=(0.8, 2)*Volt
    )  # TODO: FIX

    # self.data = self.Port(UartPort(digital_model), [Input])
    #
    # self.rssi = self.Port(DigitalSource(digital_model), optional=True)
    # self.associate = self.Port(DigitalSource(digital_model), optional=True)

    self.vin_reg = self.Port(adc_model, optional=True)

    self.nshdn = self.Port(Passive(), optional=True) # self.Port(DigitalSink(pull_up_model), optional=True)
    self.nchrg = self.Port(DigitalSink(pull_up_model), optional=True)
    self.nfault = self.Port(DigitalSink(pull_up_model), optional=True)

    self.timer = self.Port(Passive(), optional=True)
    self.vfb = self.Port(ElectricalSink(digital_model), optional=True)
    self.ntc = self.Port(DigitalSource(digital_model), optional=True)
    self.bat = self.Port(ElectricalSource(digital_model), optional=True)
    self.sense = self.Port(ElectricalSink(digital_model), optional=True)
    self.boost = self.Port(ElectricalSink(digital_model), optional=True)
    self.sw = self.Port(ElectricalSource(digital_model), optional=True)

  def contents(self):
    super().contents()
    self.footprint(
      'U', 'Sparkfun_RF:XBEE',
      {
        '1': self.vin,
        '2': self.vin_reg,
        '3': self.nshdn,
        '4': self.nchrg,
        '5': self.nfault,
        '6': self.timer,
        '7': self.vfb,
        '8': self.ntc,
        '9': self.bat,
        '10': self.sense,
        '11': self.boost,
        '12': self.sw,
        '13': self.gnd,
      },
      # mfr='Digi International', part='XBP9B-*',
      # datasheet='https://www.digi.com/resources/documentation/digidocs/pdfs/90002173.pdf'
    )

class SolarCharger_LT3652_Module(CircuitBlock):
  @init_in_parent
  def __init__(self) -> None:
    super().__init__()
    self.gnd = self.Port(Ground())
    self.vin = self.Port(ElectricalSink(
      voltage_limits=(0.5, 5.5)*Volt,
      current_draw=(0, 0.5) * Amp  # TODO current draw specs, the part doesn't really have a datasheet
    ))
    self.vout = self.Port(ElectricalSource())

  def contents(self) -> None:
    super().contents()
    self.solar_charger = self.Block(SolarCharger_LT3652())

    self.timer_cap = self.Block(Capacitor())
    self.vin_cap = self.Block(Capacitor())
    self.vin_r1 = self.Block(Resistor())
    self.vin_r2 = self.Block(Resistor())
    self.sw_boost_cap = self.Block(Capacitor())
    self.bat_boost_diode = self.Block(Diode())
    self.gnd_sw_diode = self.Block(Diode())
    self.sense_res = self.Block(CurrentSenseResistor())
    self.bat_r1 = self.Block(Resistor())
    self.bat_r2 = self.Block(Resistor())
    self.bat_cap = self.Block(Capacitor())
    self.ind = self.Block(SmtInductor())

    self.footprint(
      'U', 'SolarCharger_LT3652_Module',
      {
        '1': self.gnd,
        '2': self.vin,
        '3': self.vout,
      }
    )
    # i/o connections
    self.connect(self.solar_charger.gnd, self.gnd)
    self.connect(self.solar_charger.vin, self.vin)
    self.connect(self.solar_charger.bat, self.vout)

    # timer
    self.connect(self.solar_charger.timer, self.timer_cap.pos)
    self.connect(self.gnd, self.timer_cap.neg.as_ground())

    # vin cap
    self.connect(self.vin, self.vin_cap.pos.as_electrical_sink())
    self.connect(self.gnd, self.vin_cap.neg.as_ground())

    # vin voltage divider
    self.connect(self.gnd, self.vin_r2.b.as_ground())
    self.connect(self.vin, self.vin_r1.a.as_electrical_sink())
    self.connect(self.solar_charger.vin_reg, self.vin_r1.b.as_analog_sink())
    self.connect(self.vin_r1.b, self.vin_r2.a)

    # sw boost cap
    self.connect(self.solar_charger.boost, self.sw_boost_cap.neg.as_electrical_sink())
    self.connect(self.solar_charger.sw, self.sw_boost_cap.pos.as_electrical_sink())

    # bat boost diode
    self.connect(self.solar_charger.boost, self.bat_boost_diode.cathode.as_electrical_sink())
    self.connect(self.solar_charger.bat, self.bat_boost_diode.anode.as_electrical_sink())

    # gnd sw diode
    self.connect(self.solar_charger.sw, self.gnd_sw_diode.cathode.as_electrical_sink())
    self.connect(self.gnd, self.gnd_sw_diode.anode.as_ground())

    # bat voltage divider
    self.connect(self.gnd, self.bat_r2.b.as_ground())
    self.connect(self.solar_charger.bat, self.bat_r1.a.as_electrical_sink())
    self.connect(self.solar_charger.vfb, self.bat_r1.b.as_electrical_sink())
    self.connect(self.bat_r1.b, self.bat_r2.a)

    # bat cap
    self.connect(self.vout, self.bat_cap.pos.as_electrical_sink())
    self.connect(self.gnd, self.bat_cap.neg.as_ground())

    # ind
    self.connect(self.gnd_sw_diode.cathode, self.ind.a)
    self.connect(self.solar_charger.sense, self.ind.b.as_electrical_sink())

    # vin nshdn
    self.connect(self.solar_charger.vin, self.solar_charger.nshdn.as_electrical_sink())

    # current sense resistor
    self.connect(self.solar_charger.sense, self.sense_res.pwr_out)
    self.connect(self.solar_charger.bat, self.sense_res.pwr_in)