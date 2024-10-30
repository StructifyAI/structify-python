# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.


from .._models import BaseModel

__all__ = ["UserUsageResponse"]


class UserUsageResponse(BaseModel):
    credits_used: int

    num_entities: int

    num_jobs: int

    num_relationships: int
