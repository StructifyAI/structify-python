# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal, TypeAlias

from .._models import BaseModel

__all__ = ["StructureJobStatusResponse", "StructureJobStatusResponseItem", "StructureJobStatusResponseItemTarget"]


class StructureJobStatusResponseItemTarget(BaseModel):
    entity_id: str

    property_names: Optional[List[str]] = None

    relationship_name: Optional[str] = None


class StructureJobStatusResponseItem(BaseModel):
    dataset_name: str

    job_id: str

    status: Optional[Literal["Queued", "Running", "Completed", "Failed"]] = None

    target: Optional[StructureJobStatusResponseItemTarget] = None


StructureJobStatusResponse: TypeAlias = List[StructureJobStatusResponseItem]
