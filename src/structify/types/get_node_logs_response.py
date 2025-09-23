# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel
from .workflow_node_log import WorkflowNodeLog

__all__ = ["GetNodeLogsResponse"]


class GetNodeLogsResponse(BaseModel):
    logs: List[WorkflowNodeLog]
