# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime

from ..._models import BaseModel

__all__ = ["ImpersonateResponse"]


class ImpersonateResponse(BaseModel):
    expires_at: datetime

    refresh_token: str

    refresh_token_expires_at: datetime

    session_token: str
