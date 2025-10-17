# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel
from .connector_table_descriptor import ConnectorTableDescriptor

__all__ = ["ConnectorRelationalDatabaseDescriptor"]


class ConnectorRelationalDatabaseDescriptor(BaseModel):
    tables: List[ConnectorTableDescriptor]
    """List of tables in the database"""
