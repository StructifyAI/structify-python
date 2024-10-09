# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable, Optional
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from .._utils import PropertyInfo
from .chat_prompt_param import ChatPromptParam
from .knowledge_graph_param import KnowledgeGraphParam

__all__ = [
    "ExecutionStepParam",
    "Response",
    "ResponseToolCall",
    "ResponseToolCallInput",
    "ResponseToolCallInputSave",
    "ResponseToolCallInputScroll",
    "ResponseToolCallInputScrollScroll",
    "ResponseToolCallInputExit",
    "ResponseToolCallInputExitExit",
    "ResponseToolCallInputClick",
    "ResponseToolCallInputClickClick",
    "ResponseToolCallInputHover",
    "ResponseToolCallInputHoverHover",
    "ResponseToolCallInputWait",
    "ResponseToolCallInputWaitWait",
    "ResponseToolCallInputError",
    "ResponseToolCallInputErrorError",
    "ResponseToolCallInputGoogle",
    "ResponseToolCallInputGoogleGoogle",
    "ResponseToolCallInputType",
    "ResponseToolCallInputTypeType",
    "ResponseToolCallResult",
    "ResponseToolCallResultToolQueued",
    "ResponseToolCallResultToolFail",
    "ResponseToolCallResultInputParseFail",
    "ResponseToolCallResultSuccess",
]


class ResponseToolCallInputSave(TypedDict, total=False):
    save: Required[Annotated[KnowledgeGraphParam, PropertyInfo(alias="Save")]]
    """
    Knowledge graph info structured to deserialize and display in the same format
    that the LLM outputs. Also the first representation of an LLM output in the
    pipeline from raw tool output to being merged into a Neo4j DB
    """


class ResponseToolCallInputScrollScroll(TypedDict, total=False):
    reason: Required[str]
    """Dummy argument"""


class ResponseToolCallInputScroll(TypedDict, total=False):
    scroll: Required[Annotated[ResponseToolCallInputScrollScroll, PropertyInfo(alias="Scroll")]]
    """For tools with no inputs."""


class ResponseToolCallInputExitExit(TypedDict, total=False):
    reason: Required[str]
    """Dummy argument"""


class ResponseToolCallInputExit(TypedDict, total=False):
    exit: Required[Annotated[ResponseToolCallInputExitExit, PropertyInfo(alias="Exit")]]
    """For tools with no inputs."""


class ResponseToolCallInputClickClick(TypedDict, total=False):
    flag: Required[int]


class ResponseToolCallInputClick(TypedDict, total=False):
    click: Required[Annotated[ResponseToolCallInputClickClick, PropertyInfo(alias="Click")]]


class ResponseToolCallInputHoverHover(TypedDict, total=False):
    flag: Required[int]


class ResponseToolCallInputHover(TypedDict, total=False):
    hover: Required[Annotated[ResponseToolCallInputHoverHover, PropertyInfo(alias="Hover")]]


class ResponseToolCallInputWaitWait(TypedDict, total=False):
    seconds: int
    """Time in seconds to wait"""


class ResponseToolCallInputWait(TypedDict, total=False):
    wait: Required[Annotated[ResponseToolCallInputWaitWait, PropertyInfo(alias="Wait")]]


class ResponseToolCallInputErrorError(TypedDict, total=False):
    error: Required[str]


class ResponseToolCallInputError(TypedDict, total=False):
    error: Required[Annotated[ResponseToolCallInputErrorError, PropertyInfo(alias="Error")]]


class ResponseToolCallInputGoogleGoogle(TypedDict, total=False):
    query: Required[str]


class ResponseToolCallInputGoogle(TypedDict, total=False):
    google: Required[Annotated[ResponseToolCallInputGoogleGoogle, PropertyInfo(alias="Google")]]


class ResponseToolCallInputTypeType(TypedDict, total=False):
    flag: Required[int]

    input: Required[str]


class ResponseToolCallInputType(TypedDict, total=False):
    type: Required[Annotated[ResponseToolCallInputTypeType, PropertyInfo(alias="Type")]]


ResponseToolCallInput: TypeAlias = Union[
    ResponseToolCallInputSave,
    ResponseToolCallInputScroll,
    ResponseToolCallInputExit,
    ResponseToolCallInputClick,
    ResponseToolCallInputHover,
    ResponseToolCallInputWait,
    ResponseToolCallInputError,
    ResponseToolCallInputGoogle,
    ResponseToolCallInputType,
]


class ResponseToolCallResultToolQueued(TypedDict, total=False):
    tool_queued: Required[Annotated[str, PropertyInfo(alias="ToolQueued")]]


class ResponseToolCallResultToolFail(TypedDict, total=False):
    tool_fail: Required[Annotated[str, PropertyInfo(alias="ToolFail")]]


class ResponseToolCallResultInputParseFail(TypedDict, total=False):
    input_parse_fail: Required[Annotated[str, PropertyInfo(alias="InputParseFail")]]


class ResponseToolCallResultSuccess(TypedDict, total=False):
    success: Required[Annotated[str, PropertyInfo(alias="Success")]]


ResponseToolCallResult: TypeAlias = Union[
    ResponseToolCallResultToolQueued,
    ResponseToolCallResultToolFail,
    ResponseToolCallResultInputParseFail,
    ResponseToolCallResultSuccess,
]


class ResponseToolCall(TypedDict, total=False):
    input: Required[ResponseToolCallInput]

    name: Required[Literal["Save", "Scroll", "Exit", "Click", "Hover", "Wait", "Error", "Google", "Type"]]

    result: Optional[ResponseToolCallResult]


class Response(TypedDict, total=False):
    completion_tokens: Required[int]

    cost: Required[float]
    """Cost in dollars"""

    llm: Required[str]

    prompt_tokens: Required[int]
    """New tokens"""

    text: Required[str]

    tool_calls: Required[Iterable[ResponseToolCall]]


class ExecutionStepParam(TypedDict, total=False):
    id: Required[str]

    prompt: Required[ChatPromptParam]

    response: Required[Response]
