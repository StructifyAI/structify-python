# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .web import Web

__all__ = ["FindRelationship"]


class FindRelationship(Web):
    relationship_name: str

    source_entity_id: str

    target_entity_id: str

    allow_extra_entities: Optional[bool] = None
