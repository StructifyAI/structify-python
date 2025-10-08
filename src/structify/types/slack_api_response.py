# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union, Optional
from typing_extensions import TypeAlias

from .._models import BaseModel

__all__ = ["SlackAPIResponse", "SlackChallengeResponse", "SlackEventResponse"]


class SlackChallengeResponse(BaseModel):
    challenge: str


class SlackEventResponse(BaseModel):
    ok: bool

    message: Optional[str] = None


SlackAPIResponse: TypeAlias = Union[SlackChallengeResponse, SlackEventResponse]
