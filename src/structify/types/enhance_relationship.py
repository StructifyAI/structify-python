# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .web import Web

__all__ = ["EnhanceRelationship"]


class EnhanceRelationship(Web):
    entity_id: str

    relationship_name: str

    allow_extra_entities: Optional[bool] = None
