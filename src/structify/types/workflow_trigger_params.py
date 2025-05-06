# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Required, TypedDict

from .id import ID

__all__ = ["WorkflowTriggerParams"]


class WorkflowTriggerParams(TypedDict, total=False):
    entity_ids: Required[List[str]]

    workflow_id: Required[ID]
