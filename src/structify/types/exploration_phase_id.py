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
    """First phase: discovering all databases in the connector"""

    connector_id: str

    type: Literal["discover_databases"]


class DiscoverSchemas(BaseModel):
    """Second phase: discovering all schemas in a database"""

    database_id: str

    database_name: str

    type: Literal["discover_schemas"]


class DiscoverTables(BaseModel):
    """Third phase: discovering all tables in a schema"""

    schema_id: str

    schema_name: str

    type: Literal["discover_tables"]


class DiscoverColumns(BaseModel):
    """Fourth phase: discovering columns for a specific table"""

    table_id: str

    table_name: str

    type: Literal["discover_columns"]


class DiscoverAPIResources(BaseModel):
    """Initial phase: discovering all API resources"""

    connector_id: str

    type: Literal["discover_api_resources"]


class DiscoverAPIFields(BaseModel):
    """Second phase: discovering fields for a specific API resource"""

    resource_name: str

    table_id: str

    type: Literal["discover_api_fields"]


ExplorationPhaseID: TypeAlias = Annotated[
    Union[DiscoverDatabases, DiscoverSchemas, DiscoverTables, DiscoverColumns, DiscoverAPIResources, DiscoverAPIFields],
    PropertyInfo(discriminator="type"),
]
