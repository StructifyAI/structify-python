# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo

__all__ = [
    "StructureBulkEnhanceParams",
    "Target",
    "TargetProperties",
    "TargetPropertiesProperties",
    "TargetRelationship",
    "TargetRelationshipRelationship",
    "Source",
    "SourceScrape",
    "SourceScrapeScrape",
]


class StructureBulkEnhanceParams(TypedDict, total=False):
    dataset: Required[str]

    table_name: Required[str]

    target: Required[Target]

    instructions: Optional[str]

    model: Optional[str]

    node_id: Optional[str]

    source: Optional[Source]

    use_proxy: Optional[bool]


class TargetPropertiesProperties(TypedDict, total=False):
    property_names: Required[SequenceNotStr[str]]


class TargetProperties(TypedDict, total=False):
    properties: Required[Annotated[TargetPropertiesProperties, PropertyInfo(alias="Properties")]]


class TargetRelationshipRelationship(TypedDict, total=False):
    relationship_name: Required[str]


class TargetRelationship(TypedDict, total=False):
    relationship: Required[Annotated[TargetRelationshipRelationship, PropertyInfo(alias="Relationship")]]


Target: TypeAlias = Union[TargetProperties, TargetRelationship]


class SourceScrapeScrape(TypedDict, total=False):
    url_column: Required[str]


class SourceScrape(TypedDict, total=False):
    scrape: Required[Annotated[SourceScrapeScrape, PropertyInfo(alias="Scrape")]]


Source: TypeAlias = Union[Literal["Web"], SourceScrape]
