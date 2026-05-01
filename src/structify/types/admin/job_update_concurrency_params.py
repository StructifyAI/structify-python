# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["JobUpdateConcurrencyParams"]


class JobUpdateConcurrencyParams(TypedDict, total=False):
    max_connector_explore_jobs: Optional[int]

    max_derive_jobs: Optional[int]

    max_match_jobs: Optional[int]

    max_pdf_jobs: Optional[int]

    max_scrape_jobs: Optional[int]

    max_total_jobs: Optional[int]

    max_web_jobs: Optional[int]
