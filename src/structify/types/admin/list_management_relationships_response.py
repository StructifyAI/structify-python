# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel
from .management_relationship_detail import ManagementRelationshipDetail

__all__ = ["ListManagementRelationshipsResponse"]


class ListManagementRelationshipsResponse(BaseModel):
    relationships: List[ManagementRelationshipDetail]
