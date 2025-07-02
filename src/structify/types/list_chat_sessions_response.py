# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from datetime import datetime

from .._models import BaseModel

__all__ = ["ListChatSessionsResponse", "Session"]


class Session(BaseModel):
    id: str

    created_at: datetime

    project_id: str

    title: str

    user_id: str


class ListChatSessionsResponse(BaseModel):
    sessions: List[Session]
