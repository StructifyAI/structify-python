# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, TypedDict

from .id import ID

__all__ = ["WorkflowJobsParams"]


class WorkflowJobsParams(TypedDict, total=False):
    workflow_id: Required[ID]

    group_id: Optional[str]

    status: Optional[Literal["Queued", "Running", "Completed", "Failed"]]

    step_id: Optional[str]
