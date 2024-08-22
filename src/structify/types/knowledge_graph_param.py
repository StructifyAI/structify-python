# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable

from .entity_param import EntityParam

from .relationship_param import RelationshipParam

from typing_extensions import TypedDict

__all__ = ["KnowledgeGraphParam"]

class KnowledgeGraphParam(TypedDict, total=False):
    entities: Iterable[EntityParam]

    relationships: Iterable[RelationshipParam]