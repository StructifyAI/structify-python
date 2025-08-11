# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["WorkflowScheduleCreateParams"]


class WorkflowScheduleCreateParams(TypedDict, total=False):
    git_commit_hash: Required[str]

    name: Required[str]

    cron_schedule: Optional[str]
