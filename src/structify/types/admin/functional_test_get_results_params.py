# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["FunctionalTestGetResultsParams"]


class FunctionalTestGetResultsParams(TypedDict, total=False):
    functional_test_id: Optional[str]

    sample_name: Optional[str]
