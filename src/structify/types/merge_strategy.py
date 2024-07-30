# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["MergeStrategy", "PropertyAttr", "FuzzyStringMatch"]


class PropertyAttr(BaseModel):
    property_attr: str = FieldInfo(alias="PropertyAttr")


class FuzzyStringMatch(BaseModel):
    fuzzy_string_match: str = FieldInfo(alias="FuzzyStringMatch")
    """
    merge on some list of property names iff the values are the same in the
    extracted KgEntity
    """


MergeStrategy = Union[PropertyAttr, FuzzyStringMatch, Literal["None"]]
