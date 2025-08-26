# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["HumanLlmJob", "Job", "Metadata"]


class Job(BaseModel):
    id: str

    created_at: datetime

    dataset_id: str

    job_type: Literal["Web", "Pdf", "Derive", "Scrape"]

    max_steps_without_save: int

    status: Literal["Queued", "Running", "Completed", "Failed"]

    token_id: str

    updated_at: datetime

    use_proxy: bool

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


class Metadata(BaseModel):
    id: str

    description: str

    job_id: str

    entity_id: Optional[str] = None

    property_name: Optional[str] = None


class HumanLlmJob(BaseModel):
    job: Job

    metadata: Metadata
