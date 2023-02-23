import unittest
from typing import List, Dict

from edg import *


class CharlieplexedLedMatrix(Light, GeneratorBlock):
  """A LED matrix that saves on IO pins by charlieplexing, only requiring max(rows + 1, cols) GPIOs to control.
  Requires IOs that can tri-state, and requires scanning through rows (so not all LEDs are simultaneously on).

  Anodes (columns) are directly connected to the IO line, while the cathodes (rows) are connected through a resistor.
  A generalization of https://en.wikipedia.org/wiki/Charlieplexing#/media/File:3-pin_Charlieplexing_matrix_with_common_resistors.svg
  """
  @init_in_parent
  def __init__(self, rows: IntLike, cols: IntLike, skip: ArrayIntLike = [],
               color: LedColorLike = Led.Any, current_draw: RangeLike = (1, 10)*mAmp):
    super().__init__()

    self.current_draw = self.ArgParameter(current_draw)
    self.color = self.ArgParameter(color)

    # note that IOs supply both the positive and negative
    self.ios = self.Port(Vector(DigitalSink.empty()))

    self.generator(self.generate, rows, cols, skip)

  def generate(self, rows: int, cols: int, skip: List[int]):
    num_ios = max(rows, cols + 1)

    io_voltage = self.ios.hull(lambda x: x.link().voltage)
    io_voltage_upper = io_voltage.upper()
    io_voltage_lower = self.ios.hull(lambda x: x.link().output_thresholds).upper()

    # internally, this uses passive ports on all the components, and only casts to a DigitalSink at the end
    # which is necessary to account for that not all LEDs can be simultaneously on
    passive_ios: Dict[int, Passive] = {}  # keeps the passive-side port for each boundary IO
    def connect_passive_io(index: int, io: Passive):
      # connects a Passive-typed IO to the index, handling the first and subsequent case
      if index in passive_ios:
        self.connect(passive_ios[index], io)  # subsequent case, actually do the connection
      else:
        passive_ios[index] = io  # first case, just bootstrap the data structure

    self.res = ElementDict[Resistor]()
    res_model = Resistor(
      resistance=(io_voltage_upper / self.current_draw.upper(),
                  io_voltage_lower / self.current_draw.lower())
    )
    self.led = ElementDict[Led]()
    led_model = Led(color=self.color)

    # generate the resistor and LEDs for each column
    for col in range(cols):
      # generate the cathode resistor, guaranteed one per column
      self.res[str(col)] = res = self.Block(res_model)
      connect_passive_io (col, res.b)
      for row in range(rows):
        self.led[f"{row}_{col}"] = led = self.Block(led_model)
        self.connect(led.k, res.a)
        if row >= col:  # displaced by resistor
          connect_passive_io(row + 1, led.a)
        else:
          connect_passive_io(row, led.a)

    # generate the adapters and connect the internal passive IO to external typed IO
    for index, passive_io in passive_ios.items():
      # if there is a cathode resistor attached to this index, then include the sunk current
      if index < cols:
        sink_res = self.res[str(index)]
        sink_current = -(io_voltage / sink_res.actual_resistance).upper() * cols
      else:
        sink_current = 0 * mAmp

      # then add the maximum of the LED source currents, for the rest of the cathode lines
      source_current = 0 * mAmp
      for col in range(cols):
        col_res = self.res[str(col)]
        source_current = (io_voltage / col_res.actual_resistance).upper().max(source_current)

      self.connect(self.ios.append_elt(DigitalSink.empty(), str(index)),
                   passive_io.adapt_to(DigitalSink(current_draw=(sink_current, source_current))))


class LedMatrixTest(JlcBoardTop):
  """A USB-connected WiFi-enabled LED matrix that demonstrates a charlieplexing LED matrix generator.
  """
  def contents(self) -> None:
    super().contents()

    self.usb = self.Block(UsbCReceptacle())

    self.vusb = self.connect(self.usb.pwr)
    self.gnd = self.connect(self.usb.gnd)

    self.tp_vusb = self.Block(VoltageTestPoint()).connected(self.usb.pwr)
    self.tp_gnd = self.Block(VoltageTestPoint()).connected(self.usb.gnd)

    # POWER
    with self.implicit_connect(
        ImplicitConnect(self.gnd, [Common]),
    ) as imp:
      (self.reg_3v3, self.tp_3v3, self.prot_3v3), _ = self.chain(
        self.vusb,
        imp.Block(LinearRegulator(output_voltage=3.3*Volt(tol=0.05))),
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

      (self.sw1, ), _ = self.chain(imp.Block(DigitalSwitch()), self.mcu.gpio.request('sw1'))

      # maximum current draw that is still within the column sink capability of the ESP32
      self.matrix = imp.Block(CharlieplexedLedMatrix(6, 5, current_draw=(3.5, 5)*mAmp, color=Led.Yellow))
      self.connect(self.mcu.gpio.request_vector('led'), self.matrix.ios)
      (self.usb_esd, ), _ = self.chain(self.usb.usb, imp.Block(UsbEsdDiode()), self.mcu.usb.request())

    # Misc board
    self.duck = self.Block(DuckLogo())
    self.leadfree = self.Block(LeadFreeIndicator())
    self.id = self.Block(IdDots4())

  def multipack(self) -> None:
    self.matrix_res1 = self.PackedBlock(ResistorArray())
    self.pack(self.matrix_res1.elements.request('0'), ['matrix', 'res[0]'])
    self.pack(self.matrix_res1.elements.request('1'), ['matrix', 'res[1]'])
    self.pack(self.matrix_res1.elements.request('2'), ['matrix', 'res[2]'])

    self.matrix_res2 = self.PackedBlock(ResistorArray())
    self.pack(self.matrix_res2.elements.request('0'), ['matrix', 'res[3]'])
    self.pack(self.matrix_res2.elements.request('1'), ['matrix', 'res[4]'])

  def refinements(self) -> Refinements:
    return super().refinements() + Refinements(
      instance_refinements=[
        (['mcu'], Esp32c3_Wroom02),
        (['reg_3v3'], Ldl1117),
      ],
      instance_values=[
        (['mcu', 'pin_assigns'], [
          'led_0=3',
          'led_1=4',
          'led_2=5',
          'led_3=6',
          'led_4=17',
          'led_5=15',
          'led_6=10',
          'sw1=18',
        ]),
      ],
      class_refinements=[
        (PassiveConnector, PinHeader254),
      ],
    )


class LedMatrixTestCase(unittest.TestCase):
  def test_design(self) -> None:
    compile_board_inplace(LedMatrixTest)
