# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from datetime import datetime
from typing_extensions import TypeAlias

from ..._models import BaseModel

__all__ = ["UserGetStatsResponse", "UserGetStatsResponseItem"]


class UserGetStatsResponseItem(BaseModel):
    job_count: int

    period: datetime


UserGetStatsResponse: TypeAlias = List[UserGetStatsResponseItem]
