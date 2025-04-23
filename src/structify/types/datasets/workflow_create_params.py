# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from ..._utils import PropertyInfo

__all__ = [
    "WorkflowCreateParams",
    "Workflow",
    "WorkflowSteps",
    "WorkflowStepsOperation",
    "WorkflowStepsOperationEnhanceProperties",
    "WorkflowStepsOperationEnhanceRelationship",
    "WorkflowStepsOperationDeriveProperty",
]


class WorkflowCreateParams(TypedDict, total=False):
    dataset_name: Required[str]

    name: Required[str]

    workflow: Required[Workflow]


class WorkflowStepsOperationEnhanceProperties(TypedDict, total=False):
    enhance_properties: Required[Annotated[List[str], PropertyInfo(alias="EnhanceProperties")]]


class WorkflowStepsOperationEnhanceRelationship(TypedDict, total=False):
    enhance_relationship: Required[Annotated[str, PropertyInfo(alias="EnhanceRelationship")]]


class WorkflowStepsOperationDeriveProperty(TypedDict, total=False):
    derive_property: Required[Annotated[List[str], PropertyInfo(alias="DeriveProperty")]]


WorkflowStepsOperation: TypeAlias = Union[
    WorkflowStepsOperationEnhanceProperties,
    WorkflowStepsOperationEnhanceRelationship,
    WorkflowStepsOperationDeriveProperty,
    Literal["IngestData"],
]


class WorkflowSteps(TypedDict, total=False):
    id: Required[str]

    children: Required[List[str]]

    operation: Required[WorkflowStepsOperation]

    table_name: Required[str]


class Workflow(TypedDict, total=False):
    name: Required[str]

    starting_step: Required[str]

    starting_table: Required[str]

    steps: Required[Dict[str, WorkflowSteps]]
