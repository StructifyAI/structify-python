# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

__all__ = ["GrantCreditsResponse"]


class GrantCreditsResponse(BaseModel):
    amount: int

    grant_id: str

    team_id: str
