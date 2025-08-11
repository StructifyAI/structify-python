# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["WorkflowScheduleUpdateParams"]


class WorkflowScheduleUpdateParams(TypedDict, total=False):
    cron_schedule: Optional[str]

    git_commit_hash: Optional[str]

    name: Optional[str]
