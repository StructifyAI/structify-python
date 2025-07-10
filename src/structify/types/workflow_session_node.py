# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["WorkflowSessionNode"]


class WorkflowSessionNode(BaseModel):
    id: str

    node_index: int

    node_name: str

    session_id: str

    created_at: Optional[datetime] = None
