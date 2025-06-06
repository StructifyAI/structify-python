# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel
from .team_with_role import TeamWithRole

__all__ = ["ListTeamsResponse"]


class ListTeamsResponse(BaseModel):
    teams: List[TeamWithRole]
