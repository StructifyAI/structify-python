# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

__all__ = ["CreateSubscriptionResponse"]


class CreateSubscriptionResponse(BaseModel):
    is_active: bool

    subscription_tier: str

    team_id: str
