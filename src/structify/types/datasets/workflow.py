# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = [
    "Workflow",
    "Steps",
    "StepsOperation",
    "StepsOperationEnhanceProperties",
    "StepsOperationEnhanceRelationship",
    "StepsOperationDeriveProperty",
]


class StepsOperationEnhanceProperties(BaseModel):
    enhance_properties: List[str] = FieldInfo(alias="EnhanceProperties")


class StepsOperationEnhanceRelationship(BaseModel):
    enhance_relationship: str = FieldInfo(alias="EnhanceRelationship")


class StepsOperationDeriveProperty(BaseModel):
    derive_property: List[str] = FieldInfo(alias="DeriveProperty")


StepsOperation: TypeAlias = Union[
    StepsOperationEnhanceProperties,
    StepsOperationEnhanceRelationship,
    StepsOperationDeriveProperty,
    Literal["IngestData"],
]


class Steps(BaseModel):
    id: str

    children: List[str]

    operation: StepsOperation

    table_name: str


class Workflow(BaseModel):
    name: str

    starting_step: str

    starting_table: str

    steps: Dict[str, Steps]
