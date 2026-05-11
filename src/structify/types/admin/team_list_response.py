# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel
from .admin_teams_list_response import AdminTeamsListResponse

__all__ = ["TeamListResponse"]


class TeamListResponse(BaseModel):
    items: List[AdminTeamsListResponse]

    total_count: int
