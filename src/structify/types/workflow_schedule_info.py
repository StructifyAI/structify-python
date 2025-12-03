# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["WorkflowScheduleInfo"]


class WorkflowScheduleInfo(BaseModel):
    id: str

    chat_session_id: str

    name: str

    paused: bool

    cron_schedule: Optional[str] = None

    git_commit_hash: Optional[str] = None

    next_run_time: Optional[str] = None
