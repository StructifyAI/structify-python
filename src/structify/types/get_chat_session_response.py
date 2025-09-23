# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .chat_session_role import ChatSessionRole

__all__ = [
    "GetChatSessionResponse",
    "Session",
    "SessionCommit",
    "SessionMessage",
    "SessionMessageContent",
    "SessionMessageContentTextMessage",
    "SessionMessageContentTextMessageTextMessage",
    "SessionMessageContentThinking",
    "SessionMessageContentThinkingThinking",
    "SessionMessageContentFile",
    "SessionMessageContentFileFile",
    "SessionMessageContentAction",
    "SessionMessageContentActionAction",
    "SessionMessageContentActionActionAction",
    "SessionMessageContentConnector",
    "SessionMessageContentConnectorConnector",
    "SessionMessageContentCodeProject",
    "SessionMessageContentCodeProjectCodeProject",
    "SessionMessageContentCodeProjectCodeProjectAttributes",
    "SessionMessageContentDeleteFile",
    "SessionMessageContentDeleteFileDeleteFile",
    "SessionMessageContentMoveFile",
    "SessionMessageContentMoveFileMoveFile",
    "SessionMessageContentToolCall",
    "SessionMessageContentToolCallToolCall",
    "SessionMessageContentToolCallToolCallUnionMember0",
    "SessionMessageContentToolCallToolCallUnionMember0Input",
    "SessionMessageContentToolCallToolCallUnionMember1",
    "SessionMessageContentToolCallToolCallUnionMember1Input",
    "SessionMessageContentToolCallToolCallUnionMember2",
    "SessionMessageContentToolCallToolCallUnionMember2Input",
    "SessionMessageContentToolCallToolCallUnionMember3",
    "SessionMessageContentToolCallToolCallUnionMember3Input",
    "SessionMessageContentToolCallToolCallUnionMember4",
    "SessionMessageContentToolCallToolCallUnionMember4Input",
    "SessionMessageContentToolCallToolCallUnionMember5",
    "SessionMessageContentToolCallToolCallUnionMember5Input",
    "SessionMessageContentToolCallToolCallUnionMember6",
    "SessionMessageContentToolCallToolCallUnionMember6Input",
    "SessionMessageContentToolCallToolCallUnionMember7",
    "SessionMessageContentToolCallToolCallUnionMember7Input",
]


class SessionCommit(BaseModel):
    id: str

    chat_session_id: str

    commit_hash: str

    created_at: datetime


class SessionMessageContentTextMessageTextMessage(BaseModel):
    message: str


class SessionMessageContentTextMessage(BaseModel):
    text_message: SessionMessageContentTextMessageTextMessage = FieldInfo(alias="TextMessage")


class SessionMessageContentThinkingThinking(BaseModel):
    content: str


class SessionMessageContentThinking(BaseModel):
    thinking: SessionMessageContentThinkingThinking = FieldInfo(alias="Thinking")


class SessionMessageContentFileFile(BaseModel):
    path: str

    content: Optional[str] = None


class SessionMessageContentFile(BaseModel):
    file: SessionMessageContentFileFile = FieldInfo(alias="File")
    """
    The file event can't be serialized to the database safely without the content.
    When streaming, we start with the path only, then add the content as we go.
    """


class SessionMessageContentActionActionAction(BaseModel):
    description: str

    name: str


class SessionMessageContentActionAction(BaseModel):
    actions: List[SessionMessageContentActionActionAction]


class SessionMessageContentAction(BaseModel):
    action: SessionMessageContentActionAction = FieldInfo(alias="Action")


class SessionMessageContentConnectorConnector(BaseModel):
    env_vars: List[str]

    name: str

    description: Optional[str] = None


class SessionMessageContentConnector(BaseModel):
    connector: SessionMessageContentConnectorConnector = FieldInfo(alias="Connector")


class SessionMessageContentCodeProjectCodeProjectAttributes(BaseModel):
    id: Optional[str] = None

    badge: Optional[str] = None

    label: Optional[str] = None

    version: Optional[str] = None


class SessionMessageContentCodeProjectCodeProject(BaseModel):
    attributes: SessionMessageContentCodeProjectCodeProjectAttributes
    """CodeProject attributes"""


class SessionMessageContentCodeProject(BaseModel):
    code_project: SessionMessageContentCodeProjectCodeProject = FieldInfo(alias="CodeProject")


class SessionMessageContentDeleteFileDeleteFile(BaseModel):
    file: str


class SessionMessageContentDeleteFile(BaseModel):
    delete_file: SessionMessageContentDeleteFileDeleteFile = FieldInfo(alias="DeleteFile")


class SessionMessageContentMoveFileMoveFile(BaseModel):
    file: str

    new_path: str


class SessionMessageContentMoveFile(BaseModel):
    move_file: SessionMessageContentMoveFileMoveFile = FieldInfo(alias="MoveFile")


class SessionMessageContentToolCallToolCallUnionMember0Input(BaseModel):
    query: str


class SessionMessageContentToolCallToolCallUnionMember0(BaseModel):
    input: SessionMessageContentToolCallToolCallUnionMember0Input

    name: Literal["WebSearch"]

    result_id: Optional[str] = None

    result_text: Optional[str] = None


class SessionMessageContentToolCallToolCallUnionMember1Input(BaseModel):
    url: str


class SessionMessageContentToolCallToolCallUnionMember1(BaseModel):
    input: SessionMessageContentToolCallToolCallUnionMember1Input

    name: Literal["WebNavigate"]

    result_id: Optional[str] = None

    result_text: Optional[str] = None


class SessionMessageContentToolCallToolCallUnionMember2Input(BaseModel):
    node_function_name: str


class SessionMessageContentToolCallToolCallUnionMember2(BaseModel):
    input: SessionMessageContentToolCallToolCallUnionMember2Input

    name: Literal["InspectDAG"]

    result_id: Optional[str] = None

    result_text: Optional[str] = None


class SessionMessageContentToolCallToolCallUnionMember3Input(BaseModel):
    env_vars: List[str]

    name: str

    description: Optional[str] = None


class SessionMessageContentToolCallToolCallUnionMember3(BaseModel):
    input: SessionMessageContentToolCallToolCallUnionMember3Input

    name: Literal["Connector"]

    result_id: Optional[str] = None

    result_text: Optional[str] = None


class SessionMessageContentToolCallToolCallUnionMember4Input(BaseModel):
    file: str


class SessionMessageContentToolCallToolCallUnionMember4(BaseModel):
    input: SessionMessageContentToolCallToolCallUnionMember4Input

    name: Literal["DeleteFile"]

    result_id: Optional[str] = None

    result_text: Optional[str] = None


class SessionMessageContentToolCallToolCallUnionMember5Input(BaseModel):
    file: str

    new_path: str


class SessionMessageContentToolCallToolCallUnionMember5(BaseModel):
    input: SessionMessageContentToolCallToolCallUnionMember5Input

    name: Literal["MoveFile"]

    result_id: Optional[str] = None

    result_text: Optional[str] = None


class SessionMessageContentToolCallToolCallUnionMember6Input(BaseModel):
    command: str

    connectors: List[str]

    env: Optional[Dict[str, str]] = None

    working_dir: Optional[str] = None


class SessionMessageContentToolCallToolCallUnionMember6(BaseModel):
    input: SessionMessageContentToolCallToolCallUnionMember6Input

    name: Literal["RunBash"]

    result_id: Optional[str] = None

    result_text: Optional[str] = None


class SessionMessageContentToolCallToolCallUnionMember7Input(BaseModel):
    code: str

    connectors: List[str]

    env: Optional[Dict[str, str]] = None

    working_dir: Optional[str] = None


class SessionMessageContentToolCallToolCallUnionMember7(BaseModel):
    input: SessionMessageContentToolCallToolCallUnionMember7Input

    name: Literal["RunPython"]

    result_id: Optional[str] = None

    result_text: Optional[str] = None


SessionMessageContentToolCallToolCall: TypeAlias = Union[
    SessionMessageContentToolCallToolCallUnionMember0,
    SessionMessageContentToolCallToolCallUnionMember1,
    SessionMessageContentToolCallToolCallUnionMember2,
    SessionMessageContentToolCallToolCallUnionMember3,
    SessionMessageContentToolCallToolCallUnionMember4,
    SessionMessageContentToolCallToolCallUnionMember5,
    SessionMessageContentToolCallToolCallUnionMember6,
    SessionMessageContentToolCallToolCallUnionMember7,
]


class SessionMessageContentToolCall(BaseModel):
    tool_call: SessionMessageContentToolCallToolCall = FieldInfo(alias="ToolCall")


SessionMessageContent: TypeAlias = Union[
    SessionMessageContentTextMessage,
    SessionMessageContentThinking,
    SessionMessageContentFile,
    SessionMessageContentAction,
    SessionMessageContentConnector,
    SessionMessageContentCodeProject,
    SessionMessageContentDeleteFile,
    SessionMessageContentMoveFile,
    SessionMessageContentToolCall,
]


class SessionMessage(BaseModel):
    id: str

    chat_session_id: str

    content: SessionMessageContent
    """
    Events in a chat session timeline, including messages and unified tool
    calls/results
    """

    created_at: datetime

    role: Literal["user", "system", "assistant"]

    timestamp: datetime

    commit_hash: Optional[str] = None


class Session(BaseModel):
    id: str

    commits: List[SessionCommit]

    created_at: datetime

    git_application_token: str

    is_favorite: bool

    is_public: bool

    messages: List[SessionMessage]

    project_id: str

    title: str

    updated_at: datetime

    user_role: ChatSessionRole

    latest_workflow_session_id: Optional[str] = None

    name: Optional[str] = None


class GetChatSessionResponse(BaseModel):
    session: Session
