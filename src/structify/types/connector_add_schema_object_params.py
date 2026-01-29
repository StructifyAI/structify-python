# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict

__all__ = ["ConnectorAddSchemaObjectParams", "Variant0", "Variant1", "Variant2", "Variant3"]


class Variant0(TypedDict, total=False):
    name: Required[str]

    type: Required[Literal["database"]]

    description: Optional[str]

    notes: Optional[str]


class Variant1(TypedDict, total=False):
    database_id: Required[str]

    name: Required[str]

    type: Required[Literal["schema"]]

    description: Optional[str]

    notes: Optional[str]


class Variant2(TypedDict, total=False):
    name: Required[str]

    schema_id: Required[str]

    type: Required[Literal["table"]]

    description: Optional[str]

    endpoint: Optional[str]

    notes: Optional[str]


class Variant3(TypedDict, total=False):
    column_type: Required[str]

    name: Required[str]

    table_id: Required[str]

    type: Required[Literal["column"]]

    notes: Optional[str]


ConnectorAddSchemaObjectParams: TypeAlias = Union[Variant0, Variant1, Variant2, Variant3]
