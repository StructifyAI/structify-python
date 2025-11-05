# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime

from .._models import BaseModel
from .chat_session_role import ChatSessionRole

__all__ = ["ProjectMember"]


class ProjectMember(BaseModel):
    created_at: datetime

    email: str

    role: ChatSessionRole

    updated_at: datetime

    user_id: str
