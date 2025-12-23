# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

from ..._types import SequenceNotStr

__all__ = ["AdminUpdateCatalogParams"]


class AdminUpdateCatalogParams(TypedDict, total=False):
    categories: Optional[SequenceNotStr[str]]

    description: Optional[str]

    logo_path: Optional[str]

    name: Optional[str]

    priority: Optional[int]
