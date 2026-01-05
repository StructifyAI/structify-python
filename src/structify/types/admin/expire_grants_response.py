# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

__all__ = ["ExpireGrantsResponse"]


class ExpireGrantsResponse(BaseModel):
    expired_count: int

    team_id: str
