# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["SecretUpdateParams"]


class SecretUpdateParams(TypedDict, total=False):
    project_id: Required[str]

    secret_value: Required[str]
    """The new secret value to encrypt and store"""
