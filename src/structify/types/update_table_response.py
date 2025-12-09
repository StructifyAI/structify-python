# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel

__all__ = ["UpdateTableResponse", "Table", "TableColumn"]


class TableColumn(BaseModel):
    """Represents a column in a table or API resource"""

    name: str
    """Name of the column"""

    type: str
    """SQL type of the column (e.g., "VARCHAR(255)", "INTEGER") or API field type"""

    notes: Optional[str] = None
    """Additional notes about the column"""


class Table(BaseModel):
    """Represents a table (for relational databases) or resource (for APIs)"""

    id: str

    columns: List[TableColumn]
    """List of columns in this table/resource"""

    name: str
    """Name of the table or resource"""

    description: Optional[str] = None
    """Optional description"""

    endpoint: Optional[str] = None
    """API endpoint (None for relational DB tables, Some for API resources)"""

    notes: Optional[str] = None
    """Optional notes"""


class UpdateTableResponse(BaseModel):
    table: Table
    """Represents a table (for relational databases) or resource (for APIs)"""
