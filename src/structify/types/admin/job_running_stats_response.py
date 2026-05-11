# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel

__all__ = ["JobRunningStatsResponse", "ByMembership", "ByType"]


class ByMembership(BaseModel):
    membership_id: str

    queued: int

    running: int


class ByType(BaseModel):
    count: int

    job_type: str


class JobRunningStatsResponse(BaseModel):
    by_membership: List[ByMembership]

    by_type: List[ByType]

    completed_last_hour: int

    failed_last_hour: int

    total_queued: int

    total_running: int
