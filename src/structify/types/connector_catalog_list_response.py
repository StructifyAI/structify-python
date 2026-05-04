# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel
from .connector_catalog_with_methods import ConnectorCatalogWithMethods

__all__ = ["ConnectorCatalogListResponse", "CategoryCount"]


class CategoryCount(BaseModel):
    category: str

    count: int


class ConnectorCatalogListResponse(BaseModel):
    category_counts: List[CategoryCount]

    items: List[ConnectorCatalogWithMethods]

    total_count: int
