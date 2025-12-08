# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["TeamUpdateParams"]


class TeamUpdateParams(TypedDict, total=False):
    datahub_host: Optional[str]

    datahub_token: Optional[str]

    description: Optional[str]

    name: Optional[str]

    pipedream_project_id: Optional[str]

    slack_bot_token: Optional[str]

    slack_team_icon: Optional[str]

    slack_team_id: Optional[str]

    slack_team_name: Optional[str]
