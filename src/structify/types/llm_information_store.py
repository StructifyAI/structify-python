# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import Literal, Annotated, TypeAlias

from .._utils import PropertyInfo
from .._models import BaseModel
from .connector_column_descriptor import ConnectorColumnDescriptor
from .connector_relational_database_descriptor import ConnectorRelationalDatabaseDescriptor

__all__ = ["LlmInformationStore", "RelationalDatabase", "APITabular", "APITabularResource", "Other"]


class RelationalDatabase(ConnectorRelationalDatabaseDescriptor):
    type: Literal["relational_database"]


class APITabularResource(BaseModel):
    columns: List[ConnectorColumnDescriptor]
    """List of columns (properties/fields in the API resource)"""

    endpoint: str
    """
    API endpoint for this resource (e.g., "/crm/v3/objects/contacts",
    "/rest/api/3/issue")
    """

    name: str
    """API name of the resource (e.g., "contacts", "issues", "records")"""

    description: Optional[str] = None
    """Optional description"""

    notes: Optional[str] = None
    """Optional notes (associations, usage patterns, etc.)"""


class APITabular(BaseModel):
    resources: List[APITabularResource]
    """List of resources (similar to tables/objects)"""

    type: Literal["api_tabular"]


class Other(BaseModel):
    data: str

    type: Literal["other"]


LlmInformationStore: TypeAlias = Annotated[
    Union[RelationalDatabase, APITabular, Other], PropertyInfo(discriminator="type")
]
