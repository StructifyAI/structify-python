# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from .._models import BaseModel

__all__ = ["EntityListJobsResponse", "EntityListJobsResponseItem"]


class EntityListJobsResponseItem(BaseModel):
    id: int

    created_at: datetime

    dataset_id: object

    parameters: object

    status: Literal["Queued", "Running", "Completed", "Failed"]

    user_id: object

    message: Optional[str] = None

    plan_id: Optional[int] = None

    reason: Optional[str] = None

    report_on_complete: Optional[bool] = None

    run_started_time: Optional[datetime] = None
    """What time did the job start running?"""


EntityListJobsResponse: TypeAlias = List[EntityListJobsResponseItem]
