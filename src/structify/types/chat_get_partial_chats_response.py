# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import TypeAlias

from .._models import BaseModel
from .chat_prompt import ChatPrompt

__all__ = ["ChatGetPartialChatsResponse", "ChatGetPartialChatsResponseItem"]


class ChatGetPartialChatsResponseItem(BaseModel):
    chat_prompt: ChatPrompt

    created_at: datetime

    message_id: Optional[str] = None


ChatGetPartialChatsResponse: TypeAlias = List[ChatGetPartialChatsResponseItem]
