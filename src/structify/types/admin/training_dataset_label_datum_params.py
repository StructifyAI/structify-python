# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable, Optional
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from ..._utils import PropertyInfo
from .datum_status import DatumStatus
from ..knowledge_graph_param import KnowledgeGraphParam

__all__ = [
    "TrainingDatasetLabelDatumParams",
    "UpdatedToolCall",
    "UpdatedToolCallInput",
    "UpdatedToolCallInputSave",
    "UpdatedToolCallInputScroll",
    "UpdatedToolCallInputScrollScroll",
    "UpdatedToolCallInputScrollToBottom",
    "UpdatedToolCallInputScrollToBottomScrollToBottom",
    "UpdatedToolCallInputExit",
    "UpdatedToolCallInputExitExit",
    "UpdatedToolCallInputClick",
    "UpdatedToolCallInputClickClick",
    "UpdatedToolCallInputHover",
    "UpdatedToolCallInputHoverHover",
    "UpdatedToolCallInputWait",
    "UpdatedToolCallInputWaitWait",
    "UpdatedToolCallInputError",
    "UpdatedToolCallInputErrorError",
    "UpdatedToolCallInputGoogle",
    "UpdatedToolCallInputGoogleGoogle",
    "UpdatedToolCallInputType",
    "UpdatedToolCallInputTypeType",
    "UpdatedToolCallResult",
    "UpdatedToolCallResultToolQueued",
    "UpdatedToolCallResultToolFail",
    "UpdatedToolCallResultInputParseFail",
    "UpdatedToolCallResultSuccess",
]


class TrainingDatasetLabelDatumParams(TypedDict, total=False):
    id: Required[str]

    status: Required[DatumStatus]

    updated_tool_calls: Required[Iterable[UpdatedToolCall]]


class UpdatedToolCallInputSave(TypedDict, total=False):
    save: Required[Annotated[KnowledgeGraphParam, PropertyInfo(alias="Save")]]
    """
    Knowledge graph info structured to deserialize and display in the same format
    that the LLM outputs. Also the first representation of an LLM output in the
    pipeline from raw tool output to being merged into a Neo4j DB
    """


class UpdatedToolCallInputScrollScroll(TypedDict, total=False):
    reason: Required[str]
    """Dummy argument"""


class UpdatedToolCallInputScroll(TypedDict, total=False):
    scroll: Required[Annotated[UpdatedToolCallInputScrollScroll, PropertyInfo(alias="Scroll")]]
    """For tools with no inputs."""


class UpdatedToolCallInputScrollToBottomScrollToBottom(TypedDict, total=False):
    reason: Required[str]
    """Dummy argument"""


class UpdatedToolCallInputScrollToBottom(TypedDict, total=False):
    scroll_to_bottom: Required[
        Annotated[UpdatedToolCallInputScrollToBottomScrollToBottom, PropertyInfo(alias="ScrollToBottom")]
    ]
    """For tools with no inputs."""


class UpdatedToolCallInputExitExit(TypedDict, total=False):
    reason: Required[str]
    """Dummy argument"""


class UpdatedToolCallInputExit(TypedDict, total=False):
    exit: Required[Annotated[UpdatedToolCallInputExitExit, PropertyInfo(alias="Exit")]]
    """For tools with no inputs."""


class UpdatedToolCallInputClickClick(TypedDict, total=False):
    flag: Required[int]


class UpdatedToolCallInputClick(TypedDict, total=False):
    click: Required[Annotated[UpdatedToolCallInputClickClick, PropertyInfo(alias="Click")]]


class UpdatedToolCallInputHoverHover(TypedDict, total=False):
    flag: Required[int]


class UpdatedToolCallInputHover(TypedDict, total=False):
    hover: Required[Annotated[UpdatedToolCallInputHoverHover, PropertyInfo(alias="Hover")]]


class UpdatedToolCallInputWaitWait(TypedDict, total=False):
    seconds: int
    """Time in seconds to wait"""


class UpdatedToolCallInputWait(TypedDict, total=False):
    wait: Required[Annotated[UpdatedToolCallInputWaitWait, PropertyInfo(alias="Wait")]]


class UpdatedToolCallInputErrorError(TypedDict, total=False):
    error: Required[str]


class UpdatedToolCallInputError(TypedDict, total=False):
    error: Required[Annotated[UpdatedToolCallInputErrorError, PropertyInfo(alias="Error")]]


class UpdatedToolCallInputGoogleGoogle(TypedDict, total=False):
    query: Required[str]


class UpdatedToolCallInputGoogle(TypedDict, total=False):
    google: Required[Annotated[UpdatedToolCallInputGoogleGoogle, PropertyInfo(alias="Google")]]


class UpdatedToolCallInputTypeType(TypedDict, total=False):
    flag: Required[int]

    input: Required[str]


class UpdatedToolCallInputType(TypedDict, total=False):
    type: Required[Annotated[UpdatedToolCallInputTypeType, PropertyInfo(alias="Type")]]


UpdatedToolCallInput: TypeAlias = Union[
    UpdatedToolCallInputSave,
    UpdatedToolCallInputScroll,
    UpdatedToolCallInputScrollToBottom,
    UpdatedToolCallInputExit,
    UpdatedToolCallInputClick,
    UpdatedToolCallInputHover,
    UpdatedToolCallInputWait,
    UpdatedToolCallInputError,
    UpdatedToolCallInputGoogle,
    UpdatedToolCallInputType,
]


class UpdatedToolCallResultToolQueued(TypedDict, total=False):
    tool_queued: Required[Annotated[str, PropertyInfo(alias="ToolQueued")]]


class UpdatedToolCallResultToolFail(TypedDict, total=False):
    tool_fail: Required[Annotated[str, PropertyInfo(alias="ToolFail")]]


class UpdatedToolCallResultInputParseFail(TypedDict, total=False):
    input_parse_fail: Required[Annotated[str, PropertyInfo(alias="InputParseFail")]]


class UpdatedToolCallResultSuccess(TypedDict, total=False):
    success: Required[Annotated[str, PropertyInfo(alias="Success")]]


UpdatedToolCallResult: TypeAlias = Union[
    UpdatedToolCallResultToolQueued,
    UpdatedToolCallResultToolFail,
    UpdatedToolCallResultInputParseFail,
    UpdatedToolCallResultSuccess,
]


class UpdatedToolCall(TypedDict, total=False):
    input: Required[UpdatedToolCallInput]

    name: Required[
        Literal["Exit", "Save", "Wait", "Type", "Scroll", "ScrollToBottom", "Click", "Hover", "Error", "Google"]
    ]

    result: Optional[UpdatedToolCallResult]
