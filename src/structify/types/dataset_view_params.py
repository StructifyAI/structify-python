# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["DatasetViewParams"]


class DatasetViewParams(TypedDict, total=False):
    dataset_name: Required[str]

    requested_type: Required[Literal["Entities", "Relationships"]]

    limit: int

    offset: int

    relationship_name: Optional[str]

    table_name: Optional[str]
