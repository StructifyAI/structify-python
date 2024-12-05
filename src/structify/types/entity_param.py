# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union
from typing_extensions import Required, TypeAlias, TypedDict

__all__ = ["EntityParam", "Properties", "PropertiesImage"]


class PropertiesImage(TypedDict, total=False):
    number: Required[int]

    hash: str


Properties: TypeAlias = Union[str, bool, float, PropertiesImage]


class EntityParam(TypedDict, total=False):
    id: Required[int]

    properties: Required[Dict[str, Properties]]

    type: Required[str]
