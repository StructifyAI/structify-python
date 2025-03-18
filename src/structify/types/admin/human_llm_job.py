# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["HumanLlmJob", "Job", "Metadata"]


class Job(BaseModel):
    id: str

    creation_time: datetime

    status: Literal["Queued", "Running", "Completed", "Failed"]

    message: Optional[str] = None

    reason: Optional[str] = None

    report_on_complete: Optional[bool] = None

    run_started_time: Optional[datetime] = None
    """What time did the job start running?"""


class Metadata(BaseModel):
    dataset_name: str

    property_name: str

    user_email: str

    entity_name: Optional[str] = None


class HumanLlmJob(BaseModel):
    job: Job

    metadata: Metadata
