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
    "ToolCallToolCallUnionMember12",
    "ToolCallToolCallUnionMember12Input",
    "ToolCallToolCallUnionMember13",
    "ToolCallToolCallUnionMember13Input",
    "ToolCallToolCallUnionMember14",
    "ToolCallToolCallUnionMember14Input",
    "ToolCallToolCallUnionMember15",
    "ToolCallToolCallUnionMember15Input",
    "ToolCallToolCallUnionMember16",
    "ToolCallToolCallUnionMember16Input",
    "ToolCallToolCallUnionMember17",
    "ToolCallToolCallUnionMember17Input",
    "ToolCallToolCallUnionMember18",
    "ToolCallToolCallUnionMember18Input",
    "Question",
    "QuestionQuestion",
    "InternalError",
    "InternalErrorInternalError",
    "ReviewRequest",
    "ReviewRequestReviewRequest",
    "ReviewRequestReviewRequestNodeSummary",
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


class ToolCallToolCallUnionMember0Input(BaseModel):
    query: str


class ToolCallToolCallUnionMember0(BaseModel):
    input: ToolCallToolCallUnionMember0Input

    name: Literal["WebSearch"]

    block_id: Optional[int] = None

    complete: Optional[bool] = None

    result_image: Optional[object] = None

    result_text: Optional[str] = None


class ToolCallToolCallUnionMember1Input(BaseModel):
    url: str


class ToolCallToolCallUnionMember1(BaseModel):
    input: ToolCallToolCallUnionMember1Input

    name: Literal["WebNavigate"]

    block_id: Optional[int] = None

    complete: Optional[bool] = None

    result_image: Optional[object] = None

    result_text: Optional[str] = None


class ToolCallToolCallUnionMember2Input(BaseModel):
    step_name: str


class ToolCallToolCallUnionMember2(BaseModel):
    input: ToolCallToolCallUnionMember2Input

    name: Literal["InspectStep"]

    block_id: Optional[int] = None

    complete: Optional[bool] = None

    result_image: Optional[object] = None

    result_text: Optional[str] = None


class ToolCallToolCallUnionMember3Input(BaseModel):
    end_line: int

    node_function_name: str

    start_line: int

    log_type: Optional[str] = None


class ToolCallToolCallUnionMember3(BaseModel):
    input: ToolCallToolCallUnionMember3Input

    name: Literal["ReadNodeLogs"]

    block_id: Optional[int] = None

    complete: Optional[bool] = None

    result_image: Optional[object] = None

    result_text: Optional[str] = None


class ToolCallToolCallUnionMember4Input(BaseModel):
    file: str


class ToolCallToolCallUnionMember4(BaseModel):
    input: ToolCallToolCallUnionMember4Input

    name: Literal["DeleteFile"]

    block_id: Optional[int] = None

    complete: Optional[bool] = None

    result_image: Optional[object] = None

    result_text: Optional[str] = None


class ToolCallToolCallUnionMember5Input(BaseModel):
    file: str

    new_path: str


class ToolCallToolCallUnionMember5(BaseModel):
    input: ToolCallToolCallUnionMember5Input

    name: Literal["MoveFile"]

    block_id: Optional[int] = None

    complete: Optional[bool] = None

    result_image: Optional[object] = None

    result_text: Optional[str] = None


class ToolCallToolCallUnionMember6Input(BaseModel):
    command: str

    connector: Optional[str] = None

    working_dir: Optional[str] = None


class ToolCallToolCallUnionMember6(BaseModel):
    input: ToolCallToolCallUnionMember6Input

    name: Literal["RunBash"]

    block_id: Optional[int] = None

    complete: Optional[bool] = None

    result_image: Optional[object] = None

    result_text: Optional[str] = None


class ToolCallToolCallUnionMember7Input(BaseModel):
    code: str

    connector: Optional[str] = None

    working_dir: Optional[str] = None


class ToolCallToolCallUnionMember7(BaseModel):
    input: ToolCallToolCallUnionMember7Input

    name: Literal["RunPython"]

    block_id: Optional[int] = None

    complete: Optional[bool] = None

    result_image: Optional[object] = None

    result_text: Optional[str] = None


class ToolCallToolCallUnionMember8Input(BaseModel):
    description: str

    title: str


class ToolCallToolCallUnionMember8(BaseModel):
    input: ToolCallToolCallUnionMember8Input

    name: Literal["IssueFound"]

    block_id: Optional[int] = None

    complete: Optional[bool] = None

    result_image: Optional[object] = None

    result_text: Optional[str] = None


class ToolCallToolCallUnionMember9Input(BaseModel):
    name: str

    description: Optional[str] = None

    notes: Optional[str] = None


class ToolCallToolCallUnionMember9(BaseModel):
    input: ToolCallToolCallUnionMember9Input

    name: Literal["SaveDatabase"]

    block_id: Optional[int] = None

    complete: Optional[bool] = None

    result_image: Optional[object] = None

    result_text: Optional[str] = None


class ToolCallToolCallUnionMember10Input(BaseModel):
    name: str

    description: Optional[str] = None

    notes: Optional[str] = None


class ToolCallToolCallUnionMember10(BaseModel):
    input: ToolCallToolCallUnionMember10Input

    name: Literal["SaveSchema"]

    block_id: Optional[int] = None

    complete: Optional[bool] = None

    result_image: Optional[object] = None

    result_text: Optional[str] = None


class ToolCallToolCallUnionMember11Input(BaseModel):
    name: str

    description: Optional[str] = None

    notes: Optional[str] = None

    tag: Optional[str] = None


class ToolCallToolCallUnionMember11(BaseModel):
    input: ToolCallToolCallUnionMember11Input

    name: Literal["SaveTable"]

    block_id: Optional[int] = None

    complete: Optional[bool] = None

    result_image: Optional[object] = None

    result_text: Optional[str] = None


class ToolCallToolCallUnionMember12Input(BaseModel):
    column_name: str

    column_type: str

    notes: Optional[str] = None


class ToolCallToolCallUnionMember12(BaseModel):
    input: ToolCallToolCallUnionMember12Input

    name: Literal["SaveColumn"]

    block_id: Optional[int] = None

    complete: Optional[bool] = None

    result_image: Optional[object] = None

    result_text: Optional[str] = None


class ToolCallToolCallUnionMember13Input(BaseModel):
    endpoint: str

    name: str

    description: Optional[str] = None

    notes: Optional[str] = None


class ToolCallToolCallUnionMember13(BaseModel):
    input: ToolCallToolCallUnionMember13Input

    name: Literal["SaveApiResource"]

    block_id: Optional[int] = None

    complete: Optional[bool] = None

    result_image: Optional[object] = None

    result_text: Optional[str] = None


class ToolCallToolCallUnionMember14Input(BaseModel):
    key: str

    value: str


class ToolCallToolCallUnionMember14(BaseModel):
    input: ToolCallToolCallUnionMember14Input

    name: Literal["SaveMemory"]

    block_id: Optional[int] = None

    complete: Optional[bool] = None

    result_image: Optional[object] = None

    result_text: Optional[str] = None


class ToolCallToolCallUnionMember15Input(BaseModel):
    query: str

    wiki_tag: Optional[str] = None


class ToolCallToolCallUnionMember15(BaseModel):
    input: ToolCallToolCallUnionMember15Input

    name: Literal["SearchConnectorTables"]

    block_id: Optional[int] = None

    complete: Optional[bool] = None

    result_image: Optional[object] = None

    result_text: Optional[str] = None


class ToolCallToolCallUnionMember16Input(BaseModel):
    question: str

    table_name: str

    column_name: Optional[str] = None


class ToolCallToolCallUnionMember16(BaseModel):
    input: ToolCallToolCallUnionMember16Input

    name: Literal["RequestClarification"]

    block_id: Optional[int] = None

    complete: Optional[bool] = None

    result_image: Optional[object] = None

    result_text: Optional[str] = None


class ToolCallToolCallUnionMember17Input(BaseModel):
    package_name: str

    version_spec: Optional[str] = None


class ToolCallToolCallUnionMember17(BaseModel):
    input: ToolCallToolCallUnionMember17Input

    name: Literal["AddDependency"]

    block_id: Optional[int] = None

    complete: Optional[bool] = None

    result_image: Optional[object] = None

    result_text: Optional[str] = None


class ToolCallToolCallUnionMember18Input(BaseModel):
    node_ids: List[str]


class ToolCallToolCallUnionMember18(BaseModel):
    input: ToolCallToolCallUnionMember18Input

    name: Literal["SelectData"]

    block_id: Optional[int] = None

    complete: Optional[bool] = None

    result_image: Optional[object] = None

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
    ToolCallToolCallUnionMember12,
    ToolCallToolCallUnionMember13,
    ToolCallToolCallUnionMember14,
    ToolCallToolCallUnionMember15,
    ToolCallToolCallUnionMember16,
    ToolCallToolCallUnionMember17,
    ToolCallToolCallUnionMember18,
]


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
    name: str

    data_preview: Optional[str] = None

    image: Optional[object] = None


class ReviewRequestReviewRequest(BaseModel):
    node_summaries: List[ReviewRequestReviewRequestNodeSummary]


class ReviewRequest(BaseModel):
    review_request: ReviewRequestReviewRequest = FieldInfo(alias="ReviewRequest")


ChatEvent: TypeAlias = Union[
    TextMessage, Thinking, File, Action, Connector, ToolCall, Question, InternalError, ReviewRequest
]
