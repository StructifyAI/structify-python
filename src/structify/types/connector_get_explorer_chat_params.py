# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["ConnectorGetExplorerChatParams"]


class ConnectorGetExplorerChatParams(TypedDict, total=False):
    database_id: Optional[str]

    run_id: Optional[str]

    schema_id: Optional[str]

    table_id: Optional[str]
