# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["WikiUpdateParams"]


class WikiUpdateParams(TypedDict, total=False):
    team_id: Required[str]

    markdown: Required[str]

    base_version: Optional[int]

    title: Optional[str]
