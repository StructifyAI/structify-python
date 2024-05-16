# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union, Iterable, Optional
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._types import FileTypes
from .._utils import PropertyInfo
from .dataset_descriptor_param import DatasetDescriptorParam

__all__ = [
    "LabelLlmAssistParams",
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


class LabelLlmAssistParams(TypedDict, total=False):
    decoding_params: Required[DecodingParams]

    messages: Required[Iterable[Message]]

    metadata: Optional[Metadata]


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


class DecodingParamsParameterFunctions(TypedDict, total=False):
    functions: Required[Annotated[Iterable[object], PropertyInfo(alias="Functions")]]


class DecodingParamsParameterJsonValidator(TypedDict, total=False):
    json_validator: Required[Annotated[object, PropertyInfo(alias="JsonValidator")]]


class DecodingParamsParameterRegexValidator(TypedDict, total=False):
    regex_validator: Required[Annotated[str, PropertyInfo(alias="RegexValidator")]]


class DecodingParamsParameterContextFreeeGrammar(TypedDict, total=False):
    context_freee_grammar: Required[Annotated[str, PropertyInfo(alias="ContextFreeeGrammar")]]


class DecodingParamsParameterCrop(TypedDict, total=False):
    crop: Required[Annotated[bool, PropertyInfo(alias="Crop")]]


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


class DecodingParams(TypedDict, total=False):
    parameters: Required[Iterable[DecodingParamsParameter]]


class MessageContentText(TypedDict, total=False):
    text: Required[Annotated[str, PropertyInfo(alias="Text")]]


class MessageContentImage(TypedDict, total=False):
    image: Required[Annotated[FileTypes, PropertyInfo(alias="Image")]]


MessageContent = Union[MessageContentText, MessageContentImage]


class Message(TypedDict, total=False):
    content: Required[Iterable[MessageContent]]
    """
    We want this to be a vec of contents so we can accurately capture an
    interleaving of images and text.

    This is meant to be a completely raw, unprocessed representation of the text.
    Don't take stuff out.
    """

    role: Required[Literal["user", "system", "assistant"]]


class MetadataExtractedEntityEntity(TypedDict, total=False):
    id: Required[int]

    properties: Required[Dict[str, str]]

    type: Required[str]


class MetadataExtractedEntityRelationship(TypedDict, total=False):
    source: Required[int]

    target: Required[int]

    type: Required[str]


class MetadataExtractedEntity(TypedDict, total=False):
    entities: Iterable[MetadataExtractedEntityEntity]

    relationships: Iterable[MetadataExtractedEntityRelationship]


class MetadataToolMetadata(TypedDict, total=False):
    description: Required[str]

    name: Required[Literal["Save", "Scroll", "Exit", "Click", "Hover", "Wait", "Error", "Google", "Type"]]

    regex_validator: Required[str]

    tool_validator: Required[object]


class MetadataWebFlag(TypedDict, total=False):
    aria_label: Required[Annotated[str, PropertyInfo(alias="ariaLabel")]]

    text: Required[str]

    type: Required[str]

    x: Required[float]

    y: Required[float]


class Metadata(TypedDict, total=False):
    conditioning_prompt: Required[str]

    dataset_descriptor: Required[DatasetDescriptorParam]
    """A dataset is where you put multiple referential schemas.

    A dataset is a complete namespace where all references between schemas are held
    within the dataset.
    """

    extracted_entities: Required[Iterable[MetadataExtractedEntity]]

    tool_metadata: Required[Iterable[MetadataToolMetadata]]

    web_flags: Optional[Iterable[MetadataWebFlag]]
