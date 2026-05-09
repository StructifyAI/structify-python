# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from ..._models import BaseModel

__all__ = ["JobUpdateConcurrencyResponse"]


class JobUpdateConcurrencyResponse(BaseModel):
    id: int

    updated_at: datetime

    max_connector_explore_jobs: Optional[int] = None

    max_derive_jobs: Optional[int] = None

    max_match_jobs: Optional[int] = None

    max_pdf_jobs: Optional[int] = None

    max_scrape_jobs: Optional[int] = None

    max_total_jobs: Optional[int] = None

    max_web_jobs: Optional[int] = None
