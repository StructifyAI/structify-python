# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable, Optional
from typing_extensions import Required, TypeAlias, TypedDict

from .image_param import ImageParam

__all__ = ["EntityUpdatePropertyParams", "Properties"]


class EntityUpdatePropertyParams(TypedDict, total=False):
    dataset: Required[str]

    entity_id: Required[str]

    properties: Required[Dict[str, Properties]]

    source: Union[str, Iterable[object], Iterable[object], Optional[object]]


Properties: TypeAlias = Union[str, bool, float, ImageParam]
