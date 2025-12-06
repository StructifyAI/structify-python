# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["RefreshSessionResponse"]


class RefreshSessionResponse(BaseModel):
    expires_at: str

    refresh_token: str

    refresh_token_expires_at: str

    session_token: str
