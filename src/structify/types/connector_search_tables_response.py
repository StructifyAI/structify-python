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
    """Represents a column in a table or API resource"""

    name: str
    """Name of the column"""

    type: str
    """SQL type of the column (e.g., "VARCHAR(255)", "INTEGER") or API field type"""

    notes: Optional[str] = None
    """Additional notes about the column"""


class RankedResultTableColumn(BaseModel):
    """Represents a column in a table or API resource"""

    name: str
    """Name of the column"""

    type: str
    """SQL type of the column (e.g., "VARCHAR(255)", "INTEGER") or API field type"""

    notes: Optional[str] = None
    """Additional notes about the column"""


class RankedResultTable(BaseModel):
    """Represents a table (for relational databases) or resource (for APIs)"""

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
    """Result struct for connector table search"""

    columns: List[RankedResultColumn]

    database_name: str

    schema_name: str

    score: float
    """Search relevance score (0 = exact match, higher = less relevant)"""

    table: RankedResultTable
    """Represents a table (for relational databases) or resource (for APIs)"""


class RawResultColumn(BaseModel):
    """Represents a column in a table or API resource"""

    name: str
    """Name of the column"""

    type: str
    """SQL type of the column (e.g., "VARCHAR(255)", "INTEGER") or API field type"""

    notes: Optional[str] = None
    """Additional notes about the column"""


class RawResultTableColumn(BaseModel):
    """Represents a column in a table or API resource"""

    name: str
    """Name of the column"""

    type: str
    """SQL type of the column (e.g., "VARCHAR(255)", "INTEGER") or API field type"""

    notes: Optional[str] = None
    """Additional notes about the column"""


class RawResultTable(BaseModel):
    """Represents a table (for relational databases) or resource (for APIs)"""

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
    """Result struct for connector table search"""

    columns: List[RawResultColumn]

    database_name: str

    schema_name: str

    score: float
    """Search relevance score (0 = exact match, higher = less relevant)"""

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
