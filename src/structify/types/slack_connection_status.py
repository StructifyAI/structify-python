# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["SlackConnectionStatus"]


class SlackConnectionStatus(BaseModel):
    connected: bool

    slack_team_id: Optional[str] = None

    slack_username: Optional[str] = None
