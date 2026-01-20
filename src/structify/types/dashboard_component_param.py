# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Optional
from typing_extensions import Required, Annotated, TypeAlias, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo

__all__ = ["DashboardComponentParam", "Mosaic", "MosaicFields", "MosaicFieldsUnionMember2", "MosaicBin"]


class MosaicFieldsUnionMember2(TypedDict, total=False):
    expr: Required[str]

    target: Optional[str]
    """Optional Plotly property path (e.g., marker.color) to assign this column to"""


MosaicFields: TypeAlias = Union[str, bool, MosaicFieldsUnionMember2]

_MosaicBinReservedKeywords = TypedDict(
    "_MosaicBinReservedKeywords",
    {
        "as": str,
    },
    total=False,
)


class MosaicBin(_MosaicBinReservedKeywords, total=False):
    field: Required[str]

    step: Required[float]


class Mosaic(TypedDict, total=False):
    fields: Required[Dict[str, MosaicFields]]

    bin: Optional[MosaicBin]

    group_by: Annotated[Optional[SequenceNotStr[str]], PropertyInfo(alias="groupBy")]

    limit: Optional[int]

    order_by: Annotated[Optional[str], PropertyInfo(alias="orderBy")]

    table: Optional[str]
    """Table name - optional, derived from datasetNodeName in dashboard config"""


class DashboardComponentParam(TypedDict, total=False):
    """A component references a viz node and optionally includes mosaic metadata"""

    node_name: Required[str]
    """Function name of the viz node that outputs the chart spec"""

    title: Required[str]
    """Display title (overrides viz node title)"""

    description: Optional[str]
    """Description (optional, can override viz node's description)"""

    mosaic: Optional[Mosaic]

    span: Optional[int]
    """Grid span: 1 (quarter), 2 (half), 3 (three-quarters), 4 (full width)"""
