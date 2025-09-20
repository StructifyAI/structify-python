# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .team import Team
from .._models import BaseModel
from .team_subscription_status import TeamSubscriptionStatus

__all__ = ["GetTeamResponse"]


class GetTeamResponse(BaseModel):
    subscription_status: TeamSubscriptionStatus

    team: Team
