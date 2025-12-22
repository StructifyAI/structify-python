# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .connector_catalog_with_methods import ConnectorCatalogWithMethods

__all__ = ["ConnectorCatalogListResponse"]

ConnectorCatalogListResponse: TypeAlias = List[ConnectorCatalogWithMethods]
