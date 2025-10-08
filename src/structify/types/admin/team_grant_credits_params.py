# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from datetime import datetime
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["TeamGrantCreditsParams"]


class TeamGrantCreditsParams(TypedDict, total=False):
    amount: Required[int]

    source_type: Required[str]

    team_id: Required[str]

    expires_at: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]

    source_ref: Optional[str]

    starts_at: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]
