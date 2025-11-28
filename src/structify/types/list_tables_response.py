# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel
from .connector_table_info import ConnectorTableInfo

__all__ = ["ListTablesResponse"]


class ListTablesResponse(BaseModel):
    tables: List[ConnectorTableInfo]
