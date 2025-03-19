# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from datetime import datetime
from typing_extensions import Literal, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["TrainingDatasetGetLabellerStatsParams"]


class TrainingDatasetGetLabellerStatsParams(TypedDict, total=False):
    end_date: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]

    labeled_status: Literal["None", "SuspiciousOnly", "VerifiedOnly"]

    max_prop_count: Optional[int]

    start_date: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]

    time_bucket: Literal["Second", "Minute", "Hour", "Day", "Week", "Month", "Quarter", "Year", "Decade"]
