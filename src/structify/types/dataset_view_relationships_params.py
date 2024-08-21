# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["DatasetViewRelationshipsParams"]


class DatasetViewRelationshipsParams(TypedDict, total=False):
    dataset: Required[str]

    name: Required[str]

    limit: int

    offset: int
