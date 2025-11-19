# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel

__all__ = ["LlmInformationStore", "Database", "DatabaseSchema", "DatabaseSchemaTable", "DatabaseSchemaTableColumn"]


class DatabaseSchemaTableColumn(BaseModel):
    name: str
    """Name of the column"""

    type: str
    """SQL type of the column (e.g., "VARCHAR(255)", "INTEGER") or API field type"""

    notes: Optional[str] = None
    """Additional notes about the column"""


class DatabaseSchemaTable(BaseModel):
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
    name: str

    tables: List[DatabaseSchemaTable]

    description: Optional[str] = None

    notes: Optional[str] = None


class Database(BaseModel):
    name: str

    schemas: List[DatabaseSchema]

    description: Optional[str] = None

    notes: Optional[str] = None


class LlmInformationStore(BaseModel):
    databases: List[Database]
    """List of databases in this connector"""

    uses_default_hierarchy: bool
    """
    Whether this store uses default auto-generated database/schema names (i.e.,
    database and schema names match the connector name). When true, UIs should hide
    the database/schema hierarchy. When false, UIs should show the full database →
    schema → table hierarchy.
    """
