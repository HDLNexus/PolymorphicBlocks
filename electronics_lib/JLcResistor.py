from typing import Optional
from electronics_abstract_parts import *
from .JLcTable import *
from .JLcFootprint import JLcFootprint

class JLcResistorTable(JLcTable):
  RESISTANCE = PartsTableColumn(Range)
  POWER_RATING = PartsTableColumn(Range)
  FOOTPRINT = PartsTableColumn(str)

  PACKAGE_FOOTPRINT_MAP = {
    '0603': 'Resistor_SMD:R_0603_1608Metric',
    '0805': 'Resistor_SMD:R_0805_2012Metric',
    '1206': 'Resistor_SMD:R_1206_3216Metric',
  }

  @classmethod
  def _generate_table(cls) -> PartsTable:
    RESISTOR_MATCHES = {
      'resistance': "(\d+(?:\.\d*)?[GMkmunp]?[\u03A9])",
      'tolerance': "([\u00B1]\d+(?:\.\d*)?%)",
      'power': "(\d+(?:\.\d*)?[GMkmunp]?W)",
    }

    def parse_row(row: PartsTableRow) -> Optional[Dict[PartsTableColumn, Any]]:
      if (row['Library Type'] == 'Basic' and row['First Category'] == 'Resistors'):
        new_cols: Dict[PartsTableColumn, Any] = {}
        try:
          # handle the footprint first since this is the most likely to filter
          new_cols[cls.FOOTPRINT] = cls.PACKAGE_FOOTPRINT_MAP[row['Package']]
          new_cols.update(cls._parse_jlcpcb_common(row))

          extracted_values = JLcTable.parse(row[JLcTable.DESCRIPTION], RESISTOR_MATCHES)

          new_cols[cls.RESISTANCE] = Range.from_tolerance(
            PartsTableUtil.parse_value(extracted_values['resistance'], 'Ω'),
            PartsTableUtil.parse_tolerance(extracted_values['tolerance'])
          )

          new_cols[cls.POWER_RATING] = Range.zero_to_upper(PartsTableUtil.parse_value(extracted_values['power'], 'W'))

          return new_cols
        except (KeyError, PartsTableUtil.ParseError):
          return None

    raw_table = PartsTable.from_csv_files(PartsTableUtil.with_source_dir([
      'JLCPCB_SMT_Parts_Library.csv'
    ], 'resources'), encoding='gb2312')
    return raw_table.map_new_columns(parse_row).sort_by(
      lambda row: [row[cls.COST], row[cls.FOOTPRINT]]
    )


class JLcResistor(Resistor, JLcFootprint, FootprintBlock, GeneratorBlock):
  @init_in_parent
  def __init__(self, **kwargs):
    super().__init__(**kwargs)
    self.part_spec = self.Parameter(StringExpr(""))
    self.footprint_spec = self.Parameter(StringExpr(""))
    self.generator(self.select_resistor, self.spec_resistance, self.power,
                   self.part_spec, self.footprint_spec)

    # Output values
    self.selected_resistance = self.Parameter(RangeExpr())
    self.selected_power = self.Parameter(RangeExpr())

  def select_resistor(self, resistance: Range, power_dissipation: Range,
                      part_spec: str, footprint_spec: str) -> None:
    part = JLcResistorTable.table().filter(lambda row: (
            (not part_spec or part_spec == row[JLcResistorTable.PART_NUMBER]) and
            (not footprint_spec or footprint_spec == row[JLcResistorTable.FOOTPRINT]) and
            row[JLcResistorTable.RESISTANCE].fuzzy_in(resistance) and
            power_dissipation.fuzzy_in(row[JLcResistorTable.POWER_RATING])
    )).first(f"no resistors in {resistance} Ohm, {power_dissipation} W")

    self.assign(self.selected_resistance, part[JLcResistorTable.RESISTANCE])
    self.assign(self.selected_power, part[JLcResistorTable.POWER_RATING])
    self.assign(self.lcsc_part, part[JLcTable.DISTRIBUTER_PART_NUMBER])

    self.footprint(
      'R', part[JLcResistorTable.FOOTPRINT],
      {
        '1': self.a,
        '2': self.b,
      },
      mfr=part[JLcResistorTable.MANUFACTURER], part=part[JLcResistorTable.PART_NUMBER],
      value=f"{part[JLcTable.DESCRIPTION]}",
      datasheet=part[JLcResistorTable.DATASHEETS]
    )