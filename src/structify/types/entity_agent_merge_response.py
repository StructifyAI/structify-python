# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel

__all__ = ["EntityAgentMergeResponse"]


class EntityAgentMergeResponse(BaseModel):
    final_entity_id: str

    merged_entities: List[str]

    reasoning: Optional[str] = None
