# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["TeamExpireGrantsParams"]


class TeamExpireGrantsParams(TypedDict, total=False):
    source_type: Required[str]

    team_id: Required[str]
