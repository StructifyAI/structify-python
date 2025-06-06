# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["TeamCreateProjectParams"]


class TeamCreateProjectParams(TypedDict, total=False):
    name: Required[str]

    description: Optional[str]
