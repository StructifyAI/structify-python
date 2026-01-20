# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from .._models import BaseModel
from .dashboard import Dashboard
from .workflow_session_edge import WorkflowSessionEdge
from .workflow_session_node import WorkflowSessionNode

__all__ = ["WorkflowDag"]


class WorkflowDag(BaseModel):
    aborted: bool

    edges: List[WorkflowSessionEdge]

    is_ready: bool

    nodes: List[WorkflowSessionNode]

    session_id: str

    dag_ready_at: Optional[datetime] = None

    dashboard_layout: Optional[Dashboard] = None
    """
    A page is the top-level container with title/description Can contain multiple
    dashboards with different datasets
    """

    error: Optional[str] = None

    error_traceback: Optional[str] = None
