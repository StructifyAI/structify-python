# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["SelectTeamResponse"]


class SelectTeamResponse(BaseModel):
    api_token: str

    success: bool
