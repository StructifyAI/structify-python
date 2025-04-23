# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Iterable
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from ..._utils import PropertyInfo

__all__ = [
    "WorkflowParam",
    "Step",
    "StepOperation",
    "StepOperationEnhanceProperties",
    "StepOperationEnhanceRelationship",
    "StepOperationDeriveProperty",
]


class StepOperationEnhanceProperties(TypedDict, total=False):
    enhance_properties: Required[Annotated[List[str], PropertyInfo(alias="EnhanceProperties")]]


class StepOperationEnhanceRelationship(TypedDict, total=False):
    enhance_relationship: Required[Annotated[str, PropertyInfo(alias="EnhanceRelationship")]]


class StepOperationDeriveProperty(TypedDict, total=False):
    derive_property: Required[Annotated[List[str], PropertyInfo(alias="DeriveProperty")]]


StepOperation: TypeAlias = Union[
    StepOperationEnhanceProperties, StepOperationEnhanceRelationship, StepOperationDeriveProperty, Literal["IngestData"]
]


class Step(TypedDict, total=False):
    id: Required[str]

    children: Required[List[str]]

    operation: Required[StepOperation]

    table_name: Required[str]


class WorkflowParam(TypedDict, total=False):
    name: Required[str]

    starting_step: Required[str]

    starting_table: Required[str]

    steps: Required[Iterable[Step]]
