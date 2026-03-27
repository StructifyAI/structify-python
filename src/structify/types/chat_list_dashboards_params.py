# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["ChatListDashboardsParams"]


class ChatListDashboardsParams(TypedDict, total=False):
    commit_hash: Optional[str]
    """Optional commit hash. If omitted, uses the chat session latest commit."""
