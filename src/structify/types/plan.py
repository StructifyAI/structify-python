# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union

from .._models import BaseModel
from .enhance_property import EnhanceProperty
from .find_relationship import FindRelationship
from .enhance_relationship import EnhanceRelationship

__all__ = ["Plan"]


class Plan(BaseModel):
    steps: List[
        Union[
            EnhanceProperty,
            EnhanceRelationship,
            FindRelationship,
            List[Union[EnhanceProperty, EnhanceRelationship, FindRelationship]],
        ]
    ]
