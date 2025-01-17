# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["UserGetCreditsParams"]


class UserGetCreditsParams(TypedDict, total=False):
    user_email: Optional[str]

    user_token: Optional[str]
