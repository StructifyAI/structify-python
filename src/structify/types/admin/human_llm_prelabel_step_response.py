# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from ..knowledge_graph import KnowledgeGraph

__all__ = [
    "HumanLlmPrelabelStepResponse",
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


class ToolCallInputSave(BaseModel):
    save: KnowledgeGraph = FieldInfo(alias="Save")
    """
    Knowledge graph info structured to deserialize and display in the same format
    that the LLM outputs. Also the first representation of an LLM output in the
    pipeline from raw tool output to being merged into a DB
    """


class ToolCallInputScrollScroll(BaseModel):
    reason: str
    """Dummy argument"""


class ToolCallInputScroll(BaseModel):
    scroll: ToolCallInputScrollScroll = FieldInfo(alias="Scroll")
    """For tools with no inputs."""


class ToolCallInputScrollToBottomScrollToBottom(BaseModel):
    reason: str
    """Dummy argument"""


class ToolCallInputScrollToBottom(BaseModel):
    scroll_to_bottom: ToolCallInputScrollToBottomScrollToBottom = FieldInfo(alias="ScrollToBottom")
    """For tools with no inputs."""


class ToolCallInputExitExit(BaseModel):
    reason: str
    """Dummy argument"""


class ToolCallInputExit(BaseModel):
    exit: ToolCallInputExitExit = FieldInfo(alias="Exit")
    """For tools with no inputs."""


class ToolCallInputClickClick(BaseModel):
    flag: int


class ToolCallInputClick(BaseModel):
    click: ToolCallInputClickClick = FieldInfo(alias="Click")


class ToolCallInputHoverHover(BaseModel):
    flag: int


class ToolCallInputHover(BaseModel):
    hover: ToolCallInputHoverHover = FieldInfo(alias="Hover")


class ToolCallInputWaitWait(BaseModel):
    seconds: Optional[int] = None
    """Time in seconds to wait"""


class ToolCallInputWait(BaseModel):
    wait: ToolCallInputWaitWait = FieldInfo(alias="Wait")


class ToolCallInputErrorError(BaseModel):
    error: str


class ToolCallInputError(BaseModel):
    error: ToolCallInputErrorError = FieldInfo(alias="Error")


class ToolCallInputGoogleGoogle(BaseModel):
    query: str


class ToolCallInputGoogle(BaseModel):
    google: ToolCallInputGoogleGoogle = FieldInfo(alias="Google")


class ToolCallInputTypeType(BaseModel):
    flag: int

    input: str


class ToolCallInputType(BaseModel):
    type: ToolCallInputTypeType = FieldInfo(alias="Type")


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


class ToolCallResultToolQueued(BaseModel):
    tool_queued: str = FieldInfo(alias="ToolQueued")


class ToolCallResultToolFail(BaseModel):
    tool_fail: str = FieldInfo(alias="ToolFail")


class ToolCallResultInputParseFail(BaseModel):
    input_parse_fail: str = FieldInfo(alias="InputParseFail")


class ToolCallResultSuccess(BaseModel):
    success: str = FieldInfo(alias="Success")


ToolCallResult: TypeAlias = Union[
    ToolCallResultToolQueued, ToolCallResultToolFail, ToolCallResultInputParseFail, ToolCallResultSuccess, None
]


class ToolCall(BaseModel):
    input: ToolCallInput

    name: Literal["Exit", "Save", "Wait", "Type", "Scroll", "ScrollToBottom", "Click", "Hover", "Error", "Google"]

    result: Optional[ToolCallResult] = None


class HumanLlmPrelabelStepResponse(BaseModel):
    llm: str

    text: str

    tool_calls: List[ToolCall]

    reasoning: Optional[str] = None

    thinking: Optional[str] = None
