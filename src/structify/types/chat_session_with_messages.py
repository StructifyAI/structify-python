# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from .._models import BaseModel
from .chat_visibility import ChatVisibility
from .chat_session_role import ChatSessionRole

__all__ = ["ChatSessionWithMessages", "Commit", "Message", "MessageStreamChunk"]


class Commit(BaseModel):
    id: str

    chat_session_id: str

    commit_hash: str

    created_at: datetime


class MessageStreamChunk(BaseModel):
    """Entry for stream chunk logging - stored as JSONB array on chat_message"""

    chunk_type: str

    content: str


class Message(BaseModel):
    id: str

    chat_session_id: str

    content: str

    created_at: datetime

    role: str

    timestamp: datetime

    content_proto: Optional[object] = None

    git_commit_id: Optional[str] = None

    slack_channel_id: Optional[str] = None

    slack_message_ts: Optional[str] = None

    slack_thread_ts: Optional[str] = None

    stream_chunks: Optional[List[MessageStreamChunk]] = None


class ChatSessionWithMessages(BaseModel):
    id: str

    commits: List[Commit]

    created_at: datetime

    git_application_token: str

    is_favorite: bool

    messages: List[Message]

    team_id: str

    updated_at: datetime

    user_message_needed: bool

    user_role: ChatSessionRole

    visibility: ChatVisibility

    latest_workflow_session_id: Optional[str] = None

    name: Optional[str] = None

    project_id: Optional[str] = None
