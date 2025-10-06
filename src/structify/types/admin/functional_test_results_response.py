# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional

from ..._models import BaseModel

__all__ = ["FunctionalTestResultsResponse", "Result"]


class Result(BaseModel):
    chat_session_id: str

    results: Dict[str, object]

    sample_name: str


class FunctionalTestResultsResponse(BaseModel):
    results: List[Result]

    functional_test_id: Optional[str] = None

    sample_name: Optional[str] = None
