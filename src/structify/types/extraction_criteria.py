# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel

__all__ = ["ExtractionCriteria"]


class ExtractionCriteria(BaseModel):
    property_names: List[str]

    table_name: str
    """Vec<ExtractionCriteria> = it has to meet every one."""
