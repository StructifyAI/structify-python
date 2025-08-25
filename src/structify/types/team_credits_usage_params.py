# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from datetime import datetime
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo
from .granularity import Granularity

__all__ = ["TeamCreditsUsageParams"]


class TeamCreditsUsageParams(TypedDict, total=False):
    end: Required[Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]]
    """End time exclusive (UTC)"""

    granularity: Required[Granularity]
    """hour | day | week | month"""

    start: Required[Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]]
    """Start time inclusive (UTC)"""

    token: Optional[str]
    """Optional token ID to filter by"""
