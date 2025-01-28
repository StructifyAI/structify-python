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
    "RelationshipMergeStrategy",
    "RelationshipMergeStrategyProbabilistic",
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

    model_override: Optional[str]


class RelationshipMergeStrategyProbabilistic(TypedDict, total=False):
    source_cardinality_given_target_match: Optional[int]
    """
    Describes the expected cardinality of the source table when a match is found in
    the target table

    For example, if we have a source company and a target funding round, we expect
    the source company to appear in multiple funding rounds, but not _too_ many. So
    if we have a funding round match, the expected number of unique companies is
    relatively small. This is an estimate of that number.
    """

    target_cardinality_given_source_match: Optional[int]
    """
    Describes the expected cardinality of the target table when a match is found in
    the source table

    For example, if we have a source company and a target funding round, we usually
    expect some number of funding rounds to be associated with a single company but
    not _too_ many. So if we have a company match, the expected number of unique
    funding rounds is relatively small. This is an estimate of that number.
    """


class RelationshipMergeStrategy(TypedDict, total=False):
    probabilistic: Required[Annotated[RelationshipMergeStrategyProbabilistic, PropertyInfo(alias="Probabilistic")]]


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

    merge_strategy: Optional[RelationshipMergeStrategy]

    properties: Iterable[RelationshipProperty]
