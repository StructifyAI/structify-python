# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict
from datetime import datetime

from .._models import BaseModel

__all__ = ["CreditsUsageTimeseriesPoint"]


class CreditsUsageTimeseriesPoint(BaseModel):
    bucket_start: datetime

    groups: Dict[str, int]
