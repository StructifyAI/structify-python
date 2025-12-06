# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["UserRefreshParams"]


class UserRefreshParams(TypedDict, total=False):
    refresh_token: Required[str]

    session_token: Required[str]
