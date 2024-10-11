# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Union

from .._models import BaseModel

__all__ = ["DatasetViewRelationshipsResponse"]


class DatasetViewRelationshipsResponse(BaseModel):
    from_id: str

    label: str

    properties: Dict[str, Union[str, bool, float]]

    to_id: str
