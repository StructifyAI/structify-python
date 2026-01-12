# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

from .._types import SequenceNotStr

__all__ = ["NangoCreateSessionParams"]


class NangoCreateSessionParams(TypedDict, total=False):
    connector_auth_method_id: Optional[str]

    selected_scope_ids: Optional[SequenceNotStr[str]]
    """Specific scope IDs to use.

    If not provided, defaults to required + recommended scopes. If the auth method
    has no scopes in the database, Nango's default scopes are used.
    """
