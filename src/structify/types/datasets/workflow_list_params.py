# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["WorkflowListParams"]


class WorkflowListParams(TypedDict, total=False):
    dataset_name: Optional[str]
