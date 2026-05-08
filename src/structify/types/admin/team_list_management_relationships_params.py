# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["TeamListManagementRelationshipsParams"]


class TeamListManagementRelationshipsParams(TypedDict, total=False):
    manager_team_id: Optional[str]
    """Optional filter: only return relationships whose manager is this team."""
