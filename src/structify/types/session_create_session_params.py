# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["SessionCreateSessionParams"]


class SessionCreateSessionParams(TypedDict, total=False):
    chat_session_id: Required[str]
