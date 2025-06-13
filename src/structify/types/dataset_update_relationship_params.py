# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

from .relationship_merge_strategy_param import RelationshipMergeStrategyParam

__all__ = ["DatasetUpdateRelationshipParams"]


class DatasetUpdateRelationshipParams(TypedDict, total=False):
    dataset_name: Required[str]

    relationship_name: Required[str]

    new_description: Optional[str]

    new_merge_strategy: Optional[RelationshipMergeStrategyParam]
