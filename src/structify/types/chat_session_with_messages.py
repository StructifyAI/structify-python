# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from .._models import BaseModel
from .chat_session_role import ChatSessionRole

__all__ = ["ChatSessionWithMessages", "Commit", "Message"]


class Commit(BaseModel):
    id: str

    chat_session_id: str

    commit_hash: str

    created_at: datetime


class Message(BaseModel):
    id: str

    chat_session_id: str

    content: str

    created_at: datetime

    role: str

    timestamp: datetime

    git_commit_id: Optional[str] = None


class ChatSessionWithMessages(BaseModel):
    id: str

    commits: List[Commit]

    created_at: datetime

    git_application_token: str

    is_favorite: bool

    is_public: bool
    """Whether the chat session is public"""

    messages: List[Message]

    project_id: str

    updated_at: datetime

    user_role: ChatSessionRole

    latest_workflow_session_id: Optional[str] = None

    name: Optional[str] = None
