# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel

__all__ = ["JobRunningStatsResponse", "ByType", "ByUser"]


class ByType(BaseModel):
    count: int

    job_type: str


class ByUser(BaseModel):
    email: str

    queued: int

    running: int

    user_id: str


class JobRunningStatsResponse(BaseModel):
    by_type: List[ByType]

    by_user: List[ByUser]

    completed_last_hour: int

    failed_last_hour: int

    total_queued: int

    total_running: int
