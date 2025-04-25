# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Required, TypedDict

__all__ = ["StructureJobStatusParams", "Job"]


class StructureJobStatusParams(TypedDict, total=False):
    job: Required[Job]


class Job(TypedDict, total=False):
    dataset_name: Optional[str]

    job_ids: Optional[List[str]]
