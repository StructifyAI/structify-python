# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel
from .execution_step import ExecutionStep

__all__ = ["JobGetResponse", "Job"]


class Job(BaseModel):
    id: str

    creation_time: datetime

    status: Literal["Queued", "Running", "Completed", "Failed"]

    run_started_time: Optional[datetime] = None
    """What time did the job start running?"""


class JobGetResponse(BaseModel):
    job: Job

    steps: List[ExecutionStep]
