# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal, TypeAlias

__all__ = ["DatahubIngestionKey"]

DatahubIngestionKey: TypeAlias = Literal[
    "host",
    "port",
    "database",
    "username",
    "password",
    "account_id",
    "warehouse",
    "role",
    "instance_url",
    "access_token",
]
