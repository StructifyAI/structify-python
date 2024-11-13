# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from .human_llm_metadata import HumanLlmMetadata

__all__ = ["HumanLlmGetJobsResponse", "HumanLlmGetJobsResponseItem"]


class HumanLlmGetJobsResponseItem(HumanLlmMetadata):
    id: str

    creation_time: datetime

    status: Literal["Queued", "Running", "Completed", "Failed"]

    message: Optional[str] = None

    report_on_complete: Optional[bool] = None

    run_started_time: Optional[datetime] = None
    """What time did the job start running?"""


HumanLlmGetJobsResponse: TypeAlias = List[List[HumanLlmGetJobsResponseItem]]
