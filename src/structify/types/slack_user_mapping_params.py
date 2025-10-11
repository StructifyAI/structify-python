# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["SlackUserMappingParams"]


class SlackUserMappingParams(TypedDict, total=False):
    slack_bot_token: Required[str]

    slack_team_id: Required[str]

    slack_user_id: Required[str]

    slack_username: Optional[str]
