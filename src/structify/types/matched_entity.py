# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union
from typing_extensions import TypeAlias

from .image import Image
from .._compat import PYDANTIC_V2
from .._models import BaseModel

__all__ = [
    "MatchedEntity",
    "PropertyMatches",
    "PropertyMatchesMatchedProperties",
    "PropertyMatchesMatchedPropertiesValue1",
    "PropertyMatchesMatchedPropertiesValue2",
    "PropertyMatchesUnmatchedProperties1",
    "PropertyMatchesUnmatchedProperties2",
]

PropertyMatchesMatchedPropertiesValue1: TypeAlias = Union[str, bool, float, Image]

PropertyMatchesMatchedPropertiesValue2: TypeAlias = Union[str, bool, float, Image]


class PropertyMatchesMatchedProperties(BaseModel):
    match_score: float

    value1: PropertyMatchesMatchedPropertiesValue1

    value2: PropertyMatchesMatchedPropertiesValue2


PropertyMatchesUnmatchedProperties1: TypeAlias = Union[str, bool, float, Image]

PropertyMatchesUnmatchedProperties2: TypeAlias = Union[str, bool, float, Image]


class PropertyMatches(BaseModel):
    matched_properties: Dict[str, PropertyMatchesMatchedProperties]

    unmatched_properties_1: Dict[str, PropertyMatchesUnmatchedProperties1]

    unmatched_properties_2: Dict[str, PropertyMatchesUnmatchedProperties2]


class MatchedEntity(BaseModel):
    alternative_matches: List["MatchedEntity"]

    e1_id: str

    e2_id: str

    match_score: float

    property_matches: PropertyMatches


if PYDANTIC_V2:
    MatchedEntity.model_rebuild()
    PropertyMatches.model_rebuild()
    PropertyMatchesMatchedProperties.model_rebuild()
else:
    MatchedEntity.update_forward_refs()  # type: ignore
    PropertyMatches.update_forward_refs()  # type: ignore
    PropertyMatchesMatchedProperties.update_forward_refs()  # type: ignore
