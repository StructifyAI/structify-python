# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["UserCreateTestTokenParams"]


class UserCreateTestTokenParams(TypedDict, total=False):
    credits: int

    is_admin: bool
