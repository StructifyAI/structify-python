# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["TeamUpsertManagementRelationshipParams"]


class TeamUpsertManagementRelationshipParams(TypedDict, total=False):
    managed_team_id: Required[str]

    manager_team_id: Required[str]
