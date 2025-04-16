# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .entity import Entity
from .._models import BaseModel
from .relationship import Relationship

__all__ = ["KnowledgeGraph"]


class KnowledgeGraph(BaseModel):
    entities: List[Entity]

    relationships: List[Relationship]
