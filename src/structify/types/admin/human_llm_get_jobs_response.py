# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from ..._models import BaseModel

__all__ = ["HumanLlmGetJobsResponse", "HumanLlmGetJobsResponseItem"]


class HumanLlmGetJobsResponseItem(BaseModel):
    id: str

    creation_time: datetime

    entity_name: str

    property_name: str

    status: Literal["Queued", "Running", "Completed", "Failed"]

    user_email: str

    message: Optional[str] = None

    report_on_complete: Optional[bool] = None

    run_started_time: Optional[datetime] = None
    """What time did the job start running?"""


HumanLlmGetJobsResponse: TypeAlias = List[List[HumanLlmGetJobsResponseItem]]
