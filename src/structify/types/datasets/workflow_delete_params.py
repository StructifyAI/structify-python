# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .id import ID

__all__ = ["WorkflowDeleteParams"]


class WorkflowDeleteParams(TypedDict, total=False):
    workflow_id: Required[ID]
