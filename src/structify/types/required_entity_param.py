# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["RequiredEntityParam", "EntityExtraction"]


class EntityExtraction(TypedDict, total=False):
    entity_id: Required[int]


class RequiredEntityParam(TypedDict, total=False):
    entity_extraction: Required[Annotated[EntityExtraction, PropertyInfo(alias="EntityExtraction")]]
