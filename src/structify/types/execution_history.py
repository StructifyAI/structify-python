# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .label.tool_input import ToolInput
from .dataset_descriptor import DatasetDescriptor

__all__ = [
    "ExecutionHistory",
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
    "StepPromptMetadataExtractionCriterion",
    "StepPromptMetadataToolMetadata",
    "StepPromptMetadataWebFlag",
    "StepResponse",
    "StepResponseToolCall",
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

    history: Optional[ExecutionHistory] = None


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


class StepPromptMetadataExtractionCriterion(BaseModel):
    property_names: List[str]

    table_name: str
    """Vec<ExtractionCriteria> = it has to meet every one."""


class StepPromptMetadataToolMetadata(BaseModel):
    description: str

    name: Literal["Save", "Scroll", "Exit", "Click", "Hover", "Wait", "Error", "Google", "Type"]

    regex_validator: str

    tool_validator: object


class StepPromptMetadataWebFlag(BaseModel):
    aria_label: str = FieldInfo(alias="ariaLabel")

    height: float

    text: str

    type: str

    width: float

    x: float

    y: float


class StepPromptMetadata(BaseModel):
    dataset_descriptor: DatasetDescriptor
    """A dataset is where you put multiple referential schemas.

    A dataset is a complete namespace where all references between schemas are held
    within the dataset.
    """

    extracted_entities: List[StepPromptMetadataExtractedEntity]

    extraction_criteria: List[StepPromptMetadataExtractionCriterion]

    tool_metadata: List[StepPromptMetadataToolMetadata]

    screenshot: Optional[object] = None

    url: Optional[str] = None

    web_flags: Optional[List[StepPromptMetadataWebFlag]] = None


class StepPrompt(BaseModel):
    decoding_params: StepPromptDecodingParams

    messages: List[StepPromptMessage]

    human_llm_metadata: Optional[StepPromptHumanLlmMetadata] = None

    metadata: Optional[StepPromptMetadata] = None


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
    input: ToolInput

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


class ExecutionHistory(BaseModel):
    date: datetime

    steps: List[Step]

    uuid: str
    """Used to identify this history"""
