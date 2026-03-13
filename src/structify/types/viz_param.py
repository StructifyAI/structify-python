# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union, Optional
from typing_extensions import Literal, Annotated, TypeAlias

from .._utils import PropertyInfo
from .._models import BaseModel
from .viz_date_control import VizDateControl
from .viz_number_control import VizNumberControl
from .viz_string_control import VizStringControl
from .viz_boolean_control import VizBooleanControl

__all__ = ["VizParam", "String", "Number", "Boolean", "Date"]


class String(BaseModel):
    type: Literal["string"]

    value: str

    control: Optional[VizStringControl] = None


class Number(BaseModel):
    type: Literal["number"]

    value: float

    control: Optional[VizNumberControl] = None


class Boolean(BaseModel):
    type: Literal["boolean"]

    value: bool

    control: Optional[VizBooleanControl] = None


class Date(BaseModel):
    type: Literal["date"]

    value: str

    control: Optional[VizDateControl] = None


VizParam: TypeAlias = Annotated[Union[String, Number, Boolean, Date], PropertyInfo(discriminator="type")]
