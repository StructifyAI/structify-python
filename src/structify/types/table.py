# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .property_type import PropertyType

__all__ = [
    "Table",
    "Property",
    "PropertyMergeStrategy",
    "PropertyMergeStrategyProbabilistic",
    "PropertyMergeStrategyProbabilisticProbabilistic",
]


class PropertyMergeStrategyProbabilisticProbabilistic(BaseModel):
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


class PropertyMergeStrategyProbabilistic(BaseModel):
    probabilistic: PropertyMergeStrategyProbabilisticProbabilistic = FieldInfo(alias="Probabilistic")


PropertyMergeStrategy: TypeAlias = Union[Literal["Unique"], PropertyMergeStrategyProbabilistic, Literal["NoSignal"]]


class Property(BaseModel):
    description: str

    name: str

    merge_strategy: Optional[PropertyMergeStrategy] = None
    """Property with unique 1:1 correspondence to its parent.

    Merge based on this property 100% of the time
    """

    prop_type: Optional[PropertyType] = None


class Table(BaseModel):
    description: str

    name: str
    """Organized in a name, description format."""

    properties: List[Property]
    """Organized in a name, description format."""

    expected_cardinality: Optional[int] = None
    """Expected number of unique values in the complete dataset.

    This is used for our probabilistic merge strategy.
    """
