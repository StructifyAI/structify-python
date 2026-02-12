# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["TeamUpdateParams", "DaytonaCredentials", "WorkflowBucket"]


class TeamUpdateParams(TypedDict, total=False):
    daytona_credentials: Optional[DaytonaCredentials]

    description: Optional[str]

    name: Optional[str]

    pipedream_project_id: Optional[str]

    slack_bot_token: Optional[str]

    slack_team_icon: Optional[str]

    slack_team_id: Optional[str]

    slack_team_name: Optional[str]

    teams_app_id: Optional[str]

    teams_app_password: Optional[str]

    teams_tenant_id: Optional[str]

    workflow_bucket: Optional[WorkflowBucket]


class DaytonaCredentials(TypedDict, total=False):
    api_key: Optional[str]

    api_url: Optional[str]


class WorkflowBucket(TypedDict, total=False):
    bucket_url: Required[str]

    gcp_credentials_json: Optional[str]
