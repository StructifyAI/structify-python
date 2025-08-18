# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .workflow_session_edge import WorkflowSessionEdge
from .workflow_session_node import WorkflowSessionNode

__all__ = ["WorkflowDag"]


class WorkflowDag(BaseModel):
    edges: List[WorkflowSessionEdge]

    nodes: List[WorkflowSessionNode]

    session_id: str

    error: Optional[str] = None

    error_traceback: Optional[str] = None
