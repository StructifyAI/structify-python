# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Required, TypedDict

__all__ = ["StructurePdfParams"]


class StructurePdfParams(TypedDict, total=False):
    dataset: Required[str]

    path: Required[str]

    instructions: Optional[str]

    model: Optional[str]

    node_id: Optional[str]

    pages: Optional[Iterable[int]]
