# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime

from .._models import BaseModel

__all__ = ["AddChatMessageResponse", "Message"]


class Message(BaseModel):
    id: str

    chat_session_id: str

    content: str

    created_at: datetime

    role: str

    timestamp: datetime


class AddChatMessageResponse(BaseModel):
    message: Message
