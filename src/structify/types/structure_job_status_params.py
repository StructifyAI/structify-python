# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

from .._types import SequenceNotStr

__all__ = ["StructureJobStatusParams", "Job"]


class StructureJobStatusParams(TypedDict, total=False):
    job: Required[Job]


class Job(TypedDict, total=False):
    dataset_name: Optional[str]

    job_ids: Optional[SequenceNotStr[str]]
