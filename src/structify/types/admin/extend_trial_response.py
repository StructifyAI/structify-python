# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime

from ..._models import BaseModel

__all__ = ["ExtendTrialResponse"]


class ExtendTrialResponse(BaseModel):
    grant_id: str

    new_expires_at: datetime

    team_id: str
