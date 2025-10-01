# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["UserAddCreditsParams"]


class UserAddCreditsParams(TypedDict, total=False):
    credit_amount: Required[int]

    user_email: Required[str]

    source_type: Optional[str]

    valid_for_days: Optional[int]
