# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["RequiredProperty", "GenericProperty"]


class GenericProperty(BaseModel):
    property_names: List[str]

    table_name: str
    """Vec<ExtractionCriteria> = it has to meet every one."""


class RequiredProperty(BaseModel):
    generic_property: GenericProperty = FieldInfo(alias="GenericProperty")
