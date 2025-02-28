# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import TypeAlias

from .._models import BaseModel

__all__ = ["EntityListJobsResponse", "EntityListJobsResponseItem"]


class EntityListJobsResponseItem(BaseModel):
    id: str

    creation_time: datetime

    status: Optional[object] = None

    message: Optional[str] = None

    reason: Optional[str] = None

    report_on_complete: Optional[bool] = None

    run_started_time: Optional[datetime] = None
    """What time did the job start running?"""


EntityListJobsResponse: TypeAlias = List[EntityListJobsResponseItem]
