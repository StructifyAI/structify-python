# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
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

    text: str

    type: str

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

    web_flags: Optional[List[ChatMetadataWebFlag]] = None


class Chat(BaseModel):
    decoding_params: ChatDecodingParams

    messages: List[ChatMessage]

    metadata: Optional[ChatMetadata] = None


class LabelGetMessagesResponse(BaseModel):
    chat: Chat

    uuid: str
