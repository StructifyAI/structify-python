# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Required, TypedDict

__all__ = ["ConnectorCreateParams"]


class ConnectorCreateParams(TypedDict, total=False):
    llm_information_store: Required[str]

    name: Required[str]

    project_id: Required[str]

    description: Optional[str]

    secrets: Dict[str, str]
    """Optional secrets/environment variables for the connector"""
