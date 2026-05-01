# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo
from .set_access_action import SetAccessAction

__all__ = ["TeamSetAccessParams"]


class TeamSetAccessParams(TypedDict, total=False):
    action: Required[SetAccessAction]

    team_id: Required[str]

    expires_at: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]
    """Cutoff for the SuperAdmin membership.

    `None` means no expiry — useful for permanent admin staffing. Ignored when
    `action = Revoke`.
    """
