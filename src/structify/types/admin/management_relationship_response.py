# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel
from .management_relationship_detail import ManagementRelationshipDetail

__all__ = ["ManagementRelationshipResponse"]


class ManagementRelationshipResponse(BaseModel):
    relationship: ManagementRelationshipDetail
    """
    A management relationship plus the human-readable names of both teams, so admin
    UIs don't need a separate lookup to render labels.
    """
