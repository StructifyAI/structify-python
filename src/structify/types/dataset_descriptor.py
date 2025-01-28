# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from .table import Table
from .._models import BaseModel
from .property_type import PropertyType

__all__ = [
    "DatasetDescriptor",
    "Relationship",
    "RelationshipMergeStrategy",
    "RelationshipMergeStrategyProbabilistic",
    "RelationshipProperty",
    "RelationshipPropertyMergeStrategy",
    "RelationshipPropertyMergeStrategyProbabilistic",
    "RelationshipPropertyMergeStrategyProbabilisticProbabilistic",
]


class RelationshipMergeStrategyProbabilistic(BaseModel):
    source_cardinality_given_target_match: Optional[int] = None
    """
    Describes the expected cardinality of the source table when a match is found in
    the target table

    For example, if we have a source company and a target funding round, we expect
    the source company to appear in multiple funding rounds, but not _too_ many. So
    if we have a funding round match, the expected number of unique companies is
    relatively small. This is an estimate of that number.
    """

    target_cardinality_given_source_match: Optional[int] = None
    """
    Describes the expected cardinality of the target table when a match is found in
    the source table

    For example, if we have a source company and a target funding round, we usually
    expect some number of funding rounds to be associated with a single company but
    not _too_ many. So if we have a company match, the expected number of unique
    funding rounds is relatively small. This is an estimate of that number.
    """


class RelationshipMergeStrategy(BaseModel):
    probabilistic: RelationshipMergeStrategyProbabilistic = FieldInfo(alias="Probabilistic")


class RelationshipPropertyMergeStrategyProbabilisticProbabilistic(BaseModel):
    baseline_cardinality: int
    """
    The number of unique values that are expected to be present in the complete
    dataset

    This is used for merging to determine how significant a match is. (i.e. if there
    are only 2 possible values, a match gives less confidence than if there are 100)
    """

    match_transfer_probability: float
    """The estimated probability that, given an entity match, the properties also match

    For a person's full name, this would be quite high. For a person's job title, it
    would be lower because people can have multiple job titles over time or at
    different companies at the same time.
    """

    comparison_strategy: Optional[Literal["Default", "EnforceUniqueness"]] = None


class RelationshipPropertyMergeStrategyProbabilistic(BaseModel):
    probabilistic: RelationshipPropertyMergeStrategyProbabilisticProbabilistic = FieldInfo(alias="Probabilistic")


RelationshipPropertyMergeStrategy: TypeAlias = Union[
    Literal["Unique", "NoSignal"], RelationshipPropertyMergeStrategyProbabilistic
]


class RelationshipProperty(BaseModel):
    description: str

    name: str

    merge_strategy: Optional[RelationshipPropertyMergeStrategy] = None

    prop_type: Optional[PropertyType] = None


class Relationship(BaseModel):
    description: str

    name: str

    source_table: str

    target_table: str

    merge_strategy: Optional[RelationshipMergeStrategy] = None

    properties: Optional[List[RelationshipProperty]] = None


class DatasetDescriptor(BaseModel):
    description: str

    name: str

    relationships: List[Relationship]

    tables: List[Table]

    api_model_override: Optional[str] = FieldInfo(alias="model_override", default=None)
