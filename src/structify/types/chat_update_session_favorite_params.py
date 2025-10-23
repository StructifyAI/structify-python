# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["ChatUpdateSessionFavoriteParams"]


class ChatUpdateSessionFavoriteParams(TypedDict, total=False):
    is_favorite: Required[bool]
