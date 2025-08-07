# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from datetime import datetime

from .._models import BaseModel
from .chat_session_role import ChatSessionRole

__all__ = ["ListCollaboratorsResponse", "User"]


class User(BaseModel):
    created_at: datetime

    email: str

    role: ChatSessionRole

    updated_at: datetime

    user_id: str


class ListCollaboratorsResponse(BaseModel):
    users: List[User]
