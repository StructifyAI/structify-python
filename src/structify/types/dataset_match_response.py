# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.


from .._models import BaseModel

__all__ = ["DatasetMatchResponse"]


class DatasetMatchResponse(BaseModel):
    entity: str

    score: float
