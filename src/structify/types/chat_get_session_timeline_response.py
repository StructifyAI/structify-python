# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["ChatGetSessionTimelineResponse", "Message", "MessageStreamChunk"]


class MessageStreamChunk(BaseModel):
    """Entry for stream chunk logging - stored as JSONB array on chat_message"""

    chunk_type: str

    content: str

    model: Optional[str] = None


class Message(BaseModel):
    id: str

    chat_session_id: str

    content: str

    created_at: datetime

    role: str

    timestamp: datetime

    cache_creation_tokens: Optional[int] = None

    cache_read_tokens: Optional[int] = None

    content_proto: Optional[object] = None

    git_hash: Optional[str] = None

    input_tokens: Optional[int] = None

    output_tokens: Optional[int] = None

    previous_message_id: Optional[str] = None

    slack_channel_id: Optional[str] = None

    slack_message_ts: Optional[str] = None

    slack_thread_ts: Optional[str] = None

    stream_chunks: Optional[List[MessageStreamChunk]] = None

    teams_channel_id: Optional[str] = None

    teams_conversation_id: Optional[str] = None

    teams_message_id: Optional[str] = None


class ChatGetSessionTimelineResponse(BaseModel):
    """Response structure for getting session timeline"""

    messages: List[Message]
