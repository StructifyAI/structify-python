# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel
from .person_match import PersonMatch

__all__ = ["PeopleMatchResponse"]


class PeopleMatchResponse(BaseModel):
    is_likely_to_engage: Optional[bool] = None
    """Whether this is an exact match"""

    match_confidence: Optional[float] = None
    """Match confidence"""

    person: Optional[PersonMatch] = None
