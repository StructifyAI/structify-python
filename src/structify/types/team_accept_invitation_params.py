# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["TeamAcceptInvitationParams"]


class TeamAcceptInvitationParams(TypedDict, total=False):
    token: Required[str]

    supabase_user_id: Optional[str]
