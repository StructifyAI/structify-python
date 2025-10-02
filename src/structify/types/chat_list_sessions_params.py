# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["ChatListSessionsParams"]


class ChatListSessionsParams(TypedDict, total=False):
    project_id: Required[str]
    """Project ID to filter chat sessions"""

    team_id: Required[str]
    """Team ID to filter chat sessions"""

    limit: Optional[int]
    """Maximum number of sessions to return (default: 50)"""
