# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel
from .workflow_session_node import WorkflowSessionNode

__all__ = ["GetNodeResponse"]


class GetNodeResponse(BaseModel):
    node: WorkflowSessionNode
