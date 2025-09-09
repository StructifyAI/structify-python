# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from .._models import BaseModel
from .chat_session_role import ChatSessionRole

__all__ = ["ListChatSessionsResponse", "Session"]


class Session(BaseModel):
    id: str

    created_at: datetime

    is_favorite: bool

    is_public: bool

    project_id: str

    title: str

    updated_at: datetime

    user_role: ChatSessionRole

    name: Optional[str] = None

    owner_email: Optional[str] = None


class ListChatSessionsResponse(BaseModel):
    sessions: List[Session]
