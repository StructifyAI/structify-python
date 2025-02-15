# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.


from ..._models import BaseModel

__all__ = ["EvaluateStatusResponse"]


class EvaluateStatusResponse(BaseModel):
    id: str

    progress: float

    status: str
