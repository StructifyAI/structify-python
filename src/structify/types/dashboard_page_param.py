# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable, Optional
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo
from .dashboard_component_param import DashboardComponentParam

__all__ = [
    "DashboardPageParam",
    "Control",
    "ControlDropdown",
    "ControlDropdownOption",
    "ControlRange",
    "ControlCheckbox",
    "ControlCheckboxOption",
]


class ControlDropdownOption(TypedDict, total=False):
    label: Required[str]

    value: Required[str]


class ControlDropdown(TypedDict, total=False):
    id: Required[str]

    field: Required[str]

    label: Required[str]

    options: Required[Iterable[ControlDropdownOption]]

    type: Required[Literal["dropdown"]]

    default_value: Optional[str]


class ControlRange(TypedDict, total=False):
    id: Required[str]

    field: Required[str]

    label: Required[str]

    max: Required[float]

    min: Required[float]

    type: Required[Literal["range"]]

    default_value: Optional[Iterable[float]]

    step: Optional[float]


class ControlCheckboxOption(TypedDict, total=False):
    label: Required[str]

    value: Required[str]


class ControlCheckbox(TypedDict, total=False):
    id: Required[str]

    field: Required[str]

    label: Required[str]

    options: Required[Iterable[ControlCheckboxOption]]

    type: Required[Literal["checkbox"]]

    default_value: Optional[SequenceNotStr[str]]


Control: TypeAlias = Union[ControlDropdown, ControlRange, ControlCheckbox]


class DashboardPageParam(TypedDict, total=False):
    """
    A dashboard groups components that share a common dataset.
    If dataset_node_name is None, components render static viz without Mosaic cross-filtering.
    """

    components: Required[Iterable[DashboardComponentParam]]
    """Components (charts) in this dashboard"""

    title: Required[str]
    """Title for this dashboard section"""

    controls: Optional[Iterable[Control]]
    """Control filters (dropdowns, checkboxes, ranges) for this dashboard"""

    dataset_node_name: Annotated[Optional[str], PropertyInfo(alias="datasetNodeName")]
    """
    Function name of the node that returns the dataset (DataFrame/Parquet). If None,
    no cross-filtering is available.
    """

    description: Optional[str]
    """Optional description"""
