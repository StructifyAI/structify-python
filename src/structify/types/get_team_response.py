# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .team import Team
from .._models import BaseModel

__all__ = ["GetTeamResponse"]


class GetTeamResponse(BaseModel):
    team: Team
