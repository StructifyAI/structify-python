# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union
from typing_extensions import Required, TypeAlias, TypedDict

from .image_param import ImageParam
from .user_web_source_param import UserWebSourceParam
from .user_document_source_param import UserDocumentSourceParam

__all__ = ["EntityUpdatePropertyParams", "Properties", "Source"]


class EntityUpdatePropertyParams(TypedDict, total=False):
    dataset: Required[str]

    entity_id: Required[str]

    properties: Required[Dict[str, Properties]]

    source: Source


Properties: TypeAlias = Union[str, bool, float, ImageParam]

Source: TypeAlias = Union[UserWebSourceParam, UserDocumentSourceParam]
