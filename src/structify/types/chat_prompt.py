# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .tool_metadata import ToolMetadata
from .knowledge_graph import KnowledgeGraph
from .dataset_descriptor import DatasetDescriptor

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
    "DecodingParamsParameterLogitBias",
    "DecodingParamsParameterFunctions",
    "DecodingParamsParameterJsonValidator",
    "DecodingParamsParameterRegexValidator",
    "DecodingParamsParameterContextFreeGrammar",
    "DecodingParamsParameterNumBeams",
    "DecodingParamsParameterCrop",
    "Message",
    "MessageContent",
    "MessageContentText",
    "MessageContentImage",
    "Metadata",
    "MetadataExtractionCriterion",
    "MetadataExtractionCriterionRelationship",
    "MetadataExtractionCriterionRelationshipRelationship",
    "MetadataExtractionCriterionEntity",
    "MetadataExtractionCriterionEntityEntity",
    "MetadataExtractionCriterionProperty",
    "MetadataExtractionCriterionPropertyProperty",
    "MetadataFormatterSpecific",
    "MetadataFormatterSpecificImageMeta",
    "MetadataFormatterSpecificImageMetaImageMeta",
    "MetadataFormatterSpecificWebMeta",
    "MetadataFormatterSpecificWebMetaWebMeta",
    "MetadataFormatterSpecificWebMetaWebMetaFlag",
    "MetadataFormatterSpecificTextMeta",
    "MetadataFormatterSpecificTextMetaTextMeta",
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


class DecodingParamsParameterLogitBias(BaseModel):
    logit_bias: Dict[str, float] = FieldInfo(alias="LogitBias")


class DecodingParamsParameterFunctions(BaseModel):
    functions: List[Dict[str, object]] = FieldInfo(alias="Functions")


class DecodingParamsParameterJsonValidator(BaseModel):
    json_validator: Dict[str, object] = FieldInfo(alias="JsonValidator")


class DecodingParamsParameterRegexValidator(BaseModel):
    regex_validator: str = FieldInfo(alias="RegexValidator")


class DecodingParamsParameterContextFreeGrammar(BaseModel):
    context_free_grammar: str = FieldInfo(alias="ContextFreeGrammar")


class DecodingParamsParameterNumBeams(BaseModel):
    num_beams: int = FieldInfo(alias="NumBeams")


class DecodingParamsParameterCrop(BaseModel):
    crop: bool = FieldInfo(alias="Crop")


DecodingParamsParameter: TypeAlias = Union[
    DecodingParamsParameterMaxTokens,
    DecodingParamsParameterTopP,
    DecodingParamsParameterRepeatWindow,
    DecodingParamsParameterRepeatPenalty,
    DecodingParamsParameterTemperature,
    DecodingParamsParameterStopTokens,
    DecodingParamsParameterLogitBias,
    DecodingParamsParameterFunctions,
    DecodingParamsParameterJsonValidator,
    DecodingParamsParameterRegexValidator,
    DecodingParamsParameterContextFreeGrammar,
    DecodingParamsParameterNumBeams,
    DecodingParamsParameterCrop,
]


class DecodingParams(BaseModel):
    parameters: List[DecodingParamsParameter]


class MessageContentText(BaseModel):
    text: str = FieldInfo(alias="Text")


class MessageContentImage(BaseModel):
    image: object = FieldInfo(alias="Image")


MessageContent: TypeAlias = Union[MessageContentText, MessageContentImage]


class Message(BaseModel):
    content: List[MessageContent]
    """
    We want this to be a vec of contents so we can accurately capture an
    interleaving of images and text.

    This is meant to be a completely raw, unprocessed representation of the text.
    Don't take stuff out.
    """

    role: Literal["user", "system", "assistant"]


class MetadataExtractionCriterionRelationshipRelationship(BaseModel):
    relationship_name: str


class MetadataExtractionCriterionRelationship(BaseModel):
    relationship: MetadataExtractionCriterionRelationshipRelationship = FieldInfo(alias="Relationship")


class MetadataExtractionCriterionEntityEntity(BaseModel):
    seeded_kg_id: int
    """The integer id corresponding to an entity in the seeded kg"""

    dataset_entity_id: Optional[str] = None


class MetadataExtractionCriterionEntity(BaseModel):
    entity: MetadataExtractionCriterionEntityEntity = FieldInfo(alias="Entity")


class MetadataExtractionCriterionPropertyProperty(BaseModel):
    property_names: List[str]

    table_name: str
    """Vec<ExtractionCriteria> = it has to meet every one."""


class MetadataExtractionCriterionProperty(BaseModel):
    property: MetadataExtractionCriterionPropertyProperty = FieldInfo(alias="Property")


MetadataExtractionCriterion: TypeAlias = Union[
    MetadataExtractionCriterionRelationship, MetadataExtractionCriterionEntity, MetadataExtractionCriterionProperty
]


class MetadataFormatterSpecificImageMetaImageMeta(BaseModel):
    document_name: Optional[str] = None

    document_page: Optional[int] = None

    image: Optional[object] = None

    ocr_content: Optional[str] = None


class MetadataFormatterSpecificImageMeta(BaseModel):
    image_meta: MetadataFormatterSpecificImageMetaImageMeta = FieldInfo(alias="ImageMeta")


class MetadataFormatterSpecificWebMetaWebMetaFlag(BaseModel):
    aria_label: str = FieldInfo(alias="ariaLabel")

    type: str

    x: float

    y: float

    height: Optional[float] = None

    href: Optional[str] = None

    is_interactive: Optional[bool] = FieldInfo(alias="isInteractive", default=None)

    number: Optional[int] = None
    """The number by which the flag is referred in image, prompt, and tool calls."""

    text: Optional[str] = None

    width: Optional[float] = None
    """
    The serde default here is to give us backwards compatibility it's fine for these
    to be anything as long as the image isn't given since it won't regenerate.
    """


class MetadataFormatterSpecificWebMetaWebMeta(BaseModel):
    flags: List[MetadataFormatterSpecificWebMetaWebMetaFlag]

    url: str

    ocr_content: Optional[str] = None

    screenshot: Optional[object] = None


class MetadataFormatterSpecificWebMeta(BaseModel):
    web_meta: MetadataFormatterSpecificWebMetaWebMeta = FieldInfo(alias="WebMeta")


class MetadataFormatterSpecificTextMetaTextMeta(BaseModel):
    text: str


class MetadataFormatterSpecificTextMeta(BaseModel):
    text_meta: MetadataFormatterSpecificTextMetaTextMeta = FieldInfo(alias="TextMeta")


MetadataFormatterSpecific: TypeAlias = Union[
    MetadataFormatterSpecificImageMeta, MetadataFormatterSpecificWebMeta, MetadataFormatterSpecificTextMeta
]


class Metadata(BaseModel):
    dataset_descriptor: DatasetDescriptor
    """A dataset is where you put multiple referential schemas.

    A dataset is a complete namespace where all references between schemas are held
    within the dataset.
    """

    extracted_entities: List[KnowledgeGraph]

    extraction_criteria: List[MetadataExtractionCriterion]

    formatter_specific: MetadataFormatterSpecific

    tool_metadata: List[ToolMetadata]


class ChatPrompt(BaseModel):
    decoding_params: DecodingParams

    messages: List[Message]

    metadata: Metadata
    """All metadata required to generate a prompt for the LLM"""
