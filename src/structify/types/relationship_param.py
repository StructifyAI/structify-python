# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union
from typing_extensions import Required, TypeAlias, TypedDict

from .image_param import ImageParam

__all__ = ["RelationshipParam", "Properties"]

Properties: TypeAlias = Union[str, bool, float, ImageParam]


class RelationshipParam(TypedDict, total=False):
    source: Required[int]

    target: Required[int]

    type: Required[str]

    properties: Dict[str, Properties]
