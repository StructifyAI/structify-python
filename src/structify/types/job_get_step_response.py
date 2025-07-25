# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .chat_prompt import ChatPrompt
from .knowledge_graph import KnowledgeGraph

__all__ = [
    "JobGetStepResponse",
    "Response",
    "ResponseToolCall",
    "ResponseToolCallInput",
    "ResponseToolCallInputSave",
    "ResponseToolCallInputScroll",
    "ResponseToolCallInputScrollScroll",
    "ResponseToolCallInputScrollToBottom",
    "ResponseToolCallInputScrollToBottomScrollToBottom",
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


class ResponseToolCallInputSave(BaseModel):
    save: KnowledgeGraph = FieldInfo(alias="Save")
    """
    Knowledge graph info structured to deserialize and display in the same format
    that the LLM outputs. Also the first representation of an LLM output in the
    pipeline from raw tool output to being merged into a DB
    """


class ResponseToolCallInputScrollScroll(BaseModel):
    reason: str
    """Dummy argument"""


class ResponseToolCallInputScroll(BaseModel):
    scroll: ResponseToolCallInputScrollScroll = FieldInfo(alias="Scroll")
    """For tools with no inputs."""


class ResponseToolCallInputScrollToBottomScrollToBottom(BaseModel):
    reason: str
    """Dummy argument"""


class ResponseToolCallInputScrollToBottom(BaseModel):
    scroll_to_bottom: ResponseToolCallInputScrollToBottomScrollToBottom = FieldInfo(alias="ScrollToBottom")
    """For tools with no inputs."""


class ResponseToolCallInputExitExit(BaseModel):
    reason: str
    """Dummy argument"""


class ResponseToolCallInputExit(BaseModel):
    exit: ResponseToolCallInputExitExit = FieldInfo(alias="Exit")
    """For tools with no inputs."""


class ResponseToolCallInputClickClick(BaseModel):
    flag: int


class ResponseToolCallInputClick(BaseModel):
    click: ResponseToolCallInputClickClick = FieldInfo(alias="Click")


class ResponseToolCallInputHoverHover(BaseModel):
    flag: int


class ResponseToolCallInputHover(BaseModel):
    hover: ResponseToolCallInputHoverHover = FieldInfo(alias="Hover")


class ResponseToolCallInputWaitWait(BaseModel):
    seconds: Optional[int] = None
    """Time in seconds to wait"""


class ResponseToolCallInputWait(BaseModel):
    wait: ResponseToolCallInputWaitWait = FieldInfo(alias="Wait")


class ResponseToolCallInputErrorError(BaseModel):
    error: str


class ResponseToolCallInputError(BaseModel):
    error: ResponseToolCallInputErrorError = FieldInfo(alias="Error")


class ResponseToolCallInputGoogleGoogle(BaseModel):
    query: str


class ResponseToolCallInputGoogle(BaseModel):
    google: ResponseToolCallInputGoogleGoogle = FieldInfo(alias="Google")


class ResponseToolCallInputTypeType(BaseModel):
    flag: int

    input: str


class ResponseToolCallInputType(BaseModel):
    type: ResponseToolCallInputTypeType = FieldInfo(alias="Type")


ResponseToolCallInput: TypeAlias = Union[
    ResponseToolCallInputSave,
    ResponseToolCallInputScroll,
    ResponseToolCallInputScrollToBottom,
    ResponseToolCallInputExit,
    ResponseToolCallInputClick,
    ResponseToolCallInputHover,
    ResponseToolCallInputWait,
    ResponseToolCallInputError,
    ResponseToolCallInputGoogle,
    ResponseToolCallInputType,
]


class ResponseToolCallResultToolQueued(BaseModel):
    tool_queued: str = FieldInfo(alias="ToolQueued")


class ResponseToolCallResultToolFail(BaseModel):
    tool_fail: str = FieldInfo(alias="ToolFail")


class ResponseToolCallResultInputParseFail(BaseModel):
    input_parse_fail: str = FieldInfo(alias="InputParseFail")


class ResponseToolCallResultSuccess(BaseModel):
    success: str = FieldInfo(alias="Success")


ResponseToolCallResult: TypeAlias = Union[
    ResponseToolCallResultToolQueued,
    ResponseToolCallResultToolFail,
    ResponseToolCallResultInputParseFail,
    ResponseToolCallResultSuccess,
    None,
]


class ResponseToolCall(BaseModel):
    input: ResponseToolCallInput

    name: Literal["Exit", "Save", "Wait", "Type", "Scroll", "ScrollToBottom", "Click", "Hover", "Error", "Google"]

    result: Optional[ResponseToolCallResult] = None


class Response(BaseModel):
    llm: str

    text: str

    tool_calls: List[ResponseToolCall]

    reasoning: Optional[str] = None

    thinking: Optional[str] = None


class JobGetStepResponse(BaseModel):
    prompt: ChatPrompt

    response: Response
