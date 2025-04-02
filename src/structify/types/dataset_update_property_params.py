# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

from .strategy_param import StrategyParam
from .property_type_param import PropertyTypeParam

__all__ = ["DatasetUpdatePropertyParams"]


class DatasetUpdatePropertyParams(TypedDict, total=False):
    dataset_name: Required[str]

    property_name: Required[str]

    table_name: Required[str]

    new_property_description: Optional[str]

    new_property_merge_strategy: Optional[StrategyParam]

    new_property_type: Optional[PropertyTypeParam]
