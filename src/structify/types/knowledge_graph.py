# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .entity import Entity
from .._models import BaseModel
from .relationship import Relationship

__all__ = ["KnowledgeGraph"]


class KnowledgeGraph(BaseModel):
    entities: Optional[List[Entity]] = None

    relationships: Optional[List[Relationship]] = None
