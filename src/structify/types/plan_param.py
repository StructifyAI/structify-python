# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from typing_extensions import Required, TypeAlias, TypedDict

from .enhance_property_param import EnhancePropertyParam
from .find_relationship_param import FindRelationshipParam
from .enhance_relationship_param import EnhanceRelationshipParam

__all__ = ["PlanParam", "Step", "StepUnionMember3"]

StepUnionMember3: TypeAlias = Union[EnhancePropertyParam, EnhanceRelationshipParam, FindRelationshipParam]

Step: TypeAlias = Union[
    EnhancePropertyParam, EnhanceRelationshipParam, FindRelationshipParam, Iterable[StepUnionMember3]
]


class PlanParam(TypedDict, total=False):
    steps: Required[Iterable[Step]]
