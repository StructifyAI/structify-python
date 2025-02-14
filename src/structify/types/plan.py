# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union
from typing_extensions import TypeAlias

from .._models import BaseModel
from .enhance_property import EnhanceProperty
from .find_relationship import FindRelationship
from .enhance_relationship import EnhanceRelationship

__all__ = ["Plan", "Step", "StepUnionMember3"]

StepUnionMember3: TypeAlias = Union[EnhanceProperty, EnhanceRelationship, FindRelationship]

Step: TypeAlias = Union[EnhanceProperty, EnhanceRelationship, FindRelationship, List[StepUnionMember3]]


class Plan(BaseModel):
    steps: List[Step]
