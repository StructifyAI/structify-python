# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .workflow_param import WorkflowParam

__all__ = ["WorkflowCreateParams"]


class WorkflowCreateParams(TypedDict, total=False):
    dataset_name: Required[str]

    workflow: Required[WorkflowParam]
