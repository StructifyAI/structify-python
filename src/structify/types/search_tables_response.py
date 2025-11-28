# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel
from .table_mention import TableMention

__all__ = ["SearchTablesResponse"]


class SearchTablesResponse(BaseModel):
    results: List[TableMention]
    """List of table mentions for autocomplete"""
