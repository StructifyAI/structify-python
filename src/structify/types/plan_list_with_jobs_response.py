# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from .plan import Plan
from .._models import BaseModel

__all__ = ["PlanListWithJobsResponse", "Job"]


class Job(BaseModel):
    id: str

    created_at: datetime

    dataset_id: str

    status: Literal["Queued", "Running", "Completed", "Failed"]

    user_id: str

    message: Optional[str] = None
    """A message about the status of the job at completion"""

    parameters: Optional[object] = None

    plan_id: Optional[str] = None

    reason: Optional[str] = None
    """A reason for the job's existence"""

    run_started_time: Optional[datetime] = None
    """What time did the job start running?"""


class PlanListWithJobsResponse(BaseModel):
    created_at: datetime

    jobs: List[Job]

    plan: Plan

    plan_id: str

    status: Literal["Queued", "Running", "Completed", "Failed", "Paused"]

    step: int

    updated_at: datetime
