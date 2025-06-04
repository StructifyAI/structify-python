# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from datetime import datetime

from .._models import BaseModel

__all__ = ["ChatSessionWithMessages", "Message"]


class Message(BaseModel):
    id: str

    chat_session_id: str

    content: str

    created_at: datetime

    role: str

    timestamp: datetime


class ChatSessionWithMessages(BaseModel):
    id: str

    created_at: datetime

    messages: List[Message]

    updated_at: datetime

    user_id: str
