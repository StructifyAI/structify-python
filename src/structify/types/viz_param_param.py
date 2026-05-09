# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from .viz_date_control_param import VizDateControlParam
from .viz_number_control_param import VizNumberControlParam
from .viz_string_control_param import VizStringControlParam
from .viz_boolean_control_param import VizBooleanControlParam

__all__ = ["VizParamParam", "String", "Number", "Boolean", "Date"]


class String(TypedDict, total=False):
    type: Required[Literal["string"]]

    value: Required[str]

    control: VizStringControlParam


class Number(TypedDict, total=False):
    type: Required[Literal["number"]]

    value: Required[float]

    control: VizNumberControlParam


class Boolean(TypedDict, total=False):
    type: Required[Literal["boolean"]]

    value: Required[bool]

    control: VizBooleanControlParam


class Date(TypedDict, total=False):
    type: Required[Literal["date"]]

    value: Required[str]

    control: VizDateControlParam


VizParamParam: TypeAlias = Union[String, Number, Boolean, Date]
