# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .team_management_relationship import TeamManagementRelationship

__all__ = ["ManagementRelationshipDetail"]


class ManagementRelationshipDetail(TeamManagementRelationship):
    """
    A management relationship plus the human-readable names of both teams,
    so admin UIs don't need a separate lookup to render labels.
    """

    managed_team_name: str

    manager_team_name: str
