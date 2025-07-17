# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from .id import ID
from .._models import BaseModel
from .execution_step import ExecutionStep

__all__ = ["JobGetResponse", "Job"]


class Job(BaseModel):
    id: str

    created_at: datetime

    dataset_id: str

    job_type: Literal["Web", "Pdf", "Derive", "Scrape"]

    max_steps_without_save: int

    selected_next_workflow_step: bool

    status: Literal["Queued", "Running", "Completed", "Failed"]

    user_id: str

    max_errors: Optional[int] = None

    max_execution_time_secs: Optional[int] = None

    max_total_steps: Optional[int] = None

    message: Optional[str] = None
    """A message about the status of the job at completion"""

    node_id: Optional[str] = None

    parameters: Optional[object] = None
    """Proto for JobInput"""

    reason: Optional[str] = None
    """A reason for the job's existence"""

    run_started_time: Optional[datetime] = None
    """What time did the job start running?"""

    run_time_milliseconds: Optional[int] = None

    seeded_kg_search_term: Optional[str] = None

    workflow_group_id: Optional[str] = None

    workflow_id: Optional[ID] = None

    workflow_step_id: Optional[str] = None


class JobGetResponse(BaseModel):
    job: Job

    steps: List[ExecutionStep]
