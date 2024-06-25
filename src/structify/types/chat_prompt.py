# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._compat import PYDANTIC_V2
from .._models import BaseModel
from .tool_metadata import ToolMetadata
from .dataset_descriptor import DatasetDescriptor
from .extraction_criteria import ExtractionCriteria

__all__ = [
    "ChatPrompt",
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
    "HumanLlmMetadata",
    "HumanLlmMetadataHistory",
    "Metadata",
    "MetadataExtractedEntity",
    "MetadataExtractedEntityEntity",
    "MetadataExtractedEntityRelationship",
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


class HumanLlmMetadataHistory(BaseModel):
    date: datetime

    steps: List["ExecutionStep"]

    uuid: str
    """Used to identify this history"""


class HumanLlmMetadata(BaseModel):
    descriptor: DatasetDescriptor
    """A dataset is where you put multiple referential schemas.

    A dataset is a complete namespace where all references between schemas are held
    within the dataset.
    """

    run_id: str

    user_email: str

    history: Optional[HumanLlmMetadataHistory] = None


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


class MetadataWebFlag(BaseModel):
    aria_label: str = FieldInfo(alias="ariaLabel")

    height: float

    text: str

    type: str

    width: float

    x: float

    y: float


class Metadata(BaseModel):
    dataset_descriptor: DatasetDescriptor
    """A dataset is where you put multiple referential schemas.

    A dataset is a complete namespace where all references between schemas are held
    within the dataset.
    """

    extracted_entities: List[MetadataExtractedEntity]

    extraction_criteria: List[ExtractionCriteria]

    tool_metadata: List[ToolMetadata]

    screenshot: Optional[object] = None

    url: Optional[str] = None

    web_flags: Optional[List[MetadataWebFlag]] = None


class ChatPrompt(BaseModel):
    decoding_params: DecodingParams

    messages: List[Message]

    human_llm_metadata: Optional[HumanLlmMetadata] = None

    metadata: Optional[Metadata] = None


from .execution_step import ExecutionStep

if PYDANTIC_V2:
    ChatPrompt.model_rebuild()
    DecodingParams.model_rebuild()
    DecodingParamsParameterMaxTokens.model_rebuild()
    DecodingParamsParameterTopP.model_rebuild()
    DecodingParamsParameterRepeatWindow.model_rebuild()
    DecodingParamsParameterRepeatPenalty.model_rebuild()
    DecodingParamsParameterTemperature.model_rebuild()
    DecodingParamsParameterStopTokens.model_rebuild()
    DecodingParamsParameterFunctions.model_rebuild()
    DecodingParamsParameterJsonValidator.model_rebuild()
    DecodingParamsParameterRegexValidator.model_rebuild()
    DecodingParamsParameterContextFreeeGrammar.model_rebuild()
    DecodingParamsParameterCrop.model_rebuild()
    Message.model_rebuild()
    MessageContentText.model_rebuild()
    MessageContentImage.model_rebuild()
    HumanLlmMetadata.model_rebuild()
    HumanLlmMetadataHistory.model_rebuild()
    Metadata.model_rebuild()
    MetadataExtractedEntity.model_rebuild()
    MetadataExtractedEntityEntity.model_rebuild()
    MetadataExtractedEntityRelationship.model_rebuild()
    MetadataWebFlag.model_rebuild()
else:
    ChatPrompt.update_forward_refs()  # type: ignore
    DecodingParams.update_forward_refs()  # type: ignore
    DecodingParamsParameterMaxTokens.update_forward_refs()  # type: ignore
    DecodingParamsParameterTopP.update_forward_refs()  # type: ignore
    DecodingParamsParameterRepeatWindow.update_forward_refs()  # type: ignore
    DecodingParamsParameterRepeatPenalty.update_forward_refs()  # type: ignore
    DecodingParamsParameterTemperature.update_forward_refs()  # type: ignore
    DecodingParamsParameterStopTokens.update_forward_refs()  # type: ignore
    DecodingParamsParameterFunctions.update_forward_refs()  # type: ignore
    DecodingParamsParameterJsonValidator.update_forward_refs()  # type: ignore
    DecodingParamsParameterRegexValidator.update_forward_refs()  # type: ignore
    DecodingParamsParameterContextFreeeGrammar.update_forward_refs()  # type: ignore
    DecodingParamsParameterCrop.update_forward_refs()  # type: ignore
    Message.update_forward_refs()  # type: ignore
    MessageContentText.update_forward_refs()  # type: ignore
    MessageContentImage.update_forward_refs()  # type: ignore
    HumanLlmMetadata.update_forward_refs()  # type: ignore
    HumanLlmMetadataHistory.update_forward_refs()  # type: ignore
    Metadata.update_forward_refs()  # type: ignore
    MetadataExtractedEntity.update_forward_refs()  # type: ignore
    MetadataExtractedEntityEntity.update_forward_refs()  # type: ignore
    MetadataExtractedEntityRelationship.update_forward_refs()  # type: ignore
    MetadataWebFlag.update_forward_refs()  # type: ignore
