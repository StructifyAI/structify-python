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
    "RelationshipProperty",
    "RelationshipPropertyMergeStrategy",
    "RelationshipPropertyMergeStrategyProbabilistic",
    "RelationshipPropertyMergeStrategyProbabilisticProbabilistic",
]


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
    """The configuration for a probabilistic merge strategy"""


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

    merge_strategy: Optional[object] = None

    properties: Optional[List[RelationshipProperty]] = None


class DatasetDescriptor(BaseModel):
    description: str

    name: str

    relationships: List[Relationship]

    tables: List[Table]

    llm_override_field: Optional[str] = None
