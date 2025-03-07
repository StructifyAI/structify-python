# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union
from typing_extensions import Required, TypeAlias, TypedDict

from .image_param import ImageParam

__all__ = ["EntityUpdatePropertyParams", "Properties", "Source", "SourceUserWebSource", "SourceUserDocumentSource"]


class EntityUpdatePropertyParams(TypedDict, total=False):
    dataset: Required[str]

    entity_id: Required[str]

    properties: Required[Dict[str, Properties]]

    source: Source


Properties: TypeAlias = Union[str, bool, float, ImageParam]


class SourceUserWebSource(TypedDict, total=False):
    url: Required[str]


class SourceUserDocumentSource(TypedDict, total=False):
    name: Required[str]

    page: Required[int]


Source: TypeAlias = Union[SourceUserWebSource, SourceUserDocumentSource]
