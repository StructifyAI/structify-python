# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime

from ..._models import BaseModel

__all__ = ["TeamManagementRelationship"]


class TeamManagementRelationship(BaseModel):
    id: str

    created_at: datetime

    managed_team_id: str

    manager_team_id: str

    updated_at: datetime
