from typing import Any, Optional, Dict
from ..abstract_parts import *
from ..parts.JlcFerriteBead import JlcFerriteBead
from .JlcPartsBase import JlcPartsBase, JlcPartsAttributes


class JlcPartsFerriteBead(TableFerriteBead, PartsTableSelectorFootprint, JlcPartsBase):
    _JLC_PARTS_FILE_NAMES = ["FiltersakaEMI_OptimizationFerrite_Beads"]

    @classmethod
    def _entry_to_table_row(cls, row_dict: Dict[PartsTableColumn, Any], filename: str, package: str, attributes: JlcPartsAttributes) \
            -> Optional[Dict[PartsTableColumn, Any]]:
        try:
            row_dict[cls.KICAD_FOOTPRINT] = JlcFerriteBead.PACKAGE_FOOTPRINT_MAP[package]

            try:  # sometimes '-'
                current_rating = PartParserUtil.parse_value(
                    attributes.get("Current rating", str), 'A')
            except (KeyError, PartParserUtil.ParseError):
                current_rating = 0
            row_dict[cls.CURRENT_RATING] = Range.zero_to_upper(current_rating)
            # Dc resistance sometimes NaN
            row_dict[cls.DC_RESISTANCE] = Range.exact(attributes.get("Dc resistance", float, sub='resistance'))
            row_dict[cls.HF_IMPEDANCE] = Range.exact(
                attributes.get("Impedance @ frequency", float, sub='esr'))

            return row_dict
        except (KeyError, TypeError, PartParserUtil.ParseError):
            return None


lambda: JlcPartsFerriteBead()  # ensure class is instantiable (non-abstract)
