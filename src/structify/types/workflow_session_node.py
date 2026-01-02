# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from .._models import BaseModel
from .workflow_node_execution_status import WorkflowNodeExecutionStatus

__all__ = ["WorkflowSessionNode"]


class WorkflowSessionNode(BaseModel):
    id: str

    code_md5_hash: str

    docstring: str

    execution_status: WorkflowNodeExecutionStatus

    function_name: str

    node_index: int

    node_name: str

    reviewed: bool

    session_id: str

    updated_at: datetime

    code: Optional[str] = None

    confirmation_status: Optional[str] = None

    connector_id: Optional[str] = None

    created_at: Optional[datetime] = None

    error_message: Optional[str] = None

    error_traceback: Optional[str] = None

    estimated_cost: Optional[int] = None

    execution_time_ms: Optional[int] = None

    input_row_count: Optional[int] = None

    original_node: Optional[str] = None

    output_blob_name: Optional[str] = None

    output_schema: Optional[object] = None

    progress: Optional[object] = None

    visualization_output: Optional[object] = None
