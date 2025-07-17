# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from .._models import BaseModel
from .workflow_node_execution_status import WorkflowNodeExecutionStatus

__all__ = ["WorkflowSessionNode"]


class WorkflowSessionNode(BaseModel):
    id: str

    docstring: str

    execution_status: WorkflowNodeExecutionStatus

    function_name: str

    node_index: int

    node_name: str

    session_id: str

    updated_at: datetime

    created_at: Optional[datetime] = None

    error_message: Optional[str] = None

    error_traceback: Optional[str] = None

    execution_time_ms: Optional[int] = None

    output_data: Optional[object] = None

    output_schema: Optional[object] = None
