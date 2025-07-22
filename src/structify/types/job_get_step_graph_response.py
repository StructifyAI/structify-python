# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .chat_prompt import ChatPrompt
from .knowledge_graph import KnowledgeGraph

__all__ = [
    "JobGetStepGraphResponse",
    "JobGetStepGraphResponseItem",
    "JobGetStepGraphResponseItemExecutionStep",
    "JobGetStepGraphResponseItemExecutionStepResponse",
    "JobGetStepGraphResponseItemExecutionStepResponseToolCall",
    "JobGetStepGraphResponseItemExecutionStepResponseToolCallInput",
    "JobGetStepGraphResponseItemExecutionStepResponseToolCallInputSave",
    "JobGetStepGraphResponseItemExecutionStepResponseToolCallInputScroll",
    "JobGetStepGraphResponseItemExecutionStepResponseToolCallInputScrollScroll",
    "JobGetStepGraphResponseItemExecutionStepResponseToolCallInputScrollToBottom",
    "JobGetStepGraphResponseItemExecutionStepResponseToolCallInputScrollToBottomScrollToBottom",
    "JobGetStepGraphResponseItemExecutionStepResponseToolCallInputExit",
    "JobGetStepGraphResponseItemExecutionStepResponseToolCallInputExitExit",
    "JobGetStepGraphResponseItemExecutionStepResponseToolCallInputClick",
    "JobGetStepGraphResponseItemExecutionStepResponseToolCallInputClickClick",
    "JobGetStepGraphResponseItemExecutionStepResponseToolCallInputHover",
    "JobGetStepGraphResponseItemExecutionStepResponseToolCallInputHoverHover",
    "JobGetStepGraphResponseItemExecutionStepResponseToolCallInputWait",
    "JobGetStepGraphResponseItemExecutionStepResponseToolCallInputWaitWait",
    "JobGetStepGraphResponseItemExecutionStepResponseToolCallInputError",
    "JobGetStepGraphResponseItemExecutionStepResponseToolCallInputErrorError",
    "JobGetStepGraphResponseItemExecutionStepResponseToolCallInputGoogle",
    "JobGetStepGraphResponseItemExecutionStepResponseToolCallInputGoogleGoogle",
    "JobGetStepGraphResponseItemExecutionStepResponseToolCallInputType",
    "JobGetStepGraphResponseItemExecutionStepResponseToolCallInputTypeType",
    "JobGetStepGraphResponseItemExecutionStepResponseToolCallResult",
    "JobGetStepGraphResponseItemExecutionStepResponseToolCallResultToolQueued",
    "JobGetStepGraphResponseItemExecutionStepResponseToolCallResultToolFail",
    "JobGetStepGraphResponseItemExecutionStepResponseToolCallResultInputParseFail",
    "JobGetStepGraphResponseItemExecutionStepResponseToolCallResultSuccess",
    "JobGetStepGraphResponseItemParentTransition",
]


class JobGetStepGraphResponseItemExecutionStepResponseToolCallInputSave(BaseModel):
    save: KnowledgeGraph = FieldInfo(alias="Save")
    """
    Knowledge graph info structured to deserialize and display in the same format
    that the LLM outputs. Also the first representation of an LLM output in the
    pipeline from raw tool output to being merged into a DB
    """


class JobGetStepGraphResponseItemExecutionStepResponseToolCallInputScrollScroll(BaseModel):
    reason: str
    """Dummy argument"""


class JobGetStepGraphResponseItemExecutionStepResponseToolCallInputScroll(BaseModel):
    scroll: JobGetStepGraphResponseItemExecutionStepResponseToolCallInputScrollScroll = FieldInfo(alias="Scroll")
    """For tools with no inputs."""


class JobGetStepGraphResponseItemExecutionStepResponseToolCallInputScrollToBottomScrollToBottom(BaseModel):
    reason: str
    """Dummy argument"""


class JobGetStepGraphResponseItemExecutionStepResponseToolCallInputScrollToBottom(BaseModel):
    scroll_to_bottom: JobGetStepGraphResponseItemExecutionStepResponseToolCallInputScrollToBottomScrollToBottom = (
        FieldInfo(alias="ScrollToBottom")
    )
    """For tools with no inputs."""


class JobGetStepGraphResponseItemExecutionStepResponseToolCallInputExitExit(BaseModel):
    reason: str
    """Dummy argument"""


class JobGetStepGraphResponseItemExecutionStepResponseToolCallInputExit(BaseModel):
    exit: JobGetStepGraphResponseItemExecutionStepResponseToolCallInputExitExit = FieldInfo(alias="Exit")
    """For tools with no inputs."""


class JobGetStepGraphResponseItemExecutionStepResponseToolCallInputClickClick(BaseModel):
    flag: int


class JobGetStepGraphResponseItemExecutionStepResponseToolCallInputClick(BaseModel):
    click: JobGetStepGraphResponseItemExecutionStepResponseToolCallInputClickClick = FieldInfo(alias="Click")


class JobGetStepGraphResponseItemExecutionStepResponseToolCallInputHoverHover(BaseModel):
    flag: int


class JobGetStepGraphResponseItemExecutionStepResponseToolCallInputHover(BaseModel):
    hover: JobGetStepGraphResponseItemExecutionStepResponseToolCallInputHoverHover = FieldInfo(alias="Hover")


class JobGetStepGraphResponseItemExecutionStepResponseToolCallInputWaitWait(BaseModel):
    seconds: Optional[int] = None
    """Time in seconds to wait"""


class JobGetStepGraphResponseItemExecutionStepResponseToolCallInputWait(BaseModel):
    wait: JobGetStepGraphResponseItemExecutionStepResponseToolCallInputWaitWait = FieldInfo(alias="Wait")


class JobGetStepGraphResponseItemExecutionStepResponseToolCallInputErrorError(BaseModel):
    error: str


class JobGetStepGraphResponseItemExecutionStepResponseToolCallInputError(BaseModel):
    error: JobGetStepGraphResponseItemExecutionStepResponseToolCallInputErrorError = FieldInfo(alias="Error")


class JobGetStepGraphResponseItemExecutionStepResponseToolCallInputGoogleGoogle(BaseModel):
    query: str


class JobGetStepGraphResponseItemExecutionStepResponseToolCallInputGoogle(BaseModel):
    google: JobGetStepGraphResponseItemExecutionStepResponseToolCallInputGoogleGoogle = FieldInfo(alias="Google")


class JobGetStepGraphResponseItemExecutionStepResponseToolCallInputTypeType(BaseModel):
    flag: int

    input: str


class JobGetStepGraphResponseItemExecutionStepResponseToolCallInputType(BaseModel):
    type: JobGetStepGraphResponseItemExecutionStepResponseToolCallInputTypeType = FieldInfo(alias="Type")


JobGetStepGraphResponseItemExecutionStepResponseToolCallInput: TypeAlias = Union[
    JobGetStepGraphResponseItemExecutionStepResponseToolCallInputSave,
    JobGetStepGraphResponseItemExecutionStepResponseToolCallInputScroll,
    JobGetStepGraphResponseItemExecutionStepResponseToolCallInputScrollToBottom,
    JobGetStepGraphResponseItemExecutionStepResponseToolCallInputExit,
    JobGetStepGraphResponseItemExecutionStepResponseToolCallInputClick,
    JobGetStepGraphResponseItemExecutionStepResponseToolCallInputHover,
    JobGetStepGraphResponseItemExecutionStepResponseToolCallInputWait,
    JobGetStepGraphResponseItemExecutionStepResponseToolCallInputError,
    JobGetStepGraphResponseItemExecutionStepResponseToolCallInputGoogle,
    JobGetStepGraphResponseItemExecutionStepResponseToolCallInputType,
]


class JobGetStepGraphResponseItemExecutionStepResponseToolCallResultToolQueued(BaseModel):
    tool_queued: str = FieldInfo(alias="ToolQueued")


class JobGetStepGraphResponseItemExecutionStepResponseToolCallResultToolFail(BaseModel):
    tool_fail: str = FieldInfo(alias="ToolFail")


class JobGetStepGraphResponseItemExecutionStepResponseToolCallResultInputParseFail(BaseModel):
    input_parse_fail: str = FieldInfo(alias="InputParseFail")


class JobGetStepGraphResponseItemExecutionStepResponseToolCallResultSuccess(BaseModel):
    success: str = FieldInfo(alias="Success")


JobGetStepGraphResponseItemExecutionStepResponseToolCallResult: TypeAlias = Union[
    JobGetStepGraphResponseItemExecutionStepResponseToolCallResultToolQueued,
    JobGetStepGraphResponseItemExecutionStepResponseToolCallResultToolFail,
    JobGetStepGraphResponseItemExecutionStepResponseToolCallResultInputParseFail,
    JobGetStepGraphResponseItemExecutionStepResponseToolCallResultSuccess,
    None,
]


class JobGetStepGraphResponseItemExecutionStepResponseToolCall(BaseModel):
    input: JobGetStepGraphResponseItemExecutionStepResponseToolCallInput

    name: Literal["Exit", "Save", "Wait", "Type", "Scroll", "ScrollToBottom", "Click", "Hover", "Error", "Google"]

    result: Optional[JobGetStepGraphResponseItemExecutionStepResponseToolCallResult] = None


class JobGetStepGraphResponseItemExecutionStepResponse(BaseModel):
    llm: str

    text: str

    tool_calls: List[JobGetStepGraphResponseItemExecutionStepResponseToolCall]

    reasoning: Optional[str] = None

    thinking: Optional[str] = None


class JobGetStepGraphResponseItemExecutionStep(BaseModel):
    prompt: ChatPrompt

    response: JobGetStepGraphResponseItemExecutionStepResponse


class JobGetStepGraphResponseItemParentTransition(BaseModel):
    parent_id: str

    tool_input: str

    tool_name: str


class JobGetStepGraphResponseItem(BaseModel):
    id: str

    creation_time: datetime

    status: Literal["queued", "started", "executed", "skipped"]

    execution_step: Optional[JobGetStepGraphResponseItemExecutionStep] = None

    parent_transition: Optional[JobGetStepGraphResponseItemParentTransition] = None

    queued_message: Optional[str] = None

    skipped_reason: Optional[str] = None

    state_change_message: Optional[str] = None

    step_index: Optional[int] = None


JobGetStepGraphResponse: TypeAlias = List[JobGetStepGraphResponseItem]
