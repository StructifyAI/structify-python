# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import TypeAlias

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .tool_result import ToolResult
from .tool_invocation import ToolInvocation

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
    "Question",
    "QuestionQuestion",
    "InternalError",
    "InternalErrorInternalError",
    "ReviewRequest",
    "ReviewRequestReviewRequest",
    "ReviewRequestReviewRequestNodeSummary",
    "AttachedFile",
    "AttachedFileAttachedFile",
    "ConnectorRequest",
    "ConnectorRequestConnectorRequest",
    "UserInterrupted",
    "IssueFound",
    "IssueFoundIssueFound",
]


class TextMessageTextMessage(BaseModel):
    message: str


class TextMessage(BaseModel):
    text_message: TextMessageTextMessage = FieldInfo(alias="TextMessage")


class ThinkingThinking(BaseModel):
    block_id: int

    complete: bool

    content: str


class Thinking(BaseModel):
    thinking: ThinkingThinking = FieldInfo(alias="Thinking")


class FileFile(BaseModel):
    """
    The file event can't be serialized to the database safely without the content.
    When streaming, we start with the path only, then add the content as we go.
    """

    block_id: int

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
    """Action definition"""

    description: str

    name: str


class ActionAction(BaseModel):
    actions: List[ActionActionAction]

    block_id: int

    complete: bool


class Action(BaseModel):
    action: ActionAction = FieldInfo(alias="Action")


class ConnectorConnector(BaseModel):
    env_vars: List[str]

    name: str

    description: Optional[str] = None


class Connector(BaseModel):
    connector: ConnectorConnector = FieldInfo(alias="Connector")


class ToolCallToolCall(BaseModel):
    block_id: int

    complete: bool

    invocation: ToolInvocation

    tool_result: ToolResult


class ToolCall(BaseModel):
    tool_call: ToolCallToolCall = FieldInfo(alias="ToolCall")


class QuestionQuestion(BaseModel):
    block_id: int

    complete: bool

    content: str

    options: List[str]


class Question(BaseModel):
    question: QuestionQuestion = FieldInfo(alias="Question")


class InternalErrorInternalError(BaseModel):
    message: str


class InternalError(BaseModel):
    internal_error: InternalErrorInternalError = FieldInfo(alias="InternalError")


class ReviewRequestReviewRequestNodeSummary(BaseModel):
    in_dashboard: bool

    name: str

    data_preview: Optional[str] = None

    image: Optional[object] = None


class ReviewRequestReviewRequest(BaseModel):
    node_summaries: List[ReviewRequestReviewRequestNodeSummary]


class ReviewRequest(BaseModel):
    review_request: ReviewRequestReviewRequest = FieldInfo(alias="ReviewRequest")


class AttachedFileAttachedFile(BaseModel):
    path: str

    image_bytes: Optional[object] = None


class AttachedFile(BaseModel):
    attached_file: AttachedFileAttachedFile = FieldInfo(alias="AttachedFile")


class ConnectorRequestConnectorRequest(BaseModel):
    connector_id: str


class ConnectorRequest(BaseModel):
    connector_request: ConnectorRequestConnectorRequest = FieldInfo(alias="ConnectorRequest")


class UserInterrupted(BaseModel):
    user_interrupted: object = FieldInfo(alias="UserInterrupted")


class IssueFoundIssueFound(BaseModel):
    admin_override: bool

    description: str

    title: str


class IssueFound(BaseModel):
    issue_found: IssueFoundIssueFound = FieldInfo(alias="IssueFound")


ChatEvent: TypeAlias = Union[
    TextMessage,
    Thinking,
    File,
    Action,
    Connector,
    ToolCall,
    Question,
    InternalError,
    ReviewRequest,
    AttachedFile,
    ConnectorRequest,
    UserInterrupted,
    IssueFound,
]
