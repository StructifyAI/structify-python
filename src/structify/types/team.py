# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["Team"]


class Team(BaseModel):
    id: str

    created_at: datetime

    name: str

    updated_at: datetime

    description: Optional[str] = None

    pipedream_project_id: Optional[str] = None

    slack_team_icon: Optional[str] = None

    slack_team_id: Optional[str] = None

    slack_team_name: Optional[str] = None

    teams_app_id: Optional[str] = None

    teams_service_url: Optional[str] = None

    teams_tenant_id: Optional[str] = None
