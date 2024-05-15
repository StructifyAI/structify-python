# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .dataset_descriptor import DatasetDescriptor

__all__ = [
    "LabelGetMessagesResponse",
    "DecodingParams",
    "DecodingParamsParameter",
    "DecodingParamsParameterMaxTokens",
    "DecodingParamsParameterTopP",
    "DecodingParamsParameterRepeatWindow",
    "DecodingParamsParameterRepeatPenalty",
    "DecodingParamsParameterTemperature",
    "DecodingParamsParameterStopTokens",
    "DecodingParamsParameterFunctions",
    "DecodingParamsParameterJsonValidator",
    "DecodingParamsParameterRegexValidator",
    "DecodingParamsParameterContextFreeeGrammar",
    "DecodingParamsParameterCrop",
    "Message",
    "MessageContent",
    "MessageContentText",
    "MessageContentImage",
    "Metadata",
    "MetadataExtractedEntity",
    "MetadataExtractedEntityEntity",
    "MetadataExtractedEntityRelationship",
    "MetadataToolMetadata",
    "MetadataWebFlag",
]


class DecodingParamsParameterMaxTokens(BaseModel):
    max_tokens: int = FieldInfo(alias="MaxTokens")


class DecodingParamsParameterTopP(BaseModel):
    top_p: float = FieldInfo(alias="TopP")


class DecodingParamsParameterRepeatWindow(BaseModel):
    repeat_window: int = FieldInfo(alias="RepeatWindow")


class DecodingParamsParameterRepeatPenalty(BaseModel):
    repeat_penalty: float = FieldInfo(alias="RepeatPenalty")


class DecodingParamsParameterTemperature(BaseModel):
    temperature: float = FieldInfo(alias="Temperature")


class DecodingParamsParameterStopTokens(BaseModel):
    stop_tokens: List[str] = FieldInfo(alias="StopTokens")


class DecodingParamsParameterFunctions(BaseModel):
    functions: List[object] = FieldInfo(alias="Functions")


class DecodingParamsParameterJsonValidator(BaseModel):
    json_validator: object = FieldInfo(alias="JsonValidator")


class DecodingParamsParameterRegexValidator(BaseModel):
    regex_validator: str = FieldInfo(alias="RegexValidator")


class DecodingParamsParameterContextFreeeGrammar(BaseModel):
    context_freee_grammar: str = FieldInfo(alias="ContextFreeeGrammar")


class DecodingParamsParameterCrop(BaseModel):
    crop: bool = FieldInfo(alias="Crop")


DecodingParamsParameter = Union[
    DecodingParamsParameterMaxTokens,
    DecodingParamsParameterTopP,
    DecodingParamsParameterRepeatWindow,
    DecodingParamsParameterRepeatPenalty,
    DecodingParamsParameterTemperature,
    DecodingParamsParameterStopTokens,
    DecodingParamsParameterFunctions,
    DecodingParamsParameterJsonValidator,
    DecodingParamsParameterRegexValidator,
    DecodingParamsParameterContextFreeeGrammar,
    DecodingParamsParameterCrop,
]


class DecodingParams(BaseModel):
    parameters: List[DecodingParamsParameter]


class MessageContentText(BaseModel):
    text: str = FieldInfo(alias="Text")


class MessageContentImage(BaseModel):
    image: object = FieldInfo(alias="Image")


MessageContent = Union[MessageContentText, MessageContentImage]


class Message(BaseModel):
    content: List[MessageContent]
    """
    We want this to be a vec of contents so we can accurately capture an
    interleaving of images and text.

    This is meant to be a completely raw, unprocessed representation of the text.
    Don't take stuff out.
    """

    role: Literal["user", "system", "assistant"]


class MetadataExtractedEntityEntity(BaseModel):
    id: int

    properties: Dict[str, str]

    type: str


class MetadataExtractedEntityRelationship(BaseModel):
    source: int

    target: int

    type: str


class MetadataExtractedEntity(BaseModel):
    entities: Optional[List[MetadataExtractedEntityEntity]] = None

    relationships: Optional[List[MetadataExtractedEntityRelationship]] = None


class MetadataToolMetadata(BaseModel):
    description: str

    name: Literal["Save", "Scroll", "Exit", "Click", "Hover", "Wait", "Error", "Google", "Type"]

    regex_validator: str

    tool_validator: object


class MetadataWebFlag(BaseModel):
    aria_label: str = FieldInfo(alias="ariaLabel")

    text: str

    type: str

    x: float

    y: float


class Metadata(BaseModel):
    conditioning_prompt: str

    dataset_descriptor: DatasetDescriptor
    """A dataset is where you put multiple referential schemas.

    A dataset is a complete namespace where all references between schemas are held
    within the dataset.
    """

    extracted_entities: List[MetadataExtractedEntity]

    tool_metadata: List[MetadataToolMetadata]

    web_flags: Optional[List[MetadataWebFlag]] = None


class LabelGetMessagesResponse(BaseModel):
    decoding_params: DecodingParams

    messages: List[Message]

    metadata: Optional[Metadata] = None
