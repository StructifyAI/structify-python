# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel
from .execution_step import ExecutionStep

__all__ = ["JobGetResponse", "Job"]


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


class JobGetResponse(BaseModel):
    job: Job

    steps: List[ExecutionStep]
