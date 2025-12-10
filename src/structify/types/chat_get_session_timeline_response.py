# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, Annotated, TypeAlias

from .._utils import PropertyInfo
from .._models import BaseModel

__all__ = [
    "ChatGetSessionTimelineResponse",
    "Timeline",
    "TimelineMessage",
    "TimelineMessageStreamChunk",
    "TimelineGitCommit",
]


class TimelineMessageStreamChunk(BaseModel):
    """Entry for stream chunk logging - stored as JSONB array on chat_message"""

    chunk_type: str

    content: str


class TimelineMessage(BaseModel):
    id: str

    chat_session_id: str

    content: str

    created_at: datetime

    role: str

    timestamp: datetime

    type: Literal["Message"]

    content_proto: Optional[object] = None

    git_commit_id: Optional[str] = None

    slack_channel_id: Optional[str] = None

    slack_message_ts: Optional[str] = None

    slack_thread_ts: Optional[str] = None

    stream_chunks: Optional[List[TimelineMessageStreamChunk]] = None


class TimelineGitCommit(BaseModel):
    id: str

    chat_session_id: str

    commit_hash: str

    created_at: datetime

    type: Literal["GitCommit"]


Timeline: TypeAlias = Annotated[Union[TimelineMessage, TimelineGitCommit], PropertyInfo(discriminator="type")]


class ChatGetSessionTimelineResponse(BaseModel):
    """Response structure for getting session timeline"""

    timeline: List[Timeline]
    """Chronologically sorted list of messages and commits"""
