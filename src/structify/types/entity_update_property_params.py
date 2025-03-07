# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from .._utils import PropertyInfo
from .image_param import ImageParam

__all__ = ["EntityUpdatePropertyParams", "Properties", "Source", "SourceWeb", "SourceDocumentPage", "SourceSecFiling"]


class EntityUpdatePropertyParams(TypedDict, total=False):
    dataset_name: Required[str]

    entity_id: Required[str]

    properties: Required[Dict[str, Properties]]

    source: Source


Properties: TypeAlias = Union[str, bool, float, ImageParam]


class SourceWeb(TypedDict, total=False):
    web: Required[Annotated[str, PropertyInfo(alias="Web")]]


class SourceDocumentPage(TypedDict, total=False):
    document_page: Required[Annotated[Iterable[object], PropertyInfo(alias="DocumentPage")]]


class SourceSecFiling(TypedDict, total=False):
    sec_filing: Required[Annotated[Iterable[object], PropertyInfo(alias="SecFiling")]]


Source: TypeAlias = Union[Literal["None"], SourceWeb, SourceDocumentPage, SourceSecFiling]
