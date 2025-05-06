# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .id import ID
from .workflow_param import WorkflowParam

__all__ = ["WorkflowUpdateParams"]


class WorkflowUpdateParams(TypedDict, total=False):
    dataset_name: Required[str]

    workflow: Required[WorkflowParam]

    workflow_id: Required[ID]
