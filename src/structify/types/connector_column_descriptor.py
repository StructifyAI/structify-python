# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["ConnectorColumnDescriptor"]


class ConnectorColumnDescriptor(BaseModel):
    name: str
    """Name of the column"""

    type: str
    """SQL type of the column (e.g., "VARCHAR(255)", "INTEGER", "TIMESTAMP")"""

    notes: Optional[str] = None
    """
    Additional notes about the column (e.g., "NOT NULL", "PRIMARY KEY", "UNIQUE",
    constraints)
    """
