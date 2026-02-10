# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["UpdateSeatsOverrideResponse"]


class UpdateSeatsOverrideResponse(BaseModel):
    team_id: str

    seats_override: Optional[int] = None
