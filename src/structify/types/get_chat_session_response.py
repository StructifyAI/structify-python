# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel
from .chat_event import ChatEvent
from .chat_visibility import ChatVisibility
from .chat_session_role import ChatSessionRole

__all__ = ["GetChatSessionResponse", "Session", "SessionCommit", "SessionMessage"]


class SessionCommit(BaseModel):
    id: str

    chat_session_id: str

    commit_hash: str

    created_at: datetime


class SessionMessage(BaseModel):
    """Model-layer message representation - streamlined for LLM transmission"""

    content: ChatEvent
    """
    Events in a chat session timeline, including messages and unified tool
    calls/results
    """

    message_id: str

    role: Literal["user", "system", "assistant"]

    timestamp: datetime


class Session(BaseModel):
    id: str

    commits: List[SessionCommit]

    created_at: datetime

    git_application_token: str

    is_favorite: bool

    messages: List[SessionMessage]

    team_id: str

    title: str

    updated_at: datetime

    user_message_needed: bool

    user_role: ChatSessionRole

    visibility: ChatVisibility

    latest_workflow_session_id: Optional[str] = None

    name: Optional[str] = None

    project_id: Optional[str] = None

    workflow_schedule_id: Optional[str] = None


class GetChatSessionResponse(BaseModel):
    """Response for getting a chat session"""

    session: Session
