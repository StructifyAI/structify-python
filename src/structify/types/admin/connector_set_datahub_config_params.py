# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

from .datahub_ingestion_type import DatahubIngestionType
from ..datahub_secret_map_param import DatahubSecretMapParam

__all__ = ["ConnectorSetDatahubConfigParams"]


class ConnectorSetDatahubConfigParams(TypedDict, total=False):
    connector_id: Required[str]

    datahub_ingestion_type: Optional[DatahubIngestionType]

    datahub_secret_map: Optional[DatahubSecretMapParam]
    """
    Maps DatahubIngestionKey to the name of the connector secret that holds the
    value.
    """
