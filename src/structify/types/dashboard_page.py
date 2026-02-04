# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import Literal, Annotated, TypeAlias

from pydantic import Field as FieldInfo

from .._utils import PropertyInfo
from .._models import BaseModel
from .dashboard_component import DashboardComponent

__all__ = [
    "DashboardPage",
    "Control",
    "ControlDropdown",
    "ControlDropdownOption",
    "ControlRange",
    "ControlCheckbox",
    "ControlCheckboxOption",
]


class ControlDropdownOption(BaseModel):
    label: str

    value: str


class ControlDropdown(BaseModel):
    id: str

    field: str

    label: str

    options: List[ControlDropdownOption]

    type: Literal["dropdown"]

    default_value: Optional[str] = None


class ControlRange(BaseModel):
    id: str

    field: str

    label: str

    max: float

    min: float

    type: Literal["range"]

    default_value: Optional[List[float]] = None

    step: Optional[float] = None


class ControlCheckboxOption(BaseModel):
    label: str

    value: str


class ControlCheckbox(BaseModel):
    id: str

    field: str

    label: str

    options: List[ControlCheckboxOption]

    type: Literal["checkbox"]

    default_value: Optional[List[str]] = None


Control: TypeAlias = Annotated[
    Union[ControlDropdown, ControlRange, ControlCheckbox], PropertyInfo(discriminator="type")
]


class DashboardPage(BaseModel):
    """
    A dashboard groups components that share a common dataset.
    If dataset_node_name is None, components render static viz without Mosaic cross-filtering.
    """

    components: List[DashboardComponent]
    """Components (charts) in this dashboard"""

    controls: Optional[List[Control]] = None
    """Control filters (dropdowns, checkboxes, ranges) for this dashboard"""

    dataset_node_name: Optional[str] = FieldInfo(alias="datasetNodeName", default=None)
    """
    Function name of the node that returns the dataset (DataFrame/Parquet). If None,
    no cross-filtering is available.
    """

    description: Optional[str] = None
    """Optional description"""

    title: Optional[str] = None
    """Title for this dashboard section"""
