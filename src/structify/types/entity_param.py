# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union
from typing_extensions import Required, TypeAlias, TypedDict

from .image_param import ImageParam

__all__ = ["EntityParam", "Properties"]

Properties: TypeAlias = Union[str, bool, float, ImageParam]


class EntityParam(TypedDict, total=False):
    id: Required[int]

    properties: Required[Dict[str, Properties]]

    type: Required[str]
