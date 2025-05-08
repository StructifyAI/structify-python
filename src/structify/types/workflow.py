# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = [
    "Workflow",
    "Step",
    "StepOperation",
    "StepOperationEnhanceProperties",
    "StepOperationEnhanceRelationship",
    "StepOperationDeriveProperty",
    "StepOperationScrapePage",
    "StepOperationScrapePageScrapePage",
]


class StepOperationEnhanceProperties(BaseModel):
    enhance_properties: List[str] = FieldInfo(alias="EnhanceProperties")


class StepOperationEnhanceRelationship(BaseModel):
    enhance_relationship: str = FieldInfo(alias="EnhanceRelationship")


class StepOperationDeriveProperty(BaseModel):
    derive_property: List[str] = FieldInfo(alias="DeriveProperty")


class StepOperationScrapePageScrapePage(BaseModel):
    relationship_name: str

    starting_url_property_name: str


class StepOperationScrapePage(BaseModel):
    scrape_page: StepOperationScrapePageScrapePage = FieldInfo(alias="ScrapePage")


StepOperation: TypeAlias = Union[
    StepOperationEnhanceProperties,
    StepOperationEnhanceRelationship,
    StepOperationDeriveProperty,
    StepOperationScrapePage,
    Literal["IngestData"],
]


class Step(BaseModel):
    id: str

    children: List[str]

    operation: StepOperation

    table_name: str


class Workflow(BaseModel):
    name: str

    starting_step: str

    starting_table: str

    steps: List[Step]
