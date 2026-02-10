# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["TeamUpdateSeatsOverrideParams"]


class TeamUpdateSeatsOverrideParams(TypedDict, total=False):
    team_id: Required[str]

    seats_override: Optional[int]
