# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel
from .user_team import UserTeam

__all__ = ["ListMembersResponse"]


class ListMembersResponse(BaseModel):
    members: List[UserTeam]
