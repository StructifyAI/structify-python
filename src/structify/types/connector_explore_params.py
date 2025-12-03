# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, TypedDict

__all__ = ["ConnectorExploreParams"]


class ConnectorExploreParams(TypedDict, total=False):
    database_id: Optional[str]

    schema_id: Optional[str]

    stage: Optional[Literal["both", "ingestion", "annotation"]]
    """Which exploration stage to run"""

    table_id: Optional[str]
