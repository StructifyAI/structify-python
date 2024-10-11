# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["JobCancelResponse"]


class JobCancelResponse(BaseModel):
    id: str

    creation_time: datetime

    status: Literal["Queued", "Running", "Completed", "Failed"]

    message: Optional[str] = None

    run_started_time: Optional[datetime] = None
    """What time did the job start running?"""
