# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel

__all__ = ["LlmInformationStore", "Database", "DatabaseSchema", "DatabaseSchemaTable", "DatabaseSchemaTableColumn"]


class DatabaseSchemaTableColumn(BaseModel):
    """Represents a column in a table or API resource"""

    name: str
    """Name of the column"""

    type: str
    """SQL type of the column (e.g., "VARCHAR(255)", "INTEGER") or API field type"""

    notes: Optional[str] = None
    """Additional notes about the column"""


class DatabaseSchemaTable(BaseModel):
    """Represents a table (for relational databases) or resource (for APIs)"""

    id: str

    columns: List[DatabaseSchemaTableColumn]
    """List of columns in this table/resource"""

    name: str
    """Name of the table or resource"""

    description: Optional[str] = None
    """Optional description"""

    endpoint: Optional[str] = None
    """API endpoint (None for relational DB tables, Some for API resources)"""

    notes: Optional[str] = None
    """Optional notes"""


class DatabaseSchema(BaseModel):
    """Schema within a database"""

    name: str

    tables: List[DatabaseSchemaTable]

    description: Optional[str] = None

    notes: Optional[str] = None


class Database(BaseModel):
    """Database within a connector"""

    name: str

    schemas: List[DatabaseSchema]

    description: Optional[str] = None

    notes: Optional[str] = None


class LlmInformationStore(BaseModel):
    """Information store for connector schema

    Hierarchical structure: Connector → Database → Schema → Table → Column
    Works for both relational databases and API-based data.
    Distinguishes between the two by presence of `endpoint` on tables:
    - Relational DB: all tables have `endpoint: None`
    - API: all tables have `endpoint: Some(...)`
    """

    databases: List[Database]
    """List of databases in this connector"""

    uses_default_hierarchy: bool
    """
    Whether this store uses default auto-generated database/schema names (i.e.,
    database and schema names match the connector name). When true, UIs should hide
    the database/schema hierarchy. When false, UIs should show the full database →
    schema → table hierarchy.
    """
