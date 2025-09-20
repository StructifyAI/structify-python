# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, Annotated, TypeAlias

from .._utils import PropertyInfo
from .._models import BaseModel

__all__ = ["ChatGetSessionTimelineResponse", "Timeline", "TimelineMessage", "TimelineGitCommit"]


class TimelineMessage(BaseModel):
    id: str

    chat_session_id: str

    content: str

    created_at: datetime

    role: str

    timestamp: datetime

    type: Literal["Message"]

    git_commit_id: Optional[str] = None


class TimelineGitCommit(BaseModel):
    id: str

    chat_session_id: str

    commit_hash: str

    created_at: datetime

    type: Literal["GitCommit"]


Timeline: TypeAlias = Annotated[Union[TimelineMessage, TimelineGitCommit], PropertyInfo(discriminator="type")]


class ChatGetSessionTimelineResponse(BaseModel):
    timeline: List[Timeline]
    """Chronologically sorted list of messages and commits"""
