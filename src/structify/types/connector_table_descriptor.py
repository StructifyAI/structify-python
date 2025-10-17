# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .connector_column_descriptor import ConnectorColumnDescriptor

__all__ = ["ConnectorTableDescriptor"]


class ConnectorTableDescriptor(BaseModel):
    columns: List[ConnectorColumnDescriptor]
    """List of columns in this table"""

    name: str
    """Name of the table"""

    description: Optional[str] = None
    """Optional description of what this table contains"""

    notes: Optional[str] = None
    """Optional notes about the table (e.g., constraints, indexes, relationships)"""
