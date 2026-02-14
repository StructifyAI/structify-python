# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, TypedDict

__all__ = ["JobListParams"]


class JobListParams(TypedDict, total=False):
    job_type: Optional[Literal["Web", "Pdf", "Derive", "Scrape", "Match", "ConnectorExplore"]]

    limit: int

    offset: int

    status: Optional[Literal["Queued", "Running", "Completed", "Failed"]]

    user_id: Optional[str]
