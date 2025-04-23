# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from ..._utils import PropertyInfo

__all__ = [
    "WorkflowParam",
    "Steps",
    "StepsOperation",
    "StepsOperationEnhanceProperties",
    "StepsOperationEnhanceRelationship",
    "StepsOperationDeriveProperty",
]


class StepsOperationEnhanceProperties(TypedDict, total=False):
    enhance_properties: Required[Annotated[List[str], PropertyInfo(alias="EnhanceProperties")]]


class StepsOperationEnhanceRelationship(TypedDict, total=False):
    enhance_relationship: Required[Annotated[str, PropertyInfo(alias="EnhanceRelationship")]]


class StepsOperationDeriveProperty(TypedDict, total=False):
    derive_property: Required[Annotated[List[str], PropertyInfo(alias="DeriveProperty")]]


StepsOperation: TypeAlias = Union[
    StepsOperationEnhanceProperties,
    StepsOperationEnhanceRelationship,
    StepsOperationDeriveProperty,
    Literal["IngestData"],
]


class Steps(TypedDict, total=False):
    id: Required[str]

    children: Required[List[str]]

    operation: Required[StepsOperation]

    table_name: Required[str]


class WorkflowParam(TypedDict, total=False):
    name: Required[str]

    starting_step: Required[str]

    starting_table: Required[str]

    steps: Required[Dict[str, Steps]]
