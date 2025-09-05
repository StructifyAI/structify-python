# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union, Optional
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = [
    "ChatEvent",
    "TextMessage",
    "TextMessageTextMessage",
    "ToolCall",
    "ToolCallToolCall",
    "ToolCallToolCallUnionMember0",
    "ToolCallToolCallUnionMember0Input",
    "ToolCallToolCallUnionMember1",
    "ToolCallToolCallUnionMember1Input",
    "ToolCallToolCallUnionMember2",
    "ToolCallToolCallUnionMember2Input",
]


class TextMessageTextMessage(BaseModel):
    message: str


class TextMessage(BaseModel):
    text_message: TextMessageTextMessage = FieldInfo(alias="TextMessage")


class ToolCallToolCallUnionMember0Input(BaseModel):
    query: str


class ToolCallToolCallUnionMember0(BaseModel):
    input: ToolCallToolCallUnionMember0Input

    name: Literal["web_search"]

    result_id: Optional[str] = None

    result_text: Optional[str] = None


class ToolCallToolCallUnionMember1Input(BaseModel):
    url: str


class ToolCallToolCallUnionMember1(BaseModel):
    input: ToolCallToolCallUnionMember1Input

    name: Literal["web_navigate"]

    result_id: Optional[str] = None

    result_text: Optional[str] = None


class ToolCallToolCallUnionMember2Input(BaseModel):
    node_function_name: str


class ToolCallToolCallUnionMember2(BaseModel):
    input: ToolCallToolCallUnionMember2Input

    name: Literal["inspect_dag"]

    result_id: Optional[str] = None

    result_text: Optional[str] = None


ToolCallToolCall: TypeAlias = Union[
    ToolCallToolCallUnionMember0, ToolCallToolCallUnionMember1, ToolCallToolCallUnionMember2
]


class ToolCall(BaseModel):
    tool_call: ToolCallToolCall = FieldInfo(alias="ToolCall")


ChatEvent: TypeAlias = Union[TextMessage, ToolCall]
