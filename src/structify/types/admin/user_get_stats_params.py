# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from datetime import datetime
from typing_extensions import Literal, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["UserGetStatsParams"]


class UserGetStatsParams(TypedDict, total=False):
    bucket: Literal["Second", "Minute", "Hour", "Day", "Week", "Month", "Quarter", "Year", "Decade"]

    end_date: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]

    start_date: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]

    user_email: Optional[str]

    user_token: Optional[str]
