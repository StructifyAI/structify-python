# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from .message import Message
from .._models import BaseModel
from .tool_metadata import ToolMetadata
from .knowledge_graph import KnowledgeGraph
from .save_requirement import SaveRequirement
from .dataset_descriptor import DatasetDescriptor

__all__ = [
    "ChatPrompt",
    "DecodingParams",
    "DecodingParamsParameter",
    "DecodingParamsParameterMaxTokens",
    "DecodingParamsParameterMaxCompletionTokens",
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
    "DecodingParamsParameterThinking",
    "DecodingParamsParameterVerbosity",
    "DecodingParamsParameterReasoningEffort",
    "Metadata",
    "MetadataFormatterSpecific",
    "MetadataFormatterSpecificImageMeta",
    "MetadataFormatterSpecificImageMetaImageMeta",
    "MetadataFormatterSpecificWebMeta",
    "MetadataFormatterSpecificWebMetaWebMeta",
    "MetadataFormatterSpecificWebMetaWebMetaFlag",
    "MetadataFormatterSpecificTextMeta",
    "MetadataFormatterSpecificTextMetaTextMeta",
    "MetadataFormatterSpecificScraperMeta",
    "MetadataFormatterSpecificScraperMetaScraperMeta",
]


class DecodingParamsParameterMaxTokens(BaseModel):
    max_tokens: int = FieldInfo(alias="MaxTokens")


class DecodingParamsParameterMaxCompletionTokens(BaseModel):
    max_completion_tokens: int = FieldInfo(alias="MaxCompletionTokens")


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


class DecodingParamsParameterThinking(BaseModel):
    thinking: int = FieldInfo(alias="Thinking")
    """Thinking tokens for Claude 3.7. Contains the budget in tokens for thinking."""


class DecodingParamsParameterVerbosity(BaseModel):
    verbosity: Literal["low", "medium", "high"] = FieldInfo(alias="Verbosity")


class DecodingParamsParameterReasoningEffort(BaseModel):
    reasoning_effort: Literal["low", "medium", "high", "minimal"] = FieldInfo(alias="ReasoningEffort")


DecodingParamsParameter: TypeAlias = Union[
    DecodingParamsParameterMaxTokens,
    DecodingParamsParameterMaxCompletionTokens,
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
    DecodingParamsParameterThinking,
    DecodingParamsParameterVerbosity,
    DecodingParamsParameterReasoningEffort,
]


class DecodingParams(BaseModel):
    parameters: List[DecodingParamsParameter]


class MetadataFormatterSpecificImageMetaImageMeta(BaseModel):
    image: Optional[str] = None

    document_name: Optional[str] = None

    document_page: Optional[int] = None

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


class MetadataFormatterSpecificScraperMetaScraperMeta(BaseModel):
    html_content: str

    url: str


class MetadataFormatterSpecificScraperMeta(BaseModel):
    scraper_meta: MetadataFormatterSpecificScraperMetaScraperMeta = FieldInfo(alias="ScraperMeta")


MetadataFormatterSpecific: TypeAlias = Union[
    MetadataFormatterSpecificImageMeta,
    MetadataFormatterSpecificWebMeta,
    MetadataFormatterSpecificTextMeta,
    MetadataFormatterSpecificScraperMeta,
]


class Metadata(BaseModel):
    dataset_descriptor: DatasetDescriptor
    """A dataset is where you put multiple referential schemas.

    A dataset is a complete namespace where all references between schemas are held
    within the dataset.
    """

    extracted_entities: List[KnowledgeGraph]

    extraction_criteria: List[SaveRequirement]

    formatter_specific: MetadataFormatterSpecific

    tool_metadata: List[ToolMetadata]

    qa_potentially_sus_response: Optional[str] = None


class ChatPrompt(BaseModel):
    decoding_params: DecodingParams

    messages: List[Message]

    metadata: Metadata
    """All metadata required to generate a prompt for the LLM"""
