# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from ..._models import BaseModel

__all__ = ["HumanLlmGetQueuedJobsResponse", "HumanLlmGetQueuedJobsResponseItem"]


class HumanLlmGetQueuedJobsResponseItem(BaseModel):
    id: str

    creation_time: datetime

    status: Literal["Queued", "Running", "Completed", "Failed"]

    message: Optional[str] = None

    report_on_complete: Optional[bool] = None

    run_started_time: Optional[datetime] = None
    """What time did the job start running?"""


HumanLlmGetQueuedJobsResponse: TypeAlias = List[HumanLlmGetQueuedJobsResponseItem]