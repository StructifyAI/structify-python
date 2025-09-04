# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["ConnectorCreateSecretParams"]


class ConnectorCreateSecretParams(TypedDict, total=False):
    secret_name: Required[str]

    secret_value: Required[str]
