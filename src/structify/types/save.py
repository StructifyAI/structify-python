# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.


from pydantic import Field as FieldInfo

from .._models import BaseModel
from .knowledge_graph import KnowledgeGraph

__all__ = ["Save"]


class Save(BaseModel):
    save: KnowledgeGraph = FieldInfo(alias="Save")
    """
    Knowledge graph info structured to deserialize and display in the same format
    that the LLM outputs. Also the first representation of an LLM output in the
    pipeline from raw tool output to being merged into a Neo4j DB
    """
