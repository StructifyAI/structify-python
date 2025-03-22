# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from datetime import datetime
from typing_extensions import Literal, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["PlanListParams"]


class PlanListParams(TypedDict, total=False):
    created_since: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]

    limit: int

    offset: int

    status: Optional[Literal["Queued", "Running", "Completed", "Failed", "Paused"]]

    updated_since: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]
