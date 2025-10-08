# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel
from .slack_connection_status import SlackConnectionStatus

__all__ = ["SlackOAuthResponse"]


class SlackOAuthResponse(BaseModel):
    message: str

    success: bool

    connection_status: Optional[SlackConnectionStatus] = None
