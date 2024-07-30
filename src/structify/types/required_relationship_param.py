# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["RequiredRelationshipParam", "RelationshipExtraction"]


class RelationshipExtraction(TypedDict, total=False):
    relationship_name: Required[str]


class RequiredRelationshipParam(TypedDict, total=False):
    relationship_extraction: Required[Annotated[RelationshipExtraction, PropertyInfo(alias="RelationshipExtraction")]]
