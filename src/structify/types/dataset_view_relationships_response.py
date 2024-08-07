# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.



from .._models import BaseModel

__all__ = ["DatasetViewRelationshipsResponse"]


class DatasetViewRelationshipsResponse(BaseModel):
    from_id: str

    label: str

    to_id: str
