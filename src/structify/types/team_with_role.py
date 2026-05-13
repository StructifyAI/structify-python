# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .team import Team
from .team_role import TeamRole
from .team_subscription_status import TeamSubscriptionStatus

__all__ = ["TeamWithRole"]


class TeamWithRole(Team):
    managed_team_count: int
    """Number of teams this membership manages.

    Zero for the common case; positive when the membership belongs to a managing
    team. Frontends use this to decide whether to expose the scoped admin teams view
    without a separate membership-level lookup.
    """

    max_seats: int

    role: TeamRole

    subscription_status: TeamSubscriptionStatus
