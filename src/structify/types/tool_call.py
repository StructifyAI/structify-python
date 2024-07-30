# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .exit import Exit
from .save import Save
from .type import Type
from .wait import Wait
from .click import Click
from .error import Error
from .hover import Hover
from .google import Google
from .scroll import Scroll
from .._models import BaseModel

__all__ = ["ToolCall", "Input", "Result", "ResultToolQueued", "ResultToolFail", "ResultInputParseFail", "ResultSuccess"]

Input = Union[Save, Scroll, Exit, Click, Hover, Wait, Error, Google, Type]


class ResultToolQueued(BaseModel):
    tool_queued: str = FieldInfo(alias="ToolQueued")


class ResultToolFail(BaseModel):
    tool_fail: str = FieldInfo(alias="ToolFail")


class ResultInputParseFail(BaseModel):
    input_parse_fail: str = FieldInfo(alias="InputParseFail")


class ResultSuccess(BaseModel):
    success: str = FieldInfo(alias="Success")


Result = Union[ResultToolQueued, ResultToolFail, ResultInputParseFail, ResultSuccess, None]


class ToolCall(BaseModel):
    input: Input

    name: Literal["Save", "Scroll", "Exit", "Click", "Hover", "Wait", "Error", "Google", "Type"]

    result: Optional[Result] = None
