# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Required, TypedDict

__all__ = ["EntityUpdatePropertyParams"]


class EntityUpdatePropertyParams(TypedDict, total=False):
    dataset_name: Required[str]

    entity_id: Required[str]

    prop_name: Required[str]
    """The name of the property to update"""

    prop_value: Required[Union[str, bool, float]]
