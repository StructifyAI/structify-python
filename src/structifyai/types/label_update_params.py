# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable, Optional
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = [
    "LabelUpdateParams",
    "Body",
    "BodyInput",
    "BodyInputSave",
    "BodyInputSaveSave",
    "BodyInputSaveSaveEntity",
    "BodyInputSaveSaveRelationship",
    "BodyInputScroll",
    "BodyInputScrollScroll",
    "BodyInputExit",
    "BodyInputExitExit",
    "BodyInputClick",
    "BodyInputClickClick",
    "BodyInputHover",
    "BodyInputHoverHover",
    "BodyInputWait",
    "BodyInputWaitWait",
    "BodyInputError",
    "BodyInputErrorError",
    "BodyInputGoogle",
    "BodyInputGoogleGoogle",
    "BodyInputType",
    "BodyInputTypeType",
    "BodyResult",
    "BodyResultToolQueued",
    "BodyResultToolFail",
    "BodyResultInputParseFail",
    "BodyResultSuccess",
]


class LabelUpdateParams(TypedDict, total=False):
    run_uuid: Required[str]

    body: Required[Iterable[Body]]


class BodyInputSaveSaveEntity(TypedDict, total=False):
    id: Required[int]

    properties: Required[Dict[str, str]]

    type: Required[str]


class BodyInputSaveSaveRelationship(TypedDict, total=False):
    source: Required[int]

    target: Required[int]

    type: Required[str]


class BodyInputSaveSave(TypedDict, total=False):
    entities: Iterable[BodyInputSaveSaveEntity]

    relationships: Iterable[BodyInputSaveSaveRelationship]


class BodyInputSave(TypedDict, total=False):
    save: Required[Annotated[BodyInputSaveSave, PropertyInfo(alias="Save")]]
    """
    Knowledge graph info structured to deserialize and display in the same format
    that the LLM outputs.
    """


class BodyInputScrollScroll(TypedDict, total=False):
    reason: Required[str]
    """OpenAI Requires an argument, so we put a dummy one here."""


class BodyInputScroll(TypedDict, total=False):
    scroll: Required[Annotated[BodyInputScrollScroll, PropertyInfo(alias="Scroll")]]
    """For tools with no inputs."""


class BodyInputExitExit(TypedDict, total=False):
    reason: Required[str]
    """OpenAI Requires an argument, so we put a dummy one here."""


class BodyInputExit(TypedDict, total=False):
    exit: Required[Annotated[BodyInputExitExit, PropertyInfo(alias="Exit")]]
    """For tools with no inputs."""


class BodyInputClickClick(TypedDict, total=False):
    flag: Required[int]


class BodyInputClick(TypedDict, total=False):
    click: Required[Annotated[BodyInputClickClick, PropertyInfo(alias="Click")]]


class BodyInputHoverHover(TypedDict, total=False):
    flag: Required[int]


class BodyInputHover(TypedDict, total=False):
    hover: Required[Annotated[BodyInputHoverHover, PropertyInfo(alias="Hover")]]


class BodyInputWaitWait(TypedDict, total=False):
    seconds: Required[int]
    """Time in seconds to wait"""


class BodyInputWait(TypedDict, total=False):
    wait: Required[Annotated[BodyInputWaitWait, PropertyInfo(alias="Wait")]]


class BodyInputErrorError(TypedDict, total=False):
    error: Required[str]


class BodyInputError(TypedDict, total=False):
    error: Required[Annotated[BodyInputErrorError, PropertyInfo(alias="Error")]]


class BodyInputGoogleGoogle(TypedDict, total=False):
    query: Required[str]


class BodyInputGoogle(TypedDict, total=False):
    google: Required[Annotated[BodyInputGoogleGoogle, PropertyInfo(alias="Google")]]


class BodyInputTypeType(TypedDict, total=False):
    flag: Required[int]

    input: Required[str]


class BodyInputType(TypedDict, total=False):
    type: Required[Annotated[BodyInputTypeType, PropertyInfo(alias="Type")]]


BodyInput = Union[
    BodyInputSave,
    BodyInputScroll,
    BodyInputExit,
    BodyInputClick,
    BodyInputHover,
    BodyInputWait,
    BodyInputError,
    BodyInputGoogle,
    BodyInputType,
]


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
    input: Required[BodyInput]

    name: Required[Literal["Save", "Scroll", "Exit", "Click", "Hover", "Wait", "Error", "Google", "Type"]]

    result: Optional[BodyResult]
