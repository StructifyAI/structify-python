# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from .._models import BaseModel
from .chat_visibility import ChatVisibility

__all__ = ["ChatSession"]


class ChatSession(BaseModel):
    id: str

    created_at: datetime

    ephemeral: bool

    git_application_token: str

    slack_completion_notified: bool

    team_id: str

    updated_at: datetime

    visibility: ChatVisibility

    config_proto: Optional[object] = None

    name: Optional[str] = None

    project_id: Optional[str] = None

    slack_channel_id: Optional[str] = None

    slack_team_id: Optional[str] = None

    slack_thread_ts: Optional[str] = None
