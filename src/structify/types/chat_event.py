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
    "CodeProject",
    "CodeProjectCodeProject",
    "CodeProjectCodeProjectAttributes",
    "DeleteFile",
    "DeleteFileDeleteFile",
    "MoveFile",
    "MoveFileMoveFile",
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


class ThinkingThinking(BaseModel):
    content: str


class Thinking(BaseModel):
    thinking: ThinkingThinking = FieldInfo(alias="Thinking")


class FileFile(BaseModel):
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


class CodeProjectCodeProjectAttributes(BaseModel):
    id: Optional[str] = None

    badge: Optional[str] = None

    label: Optional[str] = None

    version: Optional[str] = None


class CodeProjectCodeProject(BaseModel):
    attributes: CodeProjectCodeProjectAttributes
    """CodeProject attributes"""


class CodeProject(BaseModel):
    code_project: CodeProjectCodeProject = FieldInfo(alias="CodeProject")


class DeleteFileDeleteFile(BaseModel):
    file: str


class DeleteFile(BaseModel):
    delete_file: DeleteFileDeleteFile = FieldInfo(alias="DeleteFile")


class MoveFileMoveFile(BaseModel):
    file: str

    new_path: str


class MoveFile(BaseModel):
    move_file: MoveFileMoveFile = FieldInfo(alias="MoveFile")


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


ChatEvent: TypeAlias = Union[
    TextMessage, Thinking, File, Action, Connector, CodeProject, DeleteFile, MoveFile, ToolCall
]
