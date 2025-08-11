# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel
from .workflow_session import WorkflowSession

__all__ = ["GetWorkflowScheduleSessionsResponse"]


class GetWorkflowScheduleSessionsResponse(BaseModel):
    sessions: List[WorkflowSession]

    total_count: int
