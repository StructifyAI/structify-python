# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from .._utils import PropertyInfo

__all__ = [
    "EntityUpdatePropertyParams",
    "PropValue",
    "PropValueImage",
    "Source",
    "SourceWeb",
    "SourceDocumentPage",
    "SourceSecFiling",
]


class EntityUpdatePropertyParams(TypedDict, total=False):
    dataset_name: Required[str]

    entity_id: Required[str]

    prop_name: Required[str]
    """The name of the property to update"""

    prop_value: Required[PropValue]

    source: Source


class PropValueImage(TypedDict, total=False):
    number: Required[int]

    hash: str


PropValue: TypeAlias = Union[str, bool, float, PropValueImage]


class SourceWeb(TypedDict, total=False):
    web: Required[Annotated[str, PropertyInfo(alias="Web")]]


class SourceDocumentPage(TypedDict, total=False):
    document_page: Required[Annotated[Iterable[object], PropertyInfo(alias="DocumentPage")]]


class SourceSecFiling(TypedDict, total=False):
    sec_filing: Required[Annotated[Iterable[object], PropertyInfo(alias="SecFiling")]]


Source: TypeAlias = Union[Literal["None"], SourceWeb, SourceDocumentPage, SourceSecFiling]
