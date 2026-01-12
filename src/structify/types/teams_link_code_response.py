# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime

from .._models import BaseModel

__all__ = ["TeamsLinkCodeResponse"]


class TeamsLinkCodeResponse(BaseModel):
    code: str

    expires_at: datetime
