# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["StripeCreatePortalSessionParams"]


class StripeCreatePortalSessionParams(TypedDict, total=False):
    return_url: Required[str]

    team_id: Required[str]
