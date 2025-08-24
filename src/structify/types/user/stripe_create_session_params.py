# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["StripeCreateSessionParams"]


class StripeCreateSessionParams(TypedDict, total=False):
    credits: Required[int]
    """Amount in cents (i64)"""

    origin: Required[str]

    team_id: Required[str]
