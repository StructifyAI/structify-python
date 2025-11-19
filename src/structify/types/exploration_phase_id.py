# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union
from typing_extensions import Literal, Annotated, TypeAlias

from .._utils import PropertyInfo
from .._models import BaseModel

__all__ = [
    "ExplorationPhaseID",
    "DiscoverDatabases",
    "DiscoverSchemas",
    "DiscoverTables",
    "DiscoverColumns",
    "DiscoverAPIResources",
    "DiscoverAPIFields",
]


class DiscoverDatabases(BaseModel):
    connector_id: str

    type: Literal["discover_databases"]


class DiscoverSchemas(BaseModel):
    database_id: str

    database_name: str

    type: Literal["discover_schemas"]


class DiscoverTables(BaseModel):
    schema_id: str

    schema_name: str

    type: Literal["discover_tables"]


class DiscoverColumns(BaseModel):
    table_id: str

    table_name: str

    type: Literal["discover_columns"]


class DiscoverAPIResources(BaseModel):
    connector_id: str

    type: Literal["discover_api_resources"]


class DiscoverAPIFields(BaseModel):
    resource_name: str

    table_id: str

    type: Literal["discover_api_fields"]


ExplorationPhaseID: TypeAlias = Annotated[
    Union[DiscoverDatabases, DiscoverSchemas, DiscoverTables, DiscoverColumns, DiscoverAPIResources, DiscoverAPIFields],
    PropertyInfo(discriminator="type"),
]
