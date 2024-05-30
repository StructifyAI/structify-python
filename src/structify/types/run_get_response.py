# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .dataset_descriptor import DatasetDescriptor

__all__ = [
    "RunGetResponse",
    "Step",
    "StepPrompt",
    "StepPromptDecodingParams",
    "StepPromptDecodingParamsParameter",
    "StepPromptDecodingParamsParameterMaxTokens",
    "StepPromptDecodingParamsParameterTopP",
    "StepPromptDecodingParamsParameterRepeatWindow",
    "StepPromptDecodingParamsParameterRepeatPenalty",
    "StepPromptDecodingParamsParameterTemperature",
    "StepPromptDecodingParamsParameterStopTokens",
    "StepPromptDecodingParamsParameterFunctions",
    "StepPromptDecodingParamsParameterJsonValidator",
    "StepPromptDecodingParamsParameterRegexValidator",
    "StepPromptDecodingParamsParameterContextFreeeGrammar",
    "StepPromptDecodingParamsParameterCrop",
    "StepPromptMessage",
    "StepPromptMessageContent",
    "StepPromptMessageContentText",
    "StepPromptMessageContentImage",
    "StepPromptHumanLlmMetadata",
    "StepPromptMetadata",
    "StepPromptMetadataExtractedEntity",
    "StepPromptMetadataExtractedEntityEntity",
    "StepPromptMetadataExtractedEntityRelationship",
    "StepPromptMetadataToolMetadata",
    "StepPromptMetadataWebFlag",
    "StepResponse",
    "StepResponseToolCall",
    "StepResponseToolCallInput",
    "StepResponseToolCallInputSave",
    "StepResponseToolCallInputSaveSave",
    "StepResponseToolCallInputSaveSaveEntity",
    "StepResponseToolCallInputSaveSaveRelationship",
    "StepResponseToolCallInputScroll",
    "StepResponseToolCallInputScrollScroll",
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
]


class StepPromptDecodingParamsParameterMaxTokens(BaseModel):
    max_tokens: int = FieldInfo(alias="MaxTokens")


class StepPromptDecodingParamsParameterTopP(BaseModel):
    top_p: float = FieldInfo(alias="TopP")


class StepPromptDecodingParamsParameterRepeatWindow(BaseModel):
    repeat_window: int = FieldInfo(alias="RepeatWindow")


class StepPromptDecodingParamsParameterRepeatPenalty(BaseModel):
    repeat_penalty: float = FieldInfo(alias="RepeatPenalty")


class StepPromptDecodingParamsParameterTemperature(BaseModel):
    temperature: float = FieldInfo(alias="Temperature")


class StepPromptDecodingParamsParameterStopTokens(BaseModel):
    stop_tokens: List[str] = FieldInfo(alias="StopTokens")


class StepPromptDecodingParamsParameterFunctions(BaseModel):
    functions: List[object] = FieldInfo(alias="Functions")


class StepPromptDecodingParamsParameterJsonValidator(BaseModel):
    json_validator: object = FieldInfo(alias="JsonValidator")


class StepPromptDecodingParamsParameterRegexValidator(BaseModel):
    regex_validator: str = FieldInfo(alias="RegexValidator")


class StepPromptDecodingParamsParameterContextFreeeGrammar(BaseModel):
    context_freee_grammar: str = FieldInfo(alias="ContextFreeeGrammar")


class StepPromptDecodingParamsParameterCrop(BaseModel):
    crop: bool = FieldInfo(alias="Crop")


StepPromptDecodingParamsParameter = Union[
    StepPromptDecodingParamsParameterMaxTokens,
    StepPromptDecodingParamsParameterTopP,
    StepPromptDecodingParamsParameterRepeatWindow,
    StepPromptDecodingParamsParameterRepeatPenalty,
    StepPromptDecodingParamsParameterTemperature,
    StepPromptDecodingParamsParameterStopTokens,
    StepPromptDecodingParamsParameterFunctions,
    StepPromptDecodingParamsParameterJsonValidator,
    StepPromptDecodingParamsParameterRegexValidator,
    StepPromptDecodingParamsParameterContextFreeeGrammar,
    StepPromptDecodingParamsParameterCrop,
]


class StepPromptDecodingParams(BaseModel):
    parameters: List[StepPromptDecodingParamsParameter]


class StepPromptMessageContentText(BaseModel):
    text: str = FieldInfo(alias="Text")


class StepPromptMessageContentImage(BaseModel):
    image: object = FieldInfo(alias="Image")


StepPromptMessageContent = Union[StepPromptMessageContentText, StepPromptMessageContentImage]


class StepPromptMessage(BaseModel):
    content: List[StepPromptMessageContent]
    """
    We want this to be a vec of contents so we can accurately capture an
    interleaving of images and text.

    This is meant to be a completely raw, unprocessed representation of the text.
    Don't take stuff out.
    """

    role: Literal["user", "system", "assistant"]


class StepPromptHumanLlmMetadata(BaseModel):
    descriptor: DatasetDescriptor
    """A dataset is where you put multiple referential schemas.

    A dataset is a complete namespace where all references between schemas are held
    within the dataset.
    """

    run_id: str

    user_email: str


class StepPromptMetadataExtractedEntityEntity(BaseModel):
    id: int

    properties: Dict[str, str]

    type: str


class StepPromptMetadataExtractedEntityRelationship(BaseModel):
    source: int

    target: int

    type: str


class StepPromptMetadataExtractedEntity(BaseModel):
    entities: Optional[List[StepPromptMetadataExtractedEntityEntity]] = None

    relationships: Optional[List[StepPromptMetadataExtractedEntityRelationship]] = None


class StepPromptMetadataToolMetadata(BaseModel):
    description: str

    name: Literal["Save", "Scroll", "Exit", "Click", "Hover", "Wait", "Error", "Google", "Type"]

    regex_validator: str

    tool_validator: object


class StepPromptMetadataWebFlag(BaseModel):
    aria_label: str = FieldInfo(alias="ariaLabel")

    text: str

    type: str

    x: float

    y: float


class StepPromptMetadata(BaseModel):
    conditioning_prompt: str

    dataset_descriptor: DatasetDescriptor
    """A dataset is where you put multiple referential schemas.

    A dataset is a complete namespace where all references between schemas are held
    within the dataset.
    """

    extracted_entities: List[StepPromptMetadataExtractedEntity]

    tool_metadata: List[StepPromptMetadataToolMetadata]

    url: Optional[str] = None

    web_flags: Optional[List[StepPromptMetadataWebFlag]] = None


class StepPrompt(BaseModel):
    decoding_params: StepPromptDecodingParams

    messages: List[StepPromptMessage]

    human_llm_metadata: Optional[StepPromptHumanLlmMetadata] = None

    metadata: Optional[StepPromptMetadata] = None


class StepResponseToolCallInputSaveSaveEntity(BaseModel):
    id: int

    properties: Dict[str, str]

    type: str


class StepResponseToolCallInputSaveSaveRelationship(BaseModel):
    source: int

    target: int

    type: str


class StepResponseToolCallInputSaveSave(BaseModel):
    entities: Optional[List[StepResponseToolCallInputSaveSaveEntity]] = None

    relationships: Optional[List[StepResponseToolCallInputSaveSaveRelationship]] = None


class StepResponseToolCallInputSave(BaseModel):
    save: StepResponseToolCallInputSaveSave = FieldInfo(alias="Save")
    """
    Knowledge graph info structured to deserialize and display in the same format
    that the LLM outputs.
    """


class StepResponseToolCallInputScrollScroll(BaseModel):
    reason: str
    """OpenAI Requires an argument, so we put a dummy one here."""


class StepResponseToolCallInputScroll(BaseModel):
    scroll: StepResponseToolCallInputScrollScroll = FieldInfo(alias="Scroll")
    """For tools with no inputs."""


class StepResponseToolCallInputExitExit(BaseModel):
    reason: str
    """OpenAI Requires an argument, so we put a dummy one here."""


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
    seconds: int
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


StepResponseToolCallInput = Union[
    StepResponseToolCallInputSave,
    StepResponseToolCallInputScroll,
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


StepResponseToolCallResult = Union[
    StepResponseToolCallResultToolQueued,
    StepResponseToolCallResultToolFail,
    StepResponseToolCallResultInputParseFail,
    StepResponseToolCallResultSuccess,
    None,
]


class StepResponseToolCall(BaseModel):
    input: StepResponseToolCallInput

    name: Literal["Save", "Scroll", "Exit", "Click", "Hover", "Wait", "Error", "Google", "Type"]

    result: Optional[StepResponseToolCallResult] = None


class StepResponse(BaseModel):
    completion_tokens: int

    cost: float
    """Cost in dollars"""

    llm: str

    prompt_tokens: int
    """New tokens"""

    text: str

    tool_calls: List[StepResponseToolCall]


class Step(BaseModel):
    prompt: StepPrompt

    response: StepResponse


class RunGetResponse(BaseModel):
    date: datetime

    steps: List[Step]

    uuid: str
    """Used to identify this history"""
