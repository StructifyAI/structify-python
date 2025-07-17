# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime

from .._models import BaseModel

__all__ = ["WorkflowSessionEdge"]


class WorkflowSessionEdge(BaseModel):
    id: str

    created_at: datetime

    session_id: str

    source_node_id: str

    target_node_id: str
