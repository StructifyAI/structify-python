# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Required, TypedDict

__all__ = ["ExtractionCriteriaParam"]


class ExtractionCriteriaParam(TypedDict, total=False):
    property_names: Required[List[str]]

    table_name: Required[str]
    """Vec<ExtractionCriteria> = it has to meet every one."""
