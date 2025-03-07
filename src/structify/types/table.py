# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import TypeAlias

from .._models import BaseModel
from .property_type import PropertyType

__all__ = ["Table", "Property", "PropertyMergeStrategy", "PropertyMergeStrategyMergeProbability"]


class PropertyMergeStrategyMergeProbability(BaseModel):
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

    comparison_strategy: Optional[object] = None


PropertyMergeStrategy: TypeAlias = Union[PropertyMergeStrategyMergeProbability, Optional[object], Optional[object]]


class Property(BaseModel):
    description: str

    name: str

    merge_strategy: Optional[PropertyMergeStrategy] = None

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
