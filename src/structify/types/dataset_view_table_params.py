# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["DatasetViewTableParams"]


class DatasetViewTableParams(TypedDict, total=False):
    dataset: Required[str]

    name: Required[str]

    job_id: Optional[str]

    limit: int

    offset: int
