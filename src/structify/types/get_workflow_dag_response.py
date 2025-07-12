# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel
from .workflow_session_edge import WorkflowSessionEdge
from .workflow_session_node import WorkflowSessionNode

__all__ = ["GetWorkflowDagResponse"]


class GetWorkflowDagResponse(BaseModel):
    edges: List[WorkflowSessionEdge]

    nodes: List[WorkflowSessionNode]
