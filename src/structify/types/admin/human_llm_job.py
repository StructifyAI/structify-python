# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from ..id import ID
from ..._models import BaseModel

__all__ = ["HumanLlmJob", "Job", "Metadata"]


class Job(BaseModel):
    id: str

    created_at: datetime

    dataset_id: str

    job_type: Literal["Web", "Pdf", "Derive", "Scrape"]

    selected_next_workflow_step: bool

    status: Literal["Queued", "Running", "Completed", "Failed"]

    user_id: str

    message: Optional[str] = None
    """A message about the status of the job at completion"""

    parameters: Optional[object] = None
    """Proto for JobInput"""

    reason: Optional[str] = None
    """A reason for the job's existence"""

    run_started_time: Optional[datetime] = None
    """What time did the job start running?"""

    run_time_milliseconds: Optional[int] = None

    workflow_group_id: Optional[str] = None

    workflow_id: Optional[ID] = None

    workflow_step_id: Optional[str] = None


class Metadata(BaseModel):
    id: str

    description: str

    job_id: str

    entity_id: Optional[str] = None

    property_name: Optional[str] = None


class HumanLlmJob(BaseModel):
    job: Job

    metadata: Metadata
