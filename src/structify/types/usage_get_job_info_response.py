# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from datetime import datetime

from .._models import BaseModel

__all__ = ["UsageGetJobInfoResponse"]


class UsageGetJobInfoResponse(BaseModel):
    images: List[str]

    job_id: str

    job_status: object

    run_time: datetime

    summary_text: str
