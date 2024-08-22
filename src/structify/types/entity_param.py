# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Required, TypedDict

__all__ = ["EntityParam"]


class EntityParam(TypedDict, total=False):
    id: Required[int]

    properties: Required[Dict[str, str]]

    type: Required[str]
