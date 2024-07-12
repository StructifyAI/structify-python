# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable, Optional
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo
from .knowledge_graph_param import KnowledgeGraphParam

__all__ = [
    "LabelUpdateParams",
    "StepUpdate",
    "StepUpdateInput",
    "StepUpdateInputSave",
    "StepUpdateInputScroll",
    "StepUpdateInputScrollScroll",
    "StepUpdateInputExit",
    "StepUpdateInputExitExit",
    "StepUpdateInputClick",
    "StepUpdateInputClickClick",
    "StepUpdateInputHover",
    "StepUpdateInputHoverHover",
    "StepUpdateInputWait",
    "StepUpdateInputWaitWait",
    "StepUpdateInputError",
    "StepUpdateInputErrorError",
    "StepUpdateInputGoogle",
    "StepUpdateInputGoogleGoogle",
    "StepUpdateInputType",
    "StepUpdateInputTypeType",
    "StepUpdateResult",
    "StepUpdateResultToolQueued",
    "StepUpdateResultToolFail",
    "StepUpdateResultInputParseFail",
    "StepUpdateResultSuccess",
]


class LabelUpdateParams(TypedDict, total=False):
    run_uuid: Required[str]

    step_update: Required[Iterable[StepUpdate]]


class StepUpdateInputSave(TypedDict, total=False):
    save: Required[Annotated[KnowledgeGraphParam, PropertyInfo(alias="Save")]]
    """
    Knowledge graph info structured to deserialize and display in the same format
    that the LLM outputs. Also the first representation of an LLM output in the
    pipeline from raw tool output to being merged into a Neo4j DB
    """


class StepUpdateInputScrollScroll(TypedDict, total=False):
    reason: Required[str]
    """OpenAI Requires an argument, so we put a dummy one here."""


class StepUpdateInputScroll(TypedDict, total=False):
    scroll: Required[Annotated[StepUpdateInputScrollScroll, PropertyInfo(alias="Scroll")]]
    """For tools with no inputs."""


class StepUpdateInputExitExit(TypedDict, total=False):
    reason: Required[str]
    """OpenAI Requires an argument, so we put a dummy one here."""


class StepUpdateInputExit(TypedDict, total=False):
    exit: Required[Annotated[StepUpdateInputExitExit, PropertyInfo(alias="Exit")]]
    """For tools with no inputs."""


class StepUpdateInputClickClick(TypedDict, total=False):
    flag: Required[int]


class StepUpdateInputClick(TypedDict, total=False):
    click: Required[Annotated[StepUpdateInputClickClick, PropertyInfo(alias="Click")]]


class StepUpdateInputHoverHover(TypedDict, total=False):
    flag: Required[int]


class StepUpdateInputHover(TypedDict, total=False):
    hover: Required[Annotated[StepUpdateInputHoverHover, PropertyInfo(alias="Hover")]]


class StepUpdateInputWaitWait(TypedDict, total=False):
    seconds: Required[int]
    """Time in seconds to wait"""


class StepUpdateInputWait(TypedDict, total=False):
    wait: Required[Annotated[StepUpdateInputWaitWait, PropertyInfo(alias="Wait")]]


class StepUpdateInputErrorError(TypedDict, total=False):
    error: Required[str]


class StepUpdateInputError(TypedDict, total=False):
    error: Required[Annotated[StepUpdateInputErrorError, PropertyInfo(alias="Error")]]


class StepUpdateInputGoogleGoogle(TypedDict, total=False):
    query: Required[str]


class StepUpdateInputGoogle(TypedDict, total=False):
    google: Required[Annotated[StepUpdateInputGoogleGoogle, PropertyInfo(alias="Google")]]


class StepUpdateInputTypeType(TypedDict, total=False):
    flag: Required[int]

    input: Required[str]


class StepUpdateInputType(TypedDict, total=False):
    type: Required[Annotated[StepUpdateInputTypeType, PropertyInfo(alias="Type")]]


StepUpdateInput = Union[
    StepUpdateInputSave,
    StepUpdateInputScroll,
    StepUpdateInputExit,
    StepUpdateInputClick,
    StepUpdateInputHover,
    StepUpdateInputWait,
    StepUpdateInputError,
    StepUpdateInputGoogle,
    StepUpdateInputType,
]


class StepUpdateResultToolQueued(TypedDict, total=False):
    tool_queued: Required[Annotated[str, PropertyInfo(alias="ToolQueued")]]


class StepUpdateResultToolFail(TypedDict, total=False):
    tool_fail: Required[Annotated[str, PropertyInfo(alias="ToolFail")]]


class StepUpdateResultInputParseFail(TypedDict, total=False):
    input_parse_fail: Required[Annotated[str, PropertyInfo(alias="InputParseFail")]]


class StepUpdateResultSuccess(TypedDict, total=False):
    success: Required[Annotated[str, PropertyInfo(alias="Success")]]


StepUpdateResult = Union[
    StepUpdateResultToolQueued, StepUpdateResultToolFail, StepUpdateResultInputParseFail, StepUpdateResultSuccess
]


class StepUpdate(TypedDict, total=False):
    input: Required[StepUpdateInput]

    name: Required[Literal["Save", "Scroll", "Exit", "Click", "Hover", "Wait", "Error", "Google", "Type"]]

    result: Optional[StepUpdateResult]
