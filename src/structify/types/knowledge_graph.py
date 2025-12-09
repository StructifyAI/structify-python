# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .entity import Entity
from .._models import BaseModel
from .relationship import Relationship

__all__ = ["KnowledgeGraph"]


class KnowledgeGraph(BaseModel):
    """
    Knowledge graph info structured to deserialize and display
    in the same format that the LLM outputs.
    Also the first representation of an LLM output in the pipeline from raw tool output to being merged into a DB
    """

    entities: List[Entity]

    relationships: Optional[List[Relationship]] = None
