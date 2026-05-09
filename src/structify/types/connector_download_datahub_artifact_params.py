# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["ConnectorDownloadDatahubArtifactParams"]


class ConnectorDownloadDatahubArtifactParams(TypedDict, total=False):
    connector_id: Required[str]

    exploration_run_id: Optional[str]
