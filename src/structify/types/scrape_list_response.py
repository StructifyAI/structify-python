# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel
from .knowledge_graph import KnowledgeGraph

__all__ = ["ScrapeListResponse"]


class ScrapeListResponse(BaseModel):
    knowledge_graph: KnowledgeGraph
    """
    Knowledge graph info structured to deserialize and display in the same format
    that the LLM outputs. Also the first representation of an LLM output in the
    pipeline from raw tool output to being merged into a Neo4j DB
    """
