# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel
from .credits_usage_timeseries_point import CreditsUsageTimeseriesPoint

__all__ = ["CreditsUsageResponse"]


class CreditsUsageResponse(BaseModel):
    timeseries: List[CreditsUsageTimeseriesPoint]

    total_credits_added: int

    total_spent: int
