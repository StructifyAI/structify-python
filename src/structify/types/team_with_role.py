# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .team import Team
from .team_role import TeamRole
from .team_subscription_status import TeamSubscriptionStatus

__all__ = ["TeamWithRole"]


class TeamWithRole(Team):
    role: TeamRole

    subscription_status: TeamSubscriptionStatus
