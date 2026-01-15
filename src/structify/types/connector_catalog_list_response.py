# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel
from .connector_catalog_with_methods import ConnectorCatalogWithMethods

__all__ = ["ConnectorCatalogListResponse", "CategoryCount"]


class CategoryCount(BaseModel):
    category: str
    """Primary category label used for catalog filtering."""

    count: int
    """Number of catalog entries in this category."""


class ConnectorCatalogListResponse(BaseModel):
    category_counts: List[CategoryCount]
    """Counts of catalog entries grouped by primary category."""

    items: List[ConnectorCatalogWithMethods]

    total_count: int
