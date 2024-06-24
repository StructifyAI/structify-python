# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._compat import PYDANTIC_V2
from .._models import BaseModel

__all__ = [
    "ExecutionStep",
    "Response",
    "ResponseToolCall",
    "ResponseToolCallInput",
    "ResponseToolCallInputSave",
    "ResponseToolCallInputSaveSave",
    "ResponseToolCallInputSaveSaveEntity",
    "ResponseToolCallInputSaveSaveRelationship",
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


class ResponseToolCallInputSaveSaveEntity(BaseModel):
    id: int

    properties: Dict[str, str]

    type: str


class ResponseToolCallInputSaveSaveRelationship(BaseModel):
    source: int

    target: int

    type: str


class ResponseToolCallInputSaveSave(BaseModel):
    entities: Optional[List[ResponseToolCallInputSaveSaveEntity]] = None

    relationships: Optional[List[ResponseToolCallInputSaveSaveRelationship]] = None


class ResponseToolCallInputSave(BaseModel):
    save: ResponseToolCallInputSaveSave = FieldInfo(alias="Save")
    """
    Knowledge graph info structured to deserialize and display in the same format
    that the LLM outputs.
    """


class ResponseToolCallInputScrollScroll(BaseModel):
    reason: str
    """OpenAI Requires an argument, so we put a dummy one here."""


class ResponseToolCallInputScroll(BaseModel):
    scroll: ResponseToolCallInputScrollScroll = FieldInfo(alias="Scroll")
    """For tools with no inputs."""


class ResponseToolCallInputExitExit(BaseModel):
    reason: str
    """OpenAI Requires an argument, so we put a dummy one here."""


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
    seconds: int
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


ResponseToolCallInput = Union[
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


class ResponseToolCallResultToolQueued(BaseModel):
    tool_queued: str = FieldInfo(alias="ToolQueued")


class ResponseToolCallResultToolFail(BaseModel):
    tool_fail: str = FieldInfo(alias="ToolFail")


class ResponseToolCallResultInputParseFail(BaseModel):
    input_parse_fail: str = FieldInfo(alias="InputParseFail")


class ResponseToolCallResultSuccess(BaseModel):
    success: str = FieldInfo(alias="Success")


ResponseToolCallResult = Union[
    ResponseToolCallResultToolQueued,
    ResponseToolCallResultToolFail,
    ResponseToolCallResultInputParseFail,
    ResponseToolCallResultSuccess,
    None,
]


class ResponseToolCall(BaseModel):
    input: ResponseToolCallInput

    name: Literal["Save", "Scroll", "Exit", "Click", "Hover", "Wait", "Error", "Google", "Type"]

    result: Optional[ResponseToolCallResult] = None


class Response(BaseModel):
    completion_tokens: int

    cost: float
    """Cost in dollars"""

    llm: str

    prompt_tokens: int
    """New tokens"""

    text: str

    tool_calls: List[ResponseToolCall]


class ExecutionStep(BaseModel):
    prompt: "ChatPrompt"

    response: Response


from .chat_prompt import ChatPrompt

if PYDANTIC_V2:
    ExecutionStep.model_rebuild()
    Response.model_rebuild()
    ResponseToolCall.model_rebuild()
    ResponseToolCallInputSave.model_rebuild()
    ResponseToolCallInputSaveSave.model_rebuild()
    ResponseToolCallInputSaveSaveEntity.model_rebuild()
    ResponseToolCallInputSaveSaveRelationship.model_rebuild()
    ResponseToolCallInputScroll.model_rebuild()
    ResponseToolCallInputScrollScroll.model_rebuild()
    ResponseToolCallInputExit.model_rebuild()
    ResponseToolCallInputExitExit.model_rebuild()
    ResponseToolCallInputClick.model_rebuild()
    ResponseToolCallInputClickClick.model_rebuild()
    ResponseToolCallInputHover.model_rebuild()
    ResponseToolCallInputHoverHover.model_rebuild()
    ResponseToolCallInputWait.model_rebuild()
    ResponseToolCallInputWaitWait.model_rebuild()
    ResponseToolCallInputError.model_rebuild()
    ResponseToolCallInputErrorError.model_rebuild()
    ResponseToolCallInputGoogle.model_rebuild()
    ResponseToolCallInputGoogleGoogle.model_rebuild()
    ResponseToolCallInputType.model_rebuild()
    ResponseToolCallInputTypeType.model_rebuild()
    ResponseToolCallResultToolQueued.model_rebuild()
    ResponseToolCallResultToolFail.model_rebuild()
    ResponseToolCallResultInputParseFail.model_rebuild()
    ResponseToolCallResultSuccess.model_rebuild()
else:
    ExecutionStep.update_forward_refs()  # type: ignore
    Response.update_forward_refs()  # type: ignore
    ResponseToolCall.update_forward_refs()  # type: ignore
    ResponseToolCallInputSave.update_forward_refs()  # type: ignore
    ResponseToolCallInputSaveSave.update_forward_refs()  # type: ignore
    ResponseToolCallInputSaveSaveEntity.update_forward_refs()  # type: ignore
    ResponseToolCallInputSaveSaveRelationship.update_forward_refs()  # type: ignore
    ResponseToolCallInputScroll.update_forward_refs()  # type: ignore
    ResponseToolCallInputScrollScroll.update_forward_refs()  # type: ignore
    ResponseToolCallInputExit.update_forward_refs()  # type: ignore
    ResponseToolCallInputExitExit.update_forward_refs()  # type: ignore
    ResponseToolCallInputClick.update_forward_refs()  # type: ignore
    ResponseToolCallInputClickClick.update_forward_refs()  # type: ignore
    ResponseToolCallInputHover.update_forward_refs()  # type: ignore
    ResponseToolCallInputHoverHover.update_forward_refs()  # type: ignore
    ResponseToolCallInputWait.update_forward_refs()  # type: ignore
    ResponseToolCallInputWaitWait.update_forward_refs()  # type: ignore
    ResponseToolCallInputError.update_forward_refs()  # type: ignore
    ResponseToolCallInputErrorError.update_forward_refs()  # type: ignore
    ResponseToolCallInputGoogle.update_forward_refs()  # type: ignore
    ResponseToolCallInputGoogleGoogle.update_forward_refs()  # type: ignore
    ResponseToolCallInputType.update_forward_refs()  # type: ignore
    ResponseToolCallInputTypeType.update_forward_refs()  # type: ignore
    ResponseToolCallResultToolQueued.update_forward_refs()  # type: ignore
    ResponseToolCallResultToolFail.update_forward_refs()  # type: ignore
    ResponseToolCallResultInputParseFail.update_forward_refs()  # type: ignore
    ResponseToolCallResultSuccess.update_forward_refs()  # type: ignore
