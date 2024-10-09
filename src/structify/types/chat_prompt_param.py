# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union, Iterable, Optional
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from .._types import FileTypes
from .._utils import PropertyInfo
from .tool_metadata_param import ToolMetadataParam
from .knowledge_graph_param import KnowledgeGraphParam
from .dataset_descriptor_param import DatasetDescriptorParam
from .extraction_criteria_param import ExtractionCriteriaParam

__all__ = [
    "ChatPromptParam",
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
    "MetadataWebFlag",
]


class DecodingParamsParameterMaxTokens(TypedDict, total=False):
    max_tokens: Required[Annotated[int, PropertyInfo(alias="MaxTokens")]]


class DecodingParamsParameterTopP(TypedDict, total=False):
    top_p: Required[Annotated[float, PropertyInfo(alias="TopP")]]


class DecodingParamsParameterRepeatWindow(TypedDict, total=False):
    repeat_window: Required[Annotated[int, PropertyInfo(alias="RepeatWindow")]]


class DecodingParamsParameterRepeatPenalty(TypedDict, total=False):
    repeat_penalty: Required[Annotated[float, PropertyInfo(alias="RepeatPenalty")]]


class DecodingParamsParameterTemperature(TypedDict, total=False):
    temperature: Required[Annotated[float, PropertyInfo(alias="Temperature")]]


class DecodingParamsParameterStopTokens(TypedDict, total=False):
    stop_tokens: Required[Annotated[List[str], PropertyInfo(alias="StopTokens")]]


class DecodingParamsParameterLogitBias(TypedDict, total=False):
    logit_bias: Required[Annotated[Dict[str, float], PropertyInfo(alias="LogitBias")]]


class DecodingParamsParameterFunctions(TypedDict, total=False):
    functions: Required[Annotated[Iterable[Dict[str, object]], PropertyInfo(alias="Functions")]]


class DecodingParamsParameterJsonValidator(TypedDict, total=False):
    json_validator: Required[Annotated[Dict[str, object], PropertyInfo(alias="JsonValidator")]]


class DecodingParamsParameterRegexValidator(TypedDict, total=False):
    regex_validator: Required[Annotated[str, PropertyInfo(alias="RegexValidator")]]


class DecodingParamsParameterContextFreeGrammar(TypedDict, total=False):
    context_free_grammar: Required[Annotated[str, PropertyInfo(alias="ContextFreeGrammar")]]


class DecodingParamsParameterNumBeams(TypedDict, total=False):
    num_beams: Required[Annotated[int, PropertyInfo(alias="NumBeams")]]


class DecodingParamsParameterCrop(TypedDict, total=False):
    crop: Required[Annotated[bool, PropertyInfo(alias="Crop")]]


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


class DecodingParams(TypedDict, total=False):
    parameters: Required[Iterable[DecodingParamsParameter]]


class MessageContentText(TypedDict, total=False):
    text: Required[Annotated[str, PropertyInfo(alias="Text")]]


class MessageContentImage(TypedDict, total=False):
    image: Required[Annotated[FileTypes, PropertyInfo(alias="Image")]]


MessageContent: TypeAlias = Union[MessageContentText, MessageContentImage]


class Message(TypedDict, total=False):
    content: Required[Iterable[MessageContent]]
    """
    We want this to be a vec of contents so we can accurately capture an
    interleaving of images and text.

    This is meant to be a completely raw, unprocessed representation of the text.
    Don't take stuff out.
    """

    role: Required[Literal["user", "system", "assistant"]]


class MetadataWebFlag(TypedDict, total=False):
    aria_label: Required[Annotated[str, PropertyInfo(alias="ariaLabel")]]

    type: Required[str]

    x: Required[float]

    y: Required[float]

    height: float

    href: Optional[str]

    number: Optional[int]
    """The number by which the flag is referred in image, prompt, and tool calls."""

    text: str

    width: float
    """
    The serde default here is to give us backwards compatibility it's fine for these
    to be anything as long as the image isn't given since it won't regenerate.
    """


class Metadata(TypedDict, total=False):
    dataset_descriptor: Required[DatasetDescriptorParam]
    """A dataset is where you put multiple referential schemas.

    A dataset is a complete namespace where all references between schemas are held
    within the dataset.
    """

    extracted_entities: Required[Iterable[KnowledgeGraphParam]]

    extraction_criteria: Required[Iterable[ExtractionCriteriaParam]]

    tool_metadata: Required[Iterable[ToolMetadataParam]]

    ocr_content: Optional[str]

    screenshot: Optional[FileTypes]

    url: Optional[str]

    web_flags: Optional[Iterable[MetadataWebFlag]]


class ChatPromptParam(TypedDict, total=False):
    decoding_params: Required[DecodingParams]

    messages: Required[Iterable[Message]]

    metadata: Required[Metadata]
