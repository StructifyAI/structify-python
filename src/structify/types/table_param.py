# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable, Optional
from typing_extensions import Required, TypeAlias, TypedDict

from .property_type_param import PropertyTypeParam

__all__ = ["TableParam", "Property", "PropertyMergeStrategy", "PropertyMergeStrategyMergeProbability"]


class PropertyMergeStrategyMergeProbability(TypedDict, total=False):
    baseline_cardinality: Required[int]
    """
    The number of unique values that are expected to be present in the complete
    dataset

    This is used for merging to determine how significant a match is. (i.e. if there
    are only 2 possible values, a match gives less confidence than if there are 100)
    """

    match_transfer_probability: Required[float]
    """The estimated probability that, given an entity match, the properties also match

    For a person's full name, this would be quite high. For a person's job title, it
    would be lower because people can have multiple job titles over time or at
    different companies at the same time.
    """

    comparison_strategy: Optional[object]


PropertyMergeStrategy: TypeAlias = Union[PropertyMergeStrategyMergeProbability, Optional[object], Optional[object]]


class Property(TypedDict, total=False):
    description: Required[str]

    name: Required[str]

    merge_strategy: PropertyMergeStrategy

    prop_type: PropertyTypeParam


class TableParam(TypedDict, total=False):
    description: Required[str]

    name: Required[str]
    """Organized in a name, description format."""

    properties: Required[Iterable[Property]]
    """Organized in a name, description format."""

    expected_cardinality: Optional[int]
    """Expected number of unique values in the complete dataset.

    This is used for our probabilistic merge strategy.
    """
