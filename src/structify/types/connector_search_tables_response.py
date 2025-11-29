# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel

__all__ = [
    "ConnectorSearchTablesResponse",
    "RankedResult",
    "RankedResultColumn",
    "RankedResultTable",
    "RankedResultTableColumn",
    "RawResult",
    "RawResultColumn",
    "RawResultTable",
    "RawResultTableColumn",
    "RerankScore",
]


class RankedResultColumn(BaseModel):
    name: str
    """Name of the column"""

    type: str
    """SQL type of the column (e.g., "VARCHAR(255)", "INTEGER") or API field type"""

    notes: Optional[str] = None
    """Additional notes about the column"""


class RankedResultTableColumn(BaseModel):
    name: str
    """Name of the column"""

    type: str
    """SQL type of the column (e.g., "VARCHAR(255)", "INTEGER") or API field type"""

    notes: Optional[str] = None
    """Additional notes about the column"""


class RankedResultTable(BaseModel):
    id: str

    columns: List[RankedResultTableColumn]
    """List of columns in this table/resource"""

    name: str
    """Name of the table or resource"""

    description: Optional[str] = None
    """Optional description"""

    endpoint: Optional[str] = None
    """API endpoint (None for relational DB tables, Some for API resources)"""

    notes: Optional[str] = None
    """Optional notes"""


class RankedResult(BaseModel):
    columns: List[RankedResultColumn]

    database_name: str

    schema_name: str

    table: RankedResultTable
    """Represents a table (for relational databases) or resource (for APIs)"""


class RawResultColumn(BaseModel):
    name: str
    """Name of the column"""

    type: str
    """SQL type of the column (e.g., "VARCHAR(255)", "INTEGER") or API field type"""

    notes: Optional[str] = None
    """Additional notes about the column"""


class RawResultTableColumn(BaseModel):
    name: str
    """Name of the column"""

    type: str
    """SQL type of the column (e.g., "VARCHAR(255)", "INTEGER") or API field type"""

    notes: Optional[str] = None
    """Additional notes about the column"""


class RawResultTable(BaseModel):
    id: str

    columns: List[RawResultTableColumn]
    """List of columns in this table/resource"""

    name: str
    """Name of the table or resource"""

    description: Optional[str] = None
    """Optional description"""

    endpoint: Optional[str] = None
    """API endpoint (None for relational DB tables, Some for API resources)"""

    notes: Optional[str] = None
    """Optional notes"""


class RawResult(BaseModel):
    columns: List[RawResultColumn]

    database_name: str

    schema_name: str

    table: RawResultTable
    """Represents a table (for relational databases) or resource (for APIs)"""


class RerankScore(BaseModel):
    index: int

    relevance_score: float

    text: Optional[str] = None


class ConnectorSearchTablesResponse(BaseModel):
    ranked_results: List[RankedResult]

    raw_results: List[RawResult]

    rerank_scores: List[RerankScore]
