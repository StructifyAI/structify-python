# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable, Optional
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo
from .tool_input_param import ToolInputParam

__all__ = [
    "UpdateCreateParams",
    "Body",
    "BodyResult",
    "BodyResultToolQueued",
    "BodyResultToolFail",
    "BodyResultInputParseFail",
    "BodyResultSuccess",
]


class UpdateCreateParams(TypedDict, total=False):
    run_uuid: Required[str]

    body: Required[Iterable[Body]]


class BodyResultToolQueued(TypedDict, total=False):
    tool_queued: Required[Annotated[str, PropertyInfo(alias="ToolQueued")]]


class BodyResultToolFail(TypedDict, total=False):
    tool_fail: Required[Annotated[str, PropertyInfo(alias="ToolFail")]]


class BodyResultInputParseFail(TypedDict, total=False):
    input_parse_fail: Required[Annotated[str, PropertyInfo(alias="InputParseFail")]]


class BodyResultSuccess(TypedDict, total=False):
    success: Required[Annotated[str, PropertyInfo(alias="Success")]]


BodyResult = Union[BodyResultToolQueued, BodyResultToolFail, BodyResultInputParseFail, BodyResultSuccess]


class Body(TypedDict, total=False):
    input: Required[ToolInputParam]

    name: Required[Literal["Save", "Scroll", "Exit", "Click", "Hover", "Wait", "Error", "Google", "Type"]]

    result: Optional[BodyResult]
