# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable, Optional
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from .._utils import PropertyInfo
from .table_param import TableParam
from .property_type_param import PropertyTypeParam

__all__ = [
    "DatasetCreateParams",
    "Relationship",
    "RelationshipProperty",
    "RelationshipPropertyMergeStrategy",
    "RelationshipPropertyMergeStrategyProbabilistic",
    "RelationshipPropertyMergeStrategyProbabilisticProbabilistic",
]


class DatasetCreateParams(TypedDict, total=False):
    description: Required[str]

    name: Required[str]

    relationships: Required[Iterable[Relationship]]

    tables: Required[Iterable[TableParam]]

    llm_override_field: Optional[str]


class RelationshipPropertyMergeStrategyProbabilisticProbabilistic(TypedDict, total=False):
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

    comparison_strategy: Literal["Default", "EnforceUniqueness"]


class RelationshipPropertyMergeStrategyProbabilistic(TypedDict, total=False):
    probabilistic: Required[
        Annotated[RelationshipPropertyMergeStrategyProbabilisticProbabilistic, PropertyInfo(alias="Probabilistic")]
    ]
    """The configuration for a probabilistic merge strategy"""


RelationshipPropertyMergeStrategy: TypeAlias = Union[
    Literal["Unique", "NoSignal"], RelationshipPropertyMergeStrategyProbabilistic
]


class RelationshipProperty(TypedDict, total=False):
    description: Required[str]

    name: Required[str]

    merge_strategy: RelationshipPropertyMergeStrategy

    prop_type: PropertyTypeParam


class Relationship(TypedDict, total=False):
    description: Required[str]

    name: Required[str]

    source_table: Required[str]

    target_table: Required[str]

    merge_strategy: object

    properties: Iterable[RelationshipProperty]
