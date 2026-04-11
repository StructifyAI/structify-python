# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from datetime import datetime
from typing_extensions import TypeAlias

from .._models import BaseModel

__all__ = ["ChatListInputFilesResponse", "ChatListInputFilesResponseItem"]


class ChatListInputFilesResponseItem(BaseModel):
    chat_session_id: str

    content_type: str

    created_at: datetime

    file_size: int

    filename: str


ChatListInputFilesResponse: TypeAlias = List[ChatListInputFilesResponseItem]
