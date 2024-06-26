# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .dataset_descriptor import DatasetDescriptor

__all__ = [
    "LabelGetMessagesResponse",
    "Chat",
    "ChatDecodingParams",
    "ChatDecodingParamsParameter",
    "ChatDecodingParamsParameterMaxTokens",
    "ChatDecodingParamsParameterTopP",
    "ChatDecodingParamsParameterRepeatWindow",
    "ChatDecodingParamsParameterRepeatPenalty",
    "ChatDecodingParamsParameterTemperature",
    "ChatDecodingParamsParameterStopTokens",
    "ChatDecodingParamsParameterFunctions",
    "ChatDecodingParamsParameterJsonValidator",
    "ChatDecodingParamsParameterRegexValidator",
    "ChatDecodingParamsParameterContextFreeeGrammar",
    "ChatDecodingParamsParameterCrop",
    "ChatMessage",
    "ChatMessageContent",
    "ChatMessageContentText",
    "ChatMessageContentImage",
    "ChatHumanLlmMetadata",
    "ChatHumanLlmMetadataHistory",
    "ChatHumanLlmMetadataHistoryStep",
    "ChatHumanLlmMetadataHistoryStepPrompt",
    "ChatHumanLlmMetadataHistoryStepPromptDecodingParams",
    "ChatHumanLlmMetadataHistoryStepPromptDecodingParamsParameter",
    "ChatHumanLlmMetadataHistoryStepPromptDecodingParamsParameterMaxTokens",
    "ChatHumanLlmMetadataHistoryStepPromptDecodingParamsParameterTopP",
    "ChatHumanLlmMetadataHistoryStepPromptDecodingParamsParameterRepeatWindow",
    "ChatHumanLlmMetadataHistoryStepPromptDecodingParamsParameterRepeatPenalty",
    "ChatHumanLlmMetadataHistoryStepPromptDecodingParamsParameterTemperature",
    "ChatHumanLlmMetadataHistoryStepPromptDecodingParamsParameterStopTokens",
    "ChatHumanLlmMetadataHistoryStepPromptDecodingParamsParameterFunctions",
    "ChatHumanLlmMetadataHistoryStepPromptDecodingParamsParameterJsonValidator",
    "ChatHumanLlmMetadataHistoryStepPromptDecodingParamsParameterRegexValidator",
    "ChatHumanLlmMetadataHistoryStepPromptDecodingParamsParameterContextFreeeGrammar",
    "ChatHumanLlmMetadataHistoryStepPromptDecodingParamsParameterCrop",
    "ChatHumanLlmMetadataHistoryStepPromptMessage",
    "ChatHumanLlmMetadataHistoryStepPromptMessageContent",
    "ChatHumanLlmMetadataHistoryStepPromptMessageContentText",
    "ChatHumanLlmMetadataHistoryStepPromptMessageContentImage",
    "ChatHumanLlmMetadataHistoryStepPromptHumanLlmMetadata",
    "ChatHumanLlmMetadataHistoryStepPromptHumanLlmMetadataHistory",
    "ChatHumanLlmMetadataHistoryStepPromptMetadata",
    "ChatHumanLlmMetadataHistoryStepPromptMetadataExtractedEntity",
    "ChatHumanLlmMetadataHistoryStepPromptMetadataExtractedEntityEntity",
    "ChatHumanLlmMetadataHistoryStepPromptMetadataExtractedEntityRelationship",
    "ChatHumanLlmMetadataHistoryStepPromptMetadataToolMetadata",
    "ChatHumanLlmMetadataHistoryStepPromptMetadataWebFlag",
    "ChatHumanLlmMetadataHistoryStepResponse",
    "ChatHumanLlmMetadataHistoryStepResponseToolCall",
    "ChatHumanLlmMetadataHistoryStepResponseToolCallInput",
    "ChatHumanLlmMetadataHistoryStepResponseToolCallInputSave",
    "ChatHumanLlmMetadataHistoryStepResponseToolCallInputSaveSave",
    "ChatHumanLlmMetadataHistoryStepResponseToolCallInputSaveSaveEntity",
    "ChatHumanLlmMetadataHistoryStepResponseToolCallInputSaveSaveRelationship",
    "ChatHumanLlmMetadataHistoryStepResponseToolCallInputScroll",
    "ChatHumanLlmMetadataHistoryStepResponseToolCallInputScrollScroll",
    "ChatHumanLlmMetadataHistoryStepResponseToolCallInputExit",
    "ChatHumanLlmMetadataHistoryStepResponseToolCallInputExitExit",
    "ChatHumanLlmMetadataHistoryStepResponseToolCallInputClick",
    "ChatHumanLlmMetadataHistoryStepResponseToolCallInputClickClick",
    "ChatHumanLlmMetadataHistoryStepResponseToolCallInputHover",
    "ChatHumanLlmMetadataHistoryStepResponseToolCallInputHoverHover",
    "ChatHumanLlmMetadataHistoryStepResponseToolCallInputWait",
    "ChatHumanLlmMetadataHistoryStepResponseToolCallInputWaitWait",
    "ChatHumanLlmMetadataHistoryStepResponseToolCallInputError",
    "ChatHumanLlmMetadataHistoryStepResponseToolCallInputErrorError",
    "ChatHumanLlmMetadataHistoryStepResponseToolCallInputGoogle",
    "ChatHumanLlmMetadataHistoryStepResponseToolCallInputGoogleGoogle",
    "ChatHumanLlmMetadataHistoryStepResponseToolCallInputType",
    "ChatHumanLlmMetadataHistoryStepResponseToolCallInputTypeType",
    "ChatHumanLlmMetadataHistoryStepResponseToolCallResult",
    "ChatHumanLlmMetadataHistoryStepResponseToolCallResultToolQueued",
    "ChatHumanLlmMetadataHistoryStepResponseToolCallResultToolFail",
    "ChatHumanLlmMetadataHistoryStepResponseToolCallResultInputParseFail",
    "ChatHumanLlmMetadataHistoryStepResponseToolCallResultSuccess",
    "ChatMetadata",
    "ChatMetadataExtractedEntity",
    "ChatMetadataExtractedEntityEntity",
    "ChatMetadataExtractedEntityRelationship",
    "ChatMetadataToolMetadata",
    "ChatMetadataWebFlag",
]


class ChatDecodingParamsParameterMaxTokens(BaseModel):
    max_tokens: int = FieldInfo(alias="MaxTokens")


class ChatDecodingParamsParameterTopP(BaseModel):
    top_p: float = FieldInfo(alias="TopP")


class ChatDecodingParamsParameterRepeatWindow(BaseModel):
    repeat_window: int = FieldInfo(alias="RepeatWindow")


class ChatDecodingParamsParameterRepeatPenalty(BaseModel):
    repeat_penalty: float = FieldInfo(alias="RepeatPenalty")


class ChatDecodingParamsParameterTemperature(BaseModel):
    temperature: float = FieldInfo(alias="Temperature")


class ChatDecodingParamsParameterStopTokens(BaseModel):
    stop_tokens: List[str] = FieldInfo(alias="StopTokens")


class ChatDecodingParamsParameterFunctions(BaseModel):
    functions: List[object] = FieldInfo(alias="Functions")


class ChatDecodingParamsParameterJsonValidator(BaseModel):
    json_validator: object = FieldInfo(alias="JsonValidator")


class ChatDecodingParamsParameterRegexValidator(BaseModel):
    regex_validator: str = FieldInfo(alias="RegexValidator")


class ChatDecodingParamsParameterContextFreeeGrammar(BaseModel):
    context_freee_grammar: str = FieldInfo(alias="ContextFreeeGrammar")


class ChatDecodingParamsParameterCrop(BaseModel):
    crop: bool = FieldInfo(alias="Crop")


ChatDecodingParamsParameter = Union[
    ChatDecodingParamsParameterMaxTokens,
    ChatDecodingParamsParameterTopP,
    ChatDecodingParamsParameterRepeatWindow,
    ChatDecodingParamsParameterRepeatPenalty,
    ChatDecodingParamsParameterTemperature,
    ChatDecodingParamsParameterStopTokens,
    ChatDecodingParamsParameterFunctions,
    ChatDecodingParamsParameterJsonValidator,
    ChatDecodingParamsParameterRegexValidator,
    ChatDecodingParamsParameterContextFreeeGrammar,
    ChatDecodingParamsParameterCrop,
]


class ChatDecodingParams(BaseModel):
    parameters: List[ChatDecodingParamsParameter]


class ChatMessageContentText(BaseModel):
    text: str = FieldInfo(alias="Text")


class ChatMessageContentImage(BaseModel):
    image: object = FieldInfo(alias="Image")


ChatMessageContent = Union[ChatMessageContentText, ChatMessageContentImage]


class ChatMessage(BaseModel):
    content: List[ChatMessageContent]
    """
    We want this to be a vec of contents so we can accurately capture an
    interleaving of images and text.

    This is meant to be a completely raw, unprocessed representation of the text.
    Don't take stuff out.
    """

    role: Literal["user", "system", "assistant"]


class ChatHumanLlmMetadataHistoryStepPromptDecodingParamsParameterMaxTokens(BaseModel):
    max_tokens: int = FieldInfo(alias="MaxTokens")


class ChatHumanLlmMetadataHistoryStepPromptDecodingParamsParameterTopP(BaseModel):
    top_p: float = FieldInfo(alias="TopP")


class ChatHumanLlmMetadataHistoryStepPromptDecodingParamsParameterRepeatWindow(BaseModel):
    repeat_window: int = FieldInfo(alias="RepeatWindow")


class ChatHumanLlmMetadataHistoryStepPromptDecodingParamsParameterRepeatPenalty(BaseModel):
    repeat_penalty: float = FieldInfo(alias="RepeatPenalty")


class ChatHumanLlmMetadataHistoryStepPromptDecodingParamsParameterTemperature(BaseModel):
    temperature: float = FieldInfo(alias="Temperature")


class ChatHumanLlmMetadataHistoryStepPromptDecodingParamsParameterStopTokens(BaseModel):
    stop_tokens: List[str] = FieldInfo(alias="StopTokens")


class ChatHumanLlmMetadataHistoryStepPromptDecodingParamsParameterFunctions(BaseModel):
    functions: List[object] = FieldInfo(alias="Functions")


class ChatHumanLlmMetadataHistoryStepPromptDecodingParamsParameterJsonValidator(BaseModel):
    json_validator: object = FieldInfo(alias="JsonValidator")


class ChatHumanLlmMetadataHistoryStepPromptDecodingParamsParameterRegexValidator(BaseModel):
    regex_validator: str = FieldInfo(alias="RegexValidator")


class ChatHumanLlmMetadataHistoryStepPromptDecodingParamsParameterContextFreeeGrammar(BaseModel):
    context_freee_grammar: str = FieldInfo(alias="ContextFreeeGrammar")


class ChatHumanLlmMetadataHistoryStepPromptDecodingParamsParameterCrop(BaseModel):
    crop: bool = FieldInfo(alias="Crop")


ChatHumanLlmMetadataHistoryStepPromptDecodingParamsParameter = Union[
    ChatHumanLlmMetadataHistoryStepPromptDecodingParamsParameterMaxTokens,
    ChatHumanLlmMetadataHistoryStepPromptDecodingParamsParameterTopP,
    ChatHumanLlmMetadataHistoryStepPromptDecodingParamsParameterRepeatWindow,
    ChatHumanLlmMetadataHistoryStepPromptDecodingParamsParameterRepeatPenalty,
    ChatHumanLlmMetadataHistoryStepPromptDecodingParamsParameterTemperature,
    ChatHumanLlmMetadataHistoryStepPromptDecodingParamsParameterStopTokens,
    ChatHumanLlmMetadataHistoryStepPromptDecodingParamsParameterFunctions,
    ChatHumanLlmMetadataHistoryStepPromptDecodingParamsParameterJsonValidator,
    ChatHumanLlmMetadataHistoryStepPromptDecodingParamsParameterRegexValidator,
    ChatHumanLlmMetadataHistoryStepPromptDecodingParamsParameterContextFreeeGrammar,
    ChatHumanLlmMetadataHistoryStepPromptDecodingParamsParameterCrop,
]


class ChatHumanLlmMetadataHistoryStepPromptDecodingParams(BaseModel):
    parameters: List[ChatHumanLlmMetadataHistoryStepPromptDecodingParamsParameter]


class ChatHumanLlmMetadataHistoryStepPromptMessageContentText(BaseModel):
    text: str = FieldInfo(alias="Text")


class ChatHumanLlmMetadataHistoryStepPromptMessageContentImage(BaseModel):
    image: object = FieldInfo(alias="Image")


ChatHumanLlmMetadataHistoryStepPromptMessageContent = Union[
    ChatHumanLlmMetadataHistoryStepPromptMessageContentText, ChatHumanLlmMetadataHistoryStepPromptMessageContentImage
]


class ChatHumanLlmMetadataHistoryStepPromptMessage(BaseModel):
    content: List[ChatHumanLlmMetadataHistoryStepPromptMessageContent]
    """
    We want this to be a vec of contents so we can accurately capture an
    interleaving of images and text.

    This is meant to be a completely raw, unprocessed representation of the text.
    Don't take stuff out.
    """

    role: Literal["user", "system", "assistant"]


class ChatHumanLlmMetadataHistoryStepPromptHumanLlmMetadataHistory(BaseModel):
    date: datetime

    steps: List[object]

    uuid: str
    """Used to identify this history"""


class ChatHumanLlmMetadataHistoryStepPromptHumanLlmMetadata(BaseModel):
    descriptor: DatasetDescriptor
    """A dataset is where you put multiple referential schemas.

    A dataset is a complete namespace where all references between schemas are held
    within the dataset.
    """

    run_id: str

    user_email: str

    history: Optional[ChatHumanLlmMetadataHistoryStepPromptHumanLlmMetadataHistory] = None


class ChatHumanLlmMetadataHistoryStepPromptMetadataExtractedEntityEntity(BaseModel):
    id: int

    properties: Dict[str, str]

    type: str


class ChatHumanLlmMetadataHistoryStepPromptMetadataExtractedEntityRelationship(BaseModel):
    source: int

    target: int

    type: str


class ChatHumanLlmMetadataHistoryStepPromptMetadataExtractedEntity(BaseModel):
    entities: Optional[List[ChatHumanLlmMetadataHistoryStepPromptMetadataExtractedEntityEntity]] = None

    relationships: Optional[List[ChatHumanLlmMetadataHistoryStepPromptMetadataExtractedEntityRelationship]] = None


class ChatHumanLlmMetadataHistoryStepPromptMetadataToolMetadata(BaseModel):
    description: str

    name: Literal["Save", "Scroll", "Exit", "Click", "Hover", "Wait", "Error", "Google", "Type"]

    regex_validator: str

    tool_validator: object


class ChatHumanLlmMetadataHistoryStepPromptMetadataWebFlag(BaseModel):
    aria_label: str = FieldInfo(alias="ariaLabel")

    height: float

    text: str

    type: str

    width: float

    x: float

    y: float


class ChatHumanLlmMetadataHistoryStepPromptMetadata(BaseModel):
    conditioning_prompt: str

    dataset_descriptor: DatasetDescriptor
    """A dataset is where you put multiple referential schemas.

    A dataset is a complete namespace where all references between schemas are held
    within the dataset.
    """

    extracted_entities: List[ChatHumanLlmMetadataHistoryStepPromptMetadataExtractedEntity]

    tool_metadata: List[ChatHumanLlmMetadataHistoryStepPromptMetadataToolMetadata]

    screenshot: Optional[object] = None

    url: Optional[str] = None

    web_flags: Optional[List[ChatHumanLlmMetadataHistoryStepPromptMetadataWebFlag]] = None


class ChatHumanLlmMetadataHistoryStepPrompt(BaseModel):
    decoding_params: ChatHumanLlmMetadataHistoryStepPromptDecodingParams

    messages: List[ChatHumanLlmMetadataHistoryStepPromptMessage]

    human_llm_metadata: Optional[ChatHumanLlmMetadataHistoryStepPromptHumanLlmMetadata] = None

    metadata: Optional[ChatHumanLlmMetadataHistoryStepPromptMetadata] = None


class ChatHumanLlmMetadataHistoryStepResponseToolCallInputSaveSaveEntity(BaseModel):
    id: int

    properties: Dict[str, str]

    type: str


class ChatHumanLlmMetadataHistoryStepResponseToolCallInputSaveSaveRelationship(BaseModel):
    source: int

    target: int

    type: str


class ChatHumanLlmMetadataHistoryStepResponseToolCallInputSaveSave(BaseModel):
    entities: Optional[List[ChatHumanLlmMetadataHistoryStepResponseToolCallInputSaveSaveEntity]] = None

    relationships: Optional[List[ChatHumanLlmMetadataHistoryStepResponseToolCallInputSaveSaveRelationship]] = None


class ChatHumanLlmMetadataHistoryStepResponseToolCallInputSave(BaseModel):
    save: ChatHumanLlmMetadataHistoryStepResponseToolCallInputSaveSave = FieldInfo(alias="Save")
    """
    Knowledge graph info structured to deserialize and display in the same format
    that the LLM outputs.
    """


class ChatHumanLlmMetadataHistoryStepResponseToolCallInputScrollScroll(BaseModel):
    reason: str
    """OpenAI Requires an argument, so we put a dummy one here."""


class ChatHumanLlmMetadataHistoryStepResponseToolCallInputScroll(BaseModel):
    scroll: ChatHumanLlmMetadataHistoryStepResponseToolCallInputScrollScroll = FieldInfo(alias="Scroll")
    """For tools with no inputs."""


class ChatHumanLlmMetadataHistoryStepResponseToolCallInputExitExit(BaseModel):
    reason: str
    """OpenAI Requires an argument, so we put a dummy one here."""


class ChatHumanLlmMetadataHistoryStepResponseToolCallInputExit(BaseModel):
    exit: ChatHumanLlmMetadataHistoryStepResponseToolCallInputExitExit = FieldInfo(alias="Exit")
    """For tools with no inputs."""


class ChatHumanLlmMetadataHistoryStepResponseToolCallInputClickClick(BaseModel):
    flag: int


class ChatHumanLlmMetadataHistoryStepResponseToolCallInputClick(BaseModel):
    click: ChatHumanLlmMetadataHistoryStepResponseToolCallInputClickClick = FieldInfo(alias="Click")


class ChatHumanLlmMetadataHistoryStepResponseToolCallInputHoverHover(BaseModel):
    flag: int


class ChatHumanLlmMetadataHistoryStepResponseToolCallInputHover(BaseModel):
    hover: ChatHumanLlmMetadataHistoryStepResponseToolCallInputHoverHover = FieldInfo(alias="Hover")


class ChatHumanLlmMetadataHistoryStepResponseToolCallInputWaitWait(BaseModel):
    seconds: int
    """Time in seconds to wait"""


class ChatHumanLlmMetadataHistoryStepResponseToolCallInputWait(BaseModel):
    wait: ChatHumanLlmMetadataHistoryStepResponseToolCallInputWaitWait = FieldInfo(alias="Wait")


class ChatHumanLlmMetadataHistoryStepResponseToolCallInputErrorError(BaseModel):
    error: str


class ChatHumanLlmMetadataHistoryStepResponseToolCallInputError(BaseModel):
    error: ChatHumanLlmMetadataHistoryStepResponseToolCallInputErrorError = FieldInfo(alias="Error")


class ChatHumanLlmMetadataHistoryStepResponseToolCallInputGoogleGoogle(BaseModel):
    query: str


class ChatHumanLlmMetadataHistoryStepResponseToolCallInputGoogle(BaseModel):
    google: ChatHumanLlmMetadataHistoryStepResponseToolCallInputGoogleGoogle = FieldInfo(alias="Google")


class ChatHumanLlmMetadataHistoryStepResponseToolCallInputTypeType(BaseModel):
    flag: int

    input: str


class ChatHumanLlmMetadataHistoryStepResponseToolCallInputType(BaseModel):
    type: ChatHumanLlmMetadataHistoryStepResponseToolCallInputTypeType = FieldInfo(alias="Type")


ChatHumanLlmMetadataHistoryStepResponseToolCallInput = Union[
    ChatHumanLlmMetadataHistoryStepResponseToolCallInputSave,
    ChatHumanLlmMetadataHistoryStepResponseToolCallInputScroll,
    ChatHumanLlmMetadataHistoryStepResponseToolCallInputExit,
    ChatHumanLlmMetadataHistoryStepResponseToolCallInputClick,
    ChatHumanLlmMetadataHistoryStepResponseToolCallInputHover,
    ChatHumanLlmMetadataHistoryStepResponseToolCallInputWait,
    ChatHumanLlmMetadataHistoryStepResponseToolCallInputError,
    ChatHumanLlmMetadataHistoryStepResponseToolCallInputGoogle,
    ChatHumanLlmMetadataHistoryStepResponseToolCallInputType,
]


class ChatHumanLlmMetadataHistoryStepResponseToolCallResultToolQueued(BaseModel):
    tool_queued: str = FieldInfo(alias="ToolQueued")


class ChatHumanLlmMetadataHistoryStepResponseToolCallResultToolFail(BaseModel):
    tool_fail: str = FieldInfo(alias="ToolFail")


class ChatHumanLlmMetadataHistoryStepResponseToolCallResultInputParseFail(BaseModel):
    input_parse_fail: str = FieldInfo(alias="InputParseFail")


class ChatHumanLlmMetadataHistoryStepResponseToolCallResultSuccess(BaseModel):
    success: str = FieldInfo(alias="Success")


ChatHumanLlmMetadataHistoryStepResponseToolCallResult = Union[
    ChatHumanLlmMetadataHistoryStepResponseToolCallResultToolQueued,
    ChatHumanLlmMetadataHistoryStepResponseToolCallResultToolFail,
    ChatHumanLlmMetadataHistoryStepResponseToolCallResultInputParseFail,
    ChatHumanLlmMetadataHistoryStepResponseToolCallResultSuccess,
    None,
]


class ChatHumanLlmMetadataHistoryStepResponseToolCall(BaseModel):
    input: ChatHumanLlmMetadataHistoryStepResponseToolCallInput

    name: Literal["Save", "Scroll", "Exit", "Click", "Hover", "Wait", "Error", "Google", "Type"]

    result: Optional[ChatHumanLlmMetadataHistoryStepResponseToolCallResult] = None


class ChatHumanLlmMetadataHistoryStepResponse(BaseModel):
    completion_tokens: int

    cost: float
    """Cost in dollars"""

    llm: str

    prompt_tokens: int
    """New tokens"""

    text: str

    tool_calls: List[ChatHumanLlmMetadataHistoryStepResponseToolCall]


class ChatHumanLlmMetadataHistoryStep(BaseModel):
    prompt: ChatHumanLlmMetadataHistoryStepPrompt

    response: ChatHumanLlmMetadataHistoryStepResponse

    uuid: str


class ChatHumanLlmMetadataHistory(BaseModel):
    date: datetime

    steps: List[ChatHumanLlmMetadataHistoryStep]

    uuid: str
    """Used to identify this history"""


class ChatHumanLlmMetadata(BaseModel):
    descriptor: DatasetDescriptor
    """A dataset is where you put multiple referential schemas.

    A dataset is a complete namespace where all references between schemas are held
    within the dataset.
    """

    run_id: str

    user_email: str

    history: Optional[ChatHumanLlmMetadataHistory] = None


class ChatMetadataExtractedEntityEntity(BaseModel):
    id: int

    properties: Dict[str, str]

    type: str


class ChatMetadataExtractedEntityRelationship(BaseModel):
    source: int

    target: int

    type: str


class ChatMetadataExtractedEntity(BaseModel):
    entities: Optional[List[ChatMetadataExtractedEntityEntity]] = None

    relationships: Optional[List[ChatMetadataExtractedEntityRelationship]] = None


class ChatMetadataToolMetadata(BaseModel):
    description: str

    name: Literal["Save", "Scroll", "Exit", "Click", "Hover", "Wait", "Error", "Google", "Type"]

    regex_validator: str

    tool_validator: object


class ChatMetadataWebFlag(BaseModel):
    aria_label: str = FieldInfo(alias="ariaLabel")

    height: float

    text: str

    type: str

    width: float

    x: float

    y: float


class ChatMetadata(BaseModel):
    conditioning_prompt: str

    dataset_descriptor: DatasetDescriptor
    """A dataset is where you put multiple referential schemas.

    A dataset is a complete namespace where all references between schemas are held
    within the dataset.
    """

    extracted_entities: List[ChatMetadataExtractedEntity]

    tool_metadata: List[ChatMetadataToolMetadata]

    screenshot: Optional[object] = None

    url: Optional[str] = None

    web_flags: Optional[List[ChatMetadataWebFlag]] = None


class Chat(BaseModel):
    decoding_params: ChatDecodingParams

    messages: List[ChatMessage]

    human_llm_metadata: Optional[ChatHumanLlmMetadata] = None

    metadata: Optional[ChatMetadata] = None


class LabelGetMessagesResponse(BaseModel):
    chat: Chat

    run_id: str

    uuid: str
