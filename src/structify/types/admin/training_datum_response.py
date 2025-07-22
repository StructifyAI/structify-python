# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from ..chat_prompt import ChatPrompt
from .datum_status import DatumStatus
from ..knowledge_graph import KnowledgeGraph

__all__ = [
    "TrainingDatumResponse",
    "Step",
    "StepResponse",
    "StepResponseToolCall",
    "StepResponseToolCallInput",
    "StepResponseToolCallInputSave",
    "StepResponseToolCallInputScroll",
    "StepResponseToolCallInputScrollScroll",
    "StepResponseToolCallInputScrollToBottom",
    "StepResponseToolCallInputScrollToBottomScrollToBottom",
    "StepResponseToolCallInputExit",
    "StepResponseToolCallInputExitExit",
    "StepResponseToolCallInputClick",
    "StepResponseToolCallInputClickClick",
    "StepResponseToolCallInputHover",
    "StepResponseToolCallInputHoverHover",
    "StepResponseToolCallInputWait",
    "StepResponseToolCallInputWaitWait",
    "StepResponseToolCallInputError",
    "StepResponseToolCallInputErrorError",
    "StepResponseToolCallInputGoogle",
    "StepResponseToolCallInputGoogleGoogle",
    "StepResponseToolCallInputType",
    "StepResponseToolCallInputTypeType",
    "StepResponseToolCallResult",
    "StepResponseToolCallResultToolQueued",
    "StepResponseToolCallResultToolFail",
    "StepResponseToolCallResultInputParseFail",
    "StepResponseToolCallResultSuccess",
    "Update",
    "UpdateResponse",
    "UpdateResponseToolCall",
    "UpdateResponseToolCallInput",
    "UpdateResponseToolCallInputSave",
    "UpdateResponseToolCallInputScroll",
    "UpdateResponseToolCallInputScrollScroll",
    "UpdateResponseToolCallInputScrollToBottom",
    "UpdateResponseToolCallInputScrollToBottomScrollToBottom",
    "UpdateResponseToolCallInputExit",
    "UpdateResponseToolCallInputExitExit",
    "UpdateResponseToolCallInputClick",
    "UpdateResponseToolCallInputClickClick",
    "UpdateResponseToolCallInputHover",
    "UpdateResponseToolCallInputHoverHover",
    "UpdateResponseToolCallInputWait",
    "UpdateResponseToolCallInputWaitWait",
    "UpdateResponseToolCallInputError",
    "UpdateResponseToolCallInputErrorError",
    "UpdateResponseToolCallInputGoogle",
    "UpdateResponseToolCallInputGoogleGoogle",
    "UpdateResponseToolCallInputType",
    "UpdateResponseToolCallInputTypeType",
    "UpdateResponseToolCallResult",
    "UpdateResponseToolCallResultToolQueued",
    "UpdateResponseToolCallResultToolFail",
    "UpdateResponseToolCallResultInputParseFail",
    "UpdateResponseToolCallResultSuccess",
]


class StepResponseToolCallInputSave(BaseModel):
    save: KnowledgeGraph = FieldInfo(alias="Save")
    """
    Knowledge graph info structured to deserialize and display in the same format
    that the LLM outputs. Also the first representation of an LLM output in the
    pipeline from raw tool output to being merged into a DB
    """


class StepResponseToolCallInputScrollScroll(BaseModel):
    reason: str
    """Dummy argument"""


class StepResponseToolCallInputScroll(BaseModel):
    scroll: StepResponseToolCallInputScrollScroll = FieldInfo(alias="Scroll")
    """For tools with no inputs."""


class StepResponseToolCallInputScrollToBottomScrollToBottom(BaseModel):
    reason: str
    """Dummy argument"""


class StepResponseToolCallInputScrollToBottom(BaseModel):
    scroll_to_bottom: StepResponseToolCallInputScrollToBottomScrollToBottom = FieldInfo(alias="ScrollToBottom")
    """For tools with no inputs."""


class StepResponseToolCallInputExitExit(BaseModel):
    reason: str
    """Dummy argument"""


class StepResponseToolCallInputExit(BaseModel):
    exit: StepResponseToolCallInputExitExit = FieldInfo(alias="Exit")
    """For tools with no inputs."""


class StepResponseToolCallInputClickClick(BaseModel):
    flag: int


class StepResponseToolCallInputClick(BaseModel):
    click: StepResponseToolCallInputClickClick = FieldInfo(alias="Click")


class StepResponseToolCallInputHoverHover(BaseModel):
    flag: int


class StepResponseToolCallInputHover(BaseModel):
    hover: StepResponseToolCallInputHoverHover = FieldInfo(alias="Hover")


class StepResponseToolCallInputWaitWait(BaseModel):
    seconds: Optional[int] = None
    """Time in seconds to wait"""


class StepResponseToolCallInputWait(BaseModel):
    wait: StepResponseToolCallInputWaitWait = FieldInfo(alias="Wait")


class StepResponseToolCallInputErrorError(BaseModel):
    error: str


class StepResponseToolCallInputError(BaseModel):
    error: StepResponseToolCallInputErrorError = FieldInfo(alias="Error")


class StepResponseToolCallInputGoogleGoogle(BaseModel):
    query: str


class StepResponseToolCallInputGoogle(BaseModel):
    google: StepResponseToolCallInputGoogleGoogle = FieldInfo(alias="Google")


class StepResponseToolCallInputTypeType(BaseModel):
    flag: int

    input: str


class StepResponseToolCallInputType(BaseModel):
    type: StepResponseToolCallInputTypeType = FieldInfo(alias="Type")


StepResponseToolCallInput: TypeAlias = Union[
    StepResponseToolCallInputSave,
    StepResponseToolCallInputScroll,
    StepResponseToolCallInputScrollToBottom,
    StepResponseToolCallInputExit,
    StepResponseToolCallInputClick,
    StepResponseToolCallInputHover,
    StepResponseToolCallInputWait,
    StepResponseToolCallInputError,
    StepResponseToolCallInputGoogle,
    StepResponseToolCallInputType,
]


class StepResponseToolCallResultToolQueued(BaseModel):
    tool_queued: str = FieldInfo(alias="ToolQueued")


class StepResponseToolCallResultToolFail(BaseModel):
    tool_fail: str = FieldInfo(alias="ToolFail")


class StepResponseToolCallResultInputParseFail(BaseModel):
    input_parse_fail: str = FieldInfo(alias="InputParseFail")


class StepResponseToolCallResultSuccess(BaseModel):
    success: str = FieldInfo(alias="Success")


StepResponseToolCallResult: TypeAlias = Union[
    StepResponseToolCallResultToolQueued,
    StepResponseToolCallResultToolFail,
    StepResponseToolCallResultInputParseFail,
    StepResponseToolCallResultSuccess,
    None,
]


class StepResponseToolCall(BaseModel):
    input: StepResponseToolCallInput

    name: Literal["Exit", "Save", "Wait", "Type", "Scroll", "ScrollToBottom", "Click", "Hover", "Error", "Google"]

    result: Optional[StepResponseToolCallResult] = None


class StepResponse(BaseModel):
    llm: str

    text: str

    tool_calls: List[StepResponseToolCall]

    reasoning: Optional[str] = None

    thinking: Optional[str] = None


class Step(BaseModel):
    prompt: ChatPrompt

    response: StepResponse


class UpdateResponseToolCallInputSave(BaseModel):
    save: KnowledgeGraph = FieldInfo(alias="Save")
    """
    Knowledge graph info structured to deserialize and display in the same format
    that the LLM outputs. Also the first representation of an LLM output in the
    pipeline from raw tool output to being merged into a DB
    """


class UpdateResponseToolCallInputScrollScroll(BaseModel):
    reason: str
    """Dummy argument"""


class UpdateResponseToolCallInputScroll(BaseModel):
    scroll: UpdateResponseToolCallInputScrollScroll = FieldInfo(alias="Scroll")
    """For tools with no inputs."""


class UpdateResponseToolCallInputScrollToBottomScrollToBottom(BaseModel):
    reason: str
    """Dummy argument"""


class UpdateResponseToolCallInputScrollToBottom(BaseModel):
    scroll_to_bottom: UpdateResponseToolCallInputScrollToBottomScrollToBottom = FieldInfo(alias="ScrollToBottom")
    """For tools with no inputs."""


class UpdateResponseToolCallInputExitExit(BaseModel):
    reason: str
    """Dummy argument"""


class UpdateResponseToolCallInputExit(BaseModel):
    exit: UpdateResponseToolCallInputExitExit = FieldInfo(alias="Exit")
    """For tools with no inputs."""


class UpdateResponseToolCallInputClickClick(BaseModel):
    flag: int


class UpdateResponseToolCallInputClick(BaseModel):
    click: UpdateResponseToolCallInputClickClick = FieldInfo(alias="Click")


class UpdateResponseToolCallInputHoverHover(BaseModel):
    flag: int


class UpdateResponseToolCallInputHover(BaseModel):
    hover: UpdateResponseToolCallInputHoverHover = FieldInfo(alias="Hover")


class UpdateResponseToolCallInputWaitWait(BaseModel):
    seconds: Optional[int] = None
    """Time in seconds to wait"""


class UpdateResponseToolCallInputWait(BaseModel):
    wait: UpdateResponseToolCallInputWaitWait = FieldInfo(alias="Wait")


class UpdateResponseToolCallInputErrorError(BaseModel):
    error: str


class UpdateResponseToolCallInputError(BaseModel):
    error: UpdateResponseToolCallInputErrorError = FieldInfo(alias="Error")


class UpdateResponseToolCallInputGoogleGoogle(BaseModel):
    query: str


class UpdateResponseToolCallInputGoogle(BaseModel):
    google: UpdateResponseToolCallInputGoogleGoogle = FieldInfo(alias="Google")


class UpdateResponseToolCallInputTypeType(BaseModel):
    flag: int

    input: str


class UpdateResponseToolCallInputType(BaseModel):
    type: UpdateResponseToolCallInputTypeType = FieldInfo(alias="Type")


UpdateResponseToolCallInput: TypeAlias = Union[
    UpdateResponseToolCallInputSave,
    UpdateResponseToolCallInputScroll,
    UpdateResponseToolCallInputScrollToBottom,
    UpdateResponseToolCallInputExit,
    UpdateResponseToolCallInputClick,
    UpdateResponseToolCallInputHover,
    UpdateResponseToolCallInputWait,
    UpdateResponseToolCallInputError,
    UpdateResponseToolCallInputGoogle,
    UpdateResponseToolCallInputType,
]


class UpdateResponseToolCallResultToolQueued(BaseModel):
    tool_queued: str = FieldInfo(alias="ToolQueued")


class UpdateResponseToolCallResultToolFail(BaseModel):
    tool_fail: str = FieldInfo(alias="ToolFail")


class UpdateResponseToolCallResultInputParseFail(BaseModel):
    input_parse_fail: str = FieldInfo(alias="InputParseFail")


class UpdateResponseToolCallResultSuccess(BaseModel):
    success: str = FieldInfo(alias="Success")


UpdateResponseToolCallResult: TypeAlias = Union[
    UpdateResponseToolCallResultToolQueued,
    UpdateResponseToolCallResultToolFail,
    UpdateResponseToolCallResultInputParseFail,
    UpdateResponseToolCallResultSuccess,
    None,
]


class UpdateResponseToolCall(BaseModel):
    input: UpdateResponseToolCallInput

    name: Literal["Exit", "Save", "Wait", "Type", "Scroll", "ScrollToBottom", "Click", "Hover", "Error", "Google"]

    result: Optional[UpdateResponseToolCallResult] = None


class UpdateResponse(BaseModel):
    llm: str

    text: str

    tool_calls: List[UpdateResponseToolCall]

    reasoning: Optional[str] = None

    thinking: Optional[str] = None


class Update(BaseModel):
    id: str

    author: str

    status: DatumStatus

    timestamp: datetime

    response: Optional[UpdateResponse] = None

    review_message: Optional[str] = None

    to_id: Optional[str] = None


class TrainingDatumResponse(BaseModel):
    id: str

    last_updated: datetime

    status: DatumStatus

    step: Step

    updates: List[Update]
    """All updates for the datum, sorted by ascending timestamp."""
