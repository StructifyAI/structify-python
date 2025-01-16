# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["UserGetCreditsParams"]


class UserGetCreditsParams(TypedDict, total=False):
    user_email: Required[str]

    user_token: Required[str]
