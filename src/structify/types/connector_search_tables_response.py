# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import TypeAlias

from .._models import BaseModel

__all__ = [
    "ConnectorSearchTablesResponse",
    "ConnectorSearchTablesResponseItem",
    "ConnectorSearchTablesResponseItemColumn",
    "ConnectorSearchTablesResponseItemTable",
    "ConnectorSearchTablesResponseItemTableColumn",
]


class ConnectorSearchTablesResponseItemColumn(BaseModel):
    """Represents a column in a table or API resource"""

    id: str

    name: str
    """Name of the column"""

    type: str
    """SQL type of the column (e.g., "VARCHAR(255)", "INTEGER") or API field type"""

    notes: Optional[str] = None
    """Additional notes about the column"""


class ConnectorSearchTablesResponseItemTableColumn(BaseModel):
    """Represents a column in a table or API resource"""

    id: str

    name: str
    """Name of the column"""

    type: str
    """SQL type of the column (e.g., "VARCHAR(255)", "INTEGER") or API field type"""

    notes: Optional[str] = None
    """Additional notes about the column"""


class ConnectorSearchTablesResponseItemTable(BaseModel):
    """Represents a table (for relational databases) or resource (for APIs)"""

    id: str

    columns: List[ConnectorSearchTablesResponseItemTableColumn]
    """List of columns in this table/resource"""

    name: str
    """Name of the table or resource"""

    description: Optional[str] = None
    """Optional description"""

    endpoint: Optional[str] = None
    """API endpoint (None for relational DB tables, Some for API resources)"""

    notes: Optional[str] = None
    """Optional notes"""


class ConnectorSearchTablesResponseItem(BaseModel):
    """Result struct for connector table search"""

    columns: List[ConnectorSearchTablesResponseItemColumn]

    database_name: str

    schema_name: str

    score: float
    """Search relevance score (0 = exact match, higher = less relevant)"""

    table: ConnectorSearchTablesResponseItemTable
    """Represents a table (for relational databases) or resource (for APIs)"""


ConnectorSearchTablesResponse: TypeAlias = List[ConnectorSearchTablesResponseItem]
