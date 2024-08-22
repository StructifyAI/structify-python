# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

from typing import Optional, List

from .entity import Entity

from .relationship import Relationship

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo
from ..types import shared

__all__ = ["KnowledgeGraph"]

class KnowledgeGraph(BaseModel):
    entities: Optional[List[Entity]] = None

    relationships: Optional[List[Relationship]] = None