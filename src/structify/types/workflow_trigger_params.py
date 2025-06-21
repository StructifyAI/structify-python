# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Required, TypedDict

from .id import ID

__all__ = ["WorkflowTriggerParams", "StopConfig"]


class WorkflowTriggerParams(TypedDict, total=False):
    entity_ids: Required[List[str]]

    workflow_id: Required[ID]

    banned_domains: Optional[List[str]]

    stop_config: Optional[StopConfig]
    """Configuration parameters for the StopChecker"""


class StopConfig(TypedDict, total=False):
    max_steps_without_save: Required[int]

    max_errors: Optional[int]

    max_execution_time_secs: Optional[int]

    max_total_steps: Optional[int]
