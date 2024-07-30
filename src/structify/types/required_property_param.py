# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["RequiredPropertyParam", "GenericProperty"]


class GenericProperty(TypedDict, total=False):
    property_names: Required[List[str]]

    table_name: Required[str]
    """Vec<ExtractionCriteria> = it has to meet every one."""


class RequiredPropertyParam(TypedDict, total=False):
    generic_property: Required[Annotated[GenericProperty, PropertyInfo(alias="GenericProperty")]]
