# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .team_role import TeamRole

__all__ = ["TeamUpdateMemberRoleParams"]


class TeamUpdateMemberRoleParams(TypedDict, total=False):
    team_id: Required[str]

    role: Required[TeamRole]
