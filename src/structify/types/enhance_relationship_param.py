# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required

from .web_param import WebParam

__all__ = ["EnhanceRelationshipParam"]


class EnhanceRelationshipParam(WebParam):
    entity_id: Required[str]

    relationship_name: Required[str]

    allow_extra_entities: bool
