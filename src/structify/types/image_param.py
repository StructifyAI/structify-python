# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

from .._types import FileTypes

__all__ = ["ImageParam"]


class ImageParam(TypedDict, total=False):
    flag_number: Optional[int]

    image: Optional[FileTypes]
