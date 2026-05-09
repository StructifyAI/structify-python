# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["ChatListSessionsParams"]


class ChatListSessionsParams(TypedDict, total=False):
    team_id: Required[str]
    """Team ID to filter chat sessions"""

    connector_id: Optional[str]
    """Connector ID to filter chat sessions that use this connector"""

    limit: Optional[int]
    """Maximum number of sessions to return (default: 50)"""

    offset: Optional[int]
    """Number of sessions to skip (default: 0)"""

    project_id: Optional[str]
    """Project ID to filter chat sessions"""

    search: Optional[str]
    """Search query to filter sessions by name (case-insensitive)"""

    sort: Optional[Literal["updated_at", "created_at", "name"]]
    """Column to sort by (default: favorites first, then `updated_at` descending)"""

    sort_desc: Optional[bool]
    """
    When `false`, sort ascending; when `true`, sort descending (default: `true` for
    timestamps, `false` for name)
    """

    tab: Optional[Literal["my_chats", "favorites", "shared", "team", "recents", "from_messaging"]]
    """Tab filter for chat sessions"""
