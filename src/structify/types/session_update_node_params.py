# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

from .workflow_node_execution_status import WorkflowNodeExecutionStatus

__all__ = ["SessionUpdateNodeParams"]


class SessionUpdateNodeParams(TypedDict, total=False):
    execution_status: Required[WorkflowNodeExecutionStatus]

    error_message: Optional[str]

    output_data: object
