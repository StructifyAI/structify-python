# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from ..execution_step import ExecutionStep
from ..knowledge_graph import KnowledgeGraph

__all__ = [
    "TrainingDatumResponse",
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


class UpdateResponseToolCallInputSave(BaseModel):
    save: KnowledgeGraph = FieldInfo(alias="Save")
    """
    Knowledge graph info structured to deserialize and display in the same format
    that the LLM outputs. Also the first representation of an LLM output in the
    pipeline from raw tool output to being merged into a Neo4j DB
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


class Update(BaseModel):
    id: str

    author: str

    status: Literal[
        "Unlabeled", "NavLabeled", "SaveLabeled", "Verified", "Pending", "Skipped", "SuspiciousNav", "SuspiciousSave"
    ]

    timestamp: datetime

    response: Optional[UpdateResponse] = None

    review_message: Optional[str] = None

    verified_update_id: Optional[str] = None


class TrainingDatumResponse(BaseModel):
    id: str

    last_updated: datetime

    status: Literal[
        "Unlabeled", "NavLabeled", "SaveLabeled", "Verified", "Pending", "Skipped", "SuspiciousNav", "SuspiciousSave"
    ]

    step: ExecutionStep

    updates: List[Update]
