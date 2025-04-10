# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from .._utils import PropertyInfo

__all__ = ["DatasetViewRelationshipsParams", "SortBy", "SortByColID", "SortByColIDUserDefinedColumn"]


class DatasetViewRelationshipsParams(TypedDict, total=False):
    dataset: Required[str]

    name: Required[str]

    job_id: Optional[str]

    last_updated: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]

    limit: int

    offset: int

    sort_by: SortBy


class SortByColIDUserDefinedColumn(TypedDict, total=False):
    user_defined_column: Required[str]


SortByColID: TypeAlias = Union[SortByColIDUserDefinedColumn, Literal["creation_time"]]


class SortBy(TypedDict, total=False):
    col_id: Required[SortByColID]

    sort: Required[Literal["asc", "desc"]]
