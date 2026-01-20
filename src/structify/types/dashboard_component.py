# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from typing_extensions import TypeAlias

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["DashboardComponent", "Mosaic", "MosaicFields", "MosaicFieldsUnionMember2", "MosaicBin"]


class MosaicFieldsUnionMember2(BaseModel):
    expr: str

    target: Optional[str] = None
    """Optional Plotly property path (e.g., marker.color) to assign this column to"""


MosaicFields: TypeAlias = Union[str, bool, MosaicFieldsUnionMember2]


class MosaicBin(BaseModel):
    as_: str = FieldInfo(alias="as")

    field: str

    step: float


class Mosaic(BaseModel):
    fields: Dict[str, MosaicFields]

    bin: Optional[MosaicBin] = None

    group_by: Optional[List[str]] = FieldInfo(alias="groupBy", default=None)

    limit: Optional[int] = None

    order_by: Optional[str] = FieldInfo(alias="orderBy", default=None)

    table: Optional[str] = None
    """Table name - optional, derived from datasetNodeName in dashboard config"""


class DashboardComponent(BaseModel):
    """A component references a viz node and optionally includes mosaic metadata"""

    node_name: str
    """Function name of the viz node that outputs the chart spec"""

    title: str
    """Display title (overrides viz node title)"""

    description: Optional[str] = None
    """Description (optional, can override viz node's description)"""

    mosaic: Optional[Mosaic] = None

    span: Optional[int] = None
    """Grid span: 1 (quarter), 2 (half), 3 (three-quarters), 4 (full width)"""
