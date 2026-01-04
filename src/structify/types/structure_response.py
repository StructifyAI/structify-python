# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

__all__ = ["StructureResponse"]


class StructureResponse(TypedDict, total=False):
    dataset_name: Required[str]

    table_name: Required[str]

    job_ids: Required[Iterable[str]]
