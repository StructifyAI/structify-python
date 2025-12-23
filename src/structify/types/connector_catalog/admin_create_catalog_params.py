# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

from ..._types import SequenceNotStr

__all__ = ["AdminCreateCatalogParams"]


class AdminCreateCatalogParams(TypedDict, total=False):
    name: Required[str]

    slug: Required[str]

    categories: SequenceNotStr[str]

    description: Optional[str]

    logo_path: Optional[str]

    priority: Optional[int]
