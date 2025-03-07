# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import TypedDict

__all__ = ["WebParam"]


class WebParam(TypedDict, total=False):
    starting_searches: List[str]

    starting_urls: List[str]
