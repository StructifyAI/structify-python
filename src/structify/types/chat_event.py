# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = [
    "ChatEvent",
    "TextMessage",
    "TextMessageTextMessage",
    "Thinking",
    "ThinkingThinking",
    "File",
    "FileFile",
    "Action",
    "ActionAction",
    "ActionActionAction",
    "Connector",
    "ConnectorConnector",
    "ToolCall",
    "ToolCallToolCall",
    "ToolCallToolCallUnionMember0",
    "ToolCallToolCallUnionMember0Input",
    "ToolCallToolCallUnionMember1",
    "ToolCallToolCallUnionMember1Input",
    "ToolCallToolCallUnionMember2",
    "ToolCallToolCallUnionMember2Input",
    "ToolCallToolCallUnionMember3",
    "ToolCallToolCallUnionMember3Input",
    "ToolCallToolCallUnionMember4",
    "ToolCallToolCallUnionMember4Input",
    "ToolCallToolCallUnionMember5",
    "ToolCallToolCallUnionMember5Input",
    "ToolCallToolCallUnionMember6",
    "ToolCallToolCallUnionMember6Input",
    "ToolCallToolCallUnionMember7",
    "ToolCallToolCallUnionMember7Input",
    "ToolCallToolCallUnionMember8",
    "ToolCallToolCallUnionMember8Input",
    "ToolCallToolCallUnionMember9",
    "ToolCallToolCallUnionMember9Input",
    "ToolCallToolCallUnionMember10",
    "ToolCallToolCallUnionMember10Input",
    "ToolCallToolCallUnionMember11",
    "ToolCallToolCallUnionMember11Input",
    "Question",
    "QuestionQuestion",
    "InternalError",
    "InternalErrorInternalError",
]


class TextMessageTextMessage(BaseModel):
    message: str


class TextMessage(BaseModel):
    text_message: TextMessageTextMessage = FieldInfo(alias="TextMessage")


class ThinkingThinking(BaseModel):
    content: str


class Thinking(BaseModel):
    thinking: ThinkingThinking = FieldInfo(alias="Thinking")


class FileFile(BaseModel):
    complete: bool

    path: str

    content: Optional[str] = None


class File(BaseModel):
    file: FileFile = FieldInfo(alias="File")
    """
    The file event can't be serialized to the database safely without the content.
    When streaming, we start with the path only, then add the content as we go.
    """


class ActionActionAction(BaseModel):
    description: str

    name: str


class ActionAction(BaseModel):
    actions: List[ActionActionAction]


class Action(BaseModel):
    action: ActionAction = FieldInfo(alias="Action")


class ConnectorConnector(BaseModel):
    env_vars: List[str]

    name: str

    description: Optional[str] = None


class Connector(BaseModel):
    connector: ConnectorConnector = FieldInfo(alias="Connector")


class ToolCallToolCallUnionMember0Input(BaseModel):
    query: str


class ToolCallToolCallUnionMember0(BaseModel):
    input: ToolCallToolCallUnionMember0Input

    name: Literal["WebSearch"]

    result_id: Optional[str] = None

    result_text: Optional[str] = None


class ToolCallToolCallUnionMember1Input(BaseModel):
    url: str


class ToolCallToolCallUnionMember1(BaseModel):
    input: ToolCallToolCallUnionMember1Input

    name: Literal["WebNavigate"]

    result_id: Optional[str] = None

    result_text: Optional[str] = None


class ToolCallToolCallUnionMember2Input(BaseModel):
    node_function_name: str


class ToolCallToolCallUnionMember2(BaseModel):
    input: ToolCallToolCallUnionMember2Input

    name: Literal["InspectDAG"]

    result_id: Optional[str] = None

    result_text: Optional[str] = None


class ToolCallToolCallUnionMember3Input(BaseModel):
    file: str


class ToolCallToolCallUnionMember3(BaseModel):
    input: ToolCallToolCallUnionMember3Input

    name: Literal["DeleteFile"]

    result_id: Optional[str] = None

    result_text: Optional[str] = None


class ToolCallToolCallUnionMember4Input(BaseModel):
    file: str

    new_path: str


class ToolCallToolCallUnionMember4(BaseModel):
    input: ToolCallToolCallUnionMember4Input

    name: Literal["MoveFile"]

    result_id: Optional[str] = None

    result_text: Optional[str] = None


class ToolCallToolCallUnionMember5Input(BaseModel):
    command: str

    connectors: List[str]

    working_dir: Optional[str] = None


class ToolCallToolCallUnionMember5(BaseModel):
    input: ToolCallToolCallUnionMember5Input

    name: Literal["RunBash"]

    result_id: Optional[str] = None

    result_text: Optional[str] = None


class ToolCallToolCallUnionMember6Input(BaseModel):
    code: str

    connectors: List[str]

    working_dir: Optional[str] = None


class ToolCallToolCallUnionMember6(BaseModel):
    input: ToolCallToolCallUnionMember6Input

    name: Literal["RunPython"]

    result_id: Optional[str] = None

    result_text: Optional[str] = None


class ToolCallToolCallUnionMember7Input(BaseModel):
    description: str

    title: str


class ToolCallToolCallUnionMember7(BaseModel):
    input: ToolCallToolCallUnionMember7Input

    name: Literal["IssueFound"]

    result_id: Optional[str] = None

    result_text: Optional[str] = None


class ToolCallToolCallUnionMember8Input(BaseModel):
    name: str

    description: Optional[str] = None

    notes: Optional[str] = None


class ToolCallToolCallUnionMember8(BaseModel):
    input: ToolCallToolCallUnionMember8Input

    name: Literal["CreateTable"]

    result_id: Optional[str] = None

    result_text: Optional[str] = None


class ToolCallToolCallUnionMember9Input(BaseModel):
    column_name: str

    column_type: str

    table_name: str

    notes: Optional[str] = None


class ToolCallToolCallUnionMember9(BaseModel):
    input: ToolCallToolCallUnionMember9Input

    name: Literal["AddColumn"]

    result_id: Optional[str] = None

    result_text: Optional[str] = None


class ToolCallToolCallUnionMember10Input(BaseModel):
    endpoint: str

    name: str

    description: Optional[str] = None

    notes: Optional[str] = None


class ToolCallToolCallUnionMember10(BaseModel):
    input: ToolCallToolCallUnionMember10Input

    name: Literal["CreateApiResource"]

    result_id: Optional[str] = None

    result_text: Optional[str] = None


class ToolCallToolCallUnionMember11Input(BaseModel):
    key: str

    value: str


class ToolCallToolCallUnionMember11(BaseModel):
    input: ToolCallToolCallUnionMember11Input

    name: Literal["SaveMemory"]

    result_id: Optional[str] = None

    result_text: Optional[str] = None


ToolCallToolCall: TypeAlias = Union[
    ToolCallToolCallUnionMember0,
    ToolCallToolCallUnionMember1,
    ToolCallToolCallUnionMember2,
    ToolCallToolCallUnionMember3,
    ToolCallToolCallUnionMember4,
    ToolCallToolCallUnionMember5,
    ToolCallToolCallUnionMember6,
    ToolCallToolCallUnionMember7,
    ToolCallToolCallUnionMember8,
    ToolCallToolCallUnionMember9,
    ToolCallToolCallUnionMember10,
    ToolCallToolCallUnionMember11,
]


class ToolCall(BaseModel):
    tool_call: ToolCallToolCall = FieldInfo(alias="ToolCall")


class QuestionQuestion(BaseModel):
    complete: bool

    content: str


class Question(BaseModel):
    question: QuestionQuestion = FieldInfo(alias="Question")


class InternalErrorInternalError(BaseModel):
    message: str


class InternalError(BaseModel):
    internal_error: InternalErrorInternalError = FieldInfo(alias="InternalError")


ChatEvent: TypeAlias = Union[TextMessage, Thinking, File, Action, Connector, ToolCall, Question, InternalError]
