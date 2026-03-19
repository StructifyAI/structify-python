# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["ConnectorExploreParams"]


class ConnectorExploreParams(TypedDict, total=False):
    database_id: Optional[str]

    only_do_datahub: Optional[bool]
    """If true, run only DataHub ingestion without queuing Diego annotation jobs."""

    schema_id: Optional[str]

    table_id: Optional[str]
