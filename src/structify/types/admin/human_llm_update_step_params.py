# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable, Optional
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from ..._utils import PropertyInfo
from ..knowledge_graph_param import KnowledgeGraphParam

__all__ = [
    "HumanLlmUpdateStepParams",
    "ToolCall",
    "ToolCallInput",
    "ToolCallInputSave",
    "ToolCallInputScroll",
    "ToolCallInputScrollScroll",
    "ToolCallInputScrollToBottom",
    "ToolCallInputScrollToBottomScrollToBottom",
    "ToolCallInputExit",
    "ToolCallInputExitExit",
    "ToolCallInputClick",
    "ToolCallInputClickClick",
    "ToolCallInputHover",
    "ToolCallInputHoverHover",
    "ToolCallInputWait",
    "ToolCallInputWaitWait",
    "ToolCallInputError",
    "ToolCallInputErrorError",
    "ToolCallInputGoogle",
    "ToolCallInputGoogleGoogle",
    "ToolCallInputType",
    "ToolCallInputTypeType",
    "ToolCallResult",
    "ToolCallResultToolQueued",
    "ToolCallResultToolFail",
    "ToolCallResultInputParseFail",
    "ToolCallResultSuccess",
]


class HumanLlmUpdateStepParams(TypedDict, total=False):
    extraction_criteria_met: Required[bool]

    job_id: Required[str]

    step_id: Required[str]

    tool_calls: Required[Iterable[ToolCall]]


class ToolCallInputSave(TypedDict, total=False):
    save: Required[Annotated[KnowledgeGraphParam, PropertyInfo(alias="Save")]]
    """
    Knowledge graph info structured to deserialize and display in the same format
    that the LLM outputs. Also the first representation of an LLM output in the
    pipeline from raw tool output to being merged into a DB
    """


class ToolCallInputScrollScroll(TypedDict, total=False):
    reason: Required[str]
    """Dummy argument"""


class ToolCallInputScroll(TypedDict, total=False):
    scroll: Required[Annotated[ToolCallInputScrollScroll, PropertyInfo(alias="Scroll")]]
    """For tools with no inputs."""


class ToolCallInputScrollToBottomScrollToBottom(TypedDict, total=False):
    reason: Required[str]
    """Dummy argument"""


class ToolCallInputScrollToBottom(TypedDict, total=False):
    scroll_to_bottom: Required[
        Annotated[ToolCallInputScrollToBottomScrollToBottom, PropertyInfo(alias="ScrollToBottom")]
    ]
    """For tools with no inputs."""


class ToolCallInputExitExit(TypedDict, total=False):
    reason: Required[str]
    """Dummy argument"""


class ToolCallInputExit(TypedDict, total=False):
    exit: Required[Annotated[ToolCallInputExitExit, PropertyInfo(alias="Exit")]]
    """For tools with no inputs."""


class ToolCallInputClickClick(TypedDict, total=False):
    flag: Required[int]


class ToolCallInputClick(TypedDict, total=False):
    click: Required[Annotated[ToolCallInputClickClick, PropertyInfo(alias="Click")]]


class ToolCallInputHoverHover(TypedDict, total=False):
    flag: Required[int]


class ToolCallInputHover(TypedDict, total=False):
    hover: Required[Annotated[ToolCallInputHoverHover, PropertyInfo(alias="Hover")]]


class ToolCallInputWaitWait(TypedDict, total=False):
    seconds: int
    """Time in seconds to wait"""


class ToolCallInputWait(TypedDict, total=False):
    wait: Required[Annotated[ToolCallInputWaitWait, PropertyInfo(alias="Wait")]]


class ToolCallInputErrorError(TypedDict, total=False):
    error: Required[str]


class ToolCallInputError(TypedDict, total=False):
    error: Required[Annotated[ToolCallInputErrorError, PropertyInfo(alias="Error")]]


class ToolCallInputGoogleGoogle(TypedDict, total=False):
    query: Required[str]


class ToolCallInputGoogle(TypedDict, total=False):
    google: Required[Annotated[ToolCallInputGoogleGoogle, PropertyInfo(alias="Google")]]


class ToolCallInputTypeType(TypedDict, total=False):
    flag: Required[int]

    input: Required[str]


class ToolCallInputType(TypedDict, total=False):
    type: Required[Annotated[ToolCallInputTypeType, PropertyInfo(alias="Type")]]


ToolCallInput: TypeAlias = Union[
    ToolCallInputSave,
    ToolCallInputScroll,
    ToolCallInputScrollToBottom,
    ToolCallInputExit,
    ToolCallInputClick,
    ToolCallInputHover,
    ToolCallInputWait,
    ToolCallInputError,
    ToolCallInputGoogle,
    ToolCallInputType,
]


class ToolCallResultToolQueued(TypedDict, total=False):
    tool_queued: Required[Annotated[str, PropertyInfo(alias="ToolQueued")]]


class ToolCallResultToolFail(TypedDict, total=False):
    tool_fail: Required[Annotated[str, PropertyInfo(alias="ToolFail")]]


class ToolCallResultInputParseFail(TypedDict, total=False):
    input_parse_fail: Required[Annotated[str, PropertyInfo(alias="InputParseFail")]]


class ToolCallResultSuccess(TypedDict, total=False):
    success: Required[Annotated[str, PropertyInfo(alias="Success")]]


ToolCallResult: TypeAlias = Union[
    ToolCallResultToolQueued, ToolCallResultToolFail, ToolCallResultInputParseFail, ToolCallResultSuccess
]


class ToolCall(TypedDict, total=False):
    input: Required[ToolCallInput]

    name: Required[
        Literal["Exit", "Save", "Wait", "Type", "Scroll", "ScrollToBottom", "Click", "Hover", "Error", "Google"]
    ]

    result: Optional[ToolCallResult]
