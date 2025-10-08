# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

__all__ = ["CancelSubscriptionResponse"]


class CancelSubscriptionResponse(BaseModel):
    canceled: bool

    team_id: str
