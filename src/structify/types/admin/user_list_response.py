# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .user import User
from ..._models import BaseModel
from ..team_role import TeamRole

__all__ = ["UserListResponse", "UserListResponseItem", "UserListResponseItemMembership"]


class UserListResponseItemMembership(BaseModel):
    membership_id: str

    role: TeamRole

    team_id: str

    team_name: str


class UserListResponseItem(User):
    memberships: List[UserListResponseItemMembership]


UserListResponse: TypeAlias = List[UserListResponseItem]
