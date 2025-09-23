# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["WorkflowSession"]


class WorkflowSession(BaseModel):
    id: str

    chat_session_id: str

    dag_ready: bool

    updated_at: datetime

    created_at: Optional[datetime] = None

    dag_ready_at: Optional[datetime] = None

    error_message: Optional[str] = None

    error_traceback: Optional[str] = None

    workflow_schedule_id: Optional[str] = None
