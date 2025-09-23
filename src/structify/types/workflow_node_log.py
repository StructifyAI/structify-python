# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime

from .._models import BaseModel

__all__ = ["WorkflowNodeLog"]


class WorkflowNodeLog(BaseModel):
    id: str

    content: str

    is_stderr: bool

    node_id: str

    timestamp: datetime
