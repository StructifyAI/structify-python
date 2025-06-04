# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel
from .chat_session import ChatSession

__all__ = ["ListChatSessionsResponse"]


class ListChatSessionsResponse(BaseModel):
    sessions: List[ChatSession]
