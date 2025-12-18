# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime

from .._models import BaseModel

__all__ = ["NangoCreateSessionResponse"]


class NangoCreateSessionResponse(BaseModel):
    """A Nango connect session for the frontend SDK"""

    token: str

    expires_at: datetime
