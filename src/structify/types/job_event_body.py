# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from typing_extensions import Literal, Annotated, TypeAlias

from .._utils import PropertyInfo
from .._models import BaseModel
from .knowledge_graph import KnowledgeGraph

__all__ = [
    "JobEventBody",
    "AgentNavigated",
    "AgentSearched",
    "AgentSaved",
    "AgentExited",
    "APINetworkCaptured",
    "APIJsExecuted",
    "DerivedProperty",
    "Failed",
    "Completed",
    "CacheHit",
    "AttemptedMatch",
    "DatahubPageFetched",
    "DatahubDatabasesCreated",
    "DatahubSchemasCreated",
    "DatahubTablesProcessed",
    "DatahubEmbeddingBatch",
    "ViewedPdfPage",
]


class AgentNavigated(BaseModel):
    event_type: Literal["agent_navigated"]

    mode: Literal["visual", "text"]

    url: str


class AgentSearched(BaseModel):
    event_type: Literal["agent_searched"]

    query: str

    results: List[List[str]]


class AgentSaved(BaseModel):
    event_type: Literal["agent_saved"]

    kg: KnowledgeGraph
    """
    Knowledge graph info structured to deserialize and display in the same format
    that the LLM outputs. Also the first representation of an LLM output in the
    pipeline from raw tool output to being merged into a DB
    """

    sources: List[str]

    page: Optional[int] = None

    reason: Optional[str] = None


class AgentExited(BaseModel):
    event_type: Literal["agent_exited"]

    reason: Optional[str] = None


class APINetworkCaptured(BaseModel):
    api_candidate_count: int

    event_type: Literal["api_network_captured"]

    request_count: int

    url: str


class APIJsExecuted(BaseModel):
    code_preview: str

    event_type: Literal["api_js_executed"]

    success: bool


class DerivedProperty(BaseModel):
    event_type: Literal["derived_property"]

    property: str

    value: str


class Failed(BaseModel):
    error: str

    event_type: Literal["failed"]

    summary: Optional[str] = None


class Completed(BaseModel):
    event_type: Literal["completed"]

    message: Optional[str] = None


class CacheHit(BaseModel):
    cached_from_job_id: str

    event_type: Literal["cache_hit"]

    message: Optional[str] = None


class AttemptedMatch(BaseModel):
    candidates: List[Dict[str, Union[str, bool, float]]]

    event_type: Literal["attempted_match"]

    reason: str

    target: Dict[str, Union[str, bool, float]]

    candidate_indices: Optional[List[int]] = None

    match_idx: Optional[int] = None

    raw_text: Optional[str] = None


class DatahubPageFetched(BaseModel):
    datasets_in_page: int

    event_type: Literal["datahub_page_fetched"]

    page_num: int

    total_datasets: int


class DatahubDatabasesCreated(BaseModel):
    count: int

    event_type: Literal["datahub_databases_created"]


class DatahubSchemasCreated(BaseModel):
    count: int

    event_type: Literal["datahub_schemas_created"]


class DatahubTablesProcessed(BaseModel):
    column_lineage_count: int

    event_type: Literal["datahub_tables_processed"]

    table_lineage_count: int

    tables_created: int

    tables_failed: int

    tables_updated: int


class DatahubEmbeddingBatch(BaseModel):
    batch_num: int

    event_type: Literal["datahub_embedding_batch"]

    tables_in_batch: int

    total_batches: int


class ViewedPdfPage(BaseModel):
    event_type: Literal["viewed_pdf_page"]

    page_index: int


JobEventBody: TypeAlias = Annotated[
    Union[
        AgentNavigated,
        AgentSearched,
        AgentSaved,
        AgentExited,
        APINetworkCaptured,
        APIJsExecuted,
        DerivedProperty,
        Failed,
        Completed,
        CacheHit,
        AttemptedMatch,
        DatahubPageFetched,
        DatahubDatabasesCreated,
        DatahubSchemasCreated,
        DatahubTablesProcessed,
        DatahubEmbeddingBatch,
        ViewedPdfPage,
    ],
    PropertyInfo(discriminator="event_type"),
]
