# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["NextActionGetTrainingDataParams"]


class NextActionGetTrainingDataParams(TypedDict, total=False):
    job_id: Optional[str]

    limit: int

    offset: int

    status: Optional[str]
