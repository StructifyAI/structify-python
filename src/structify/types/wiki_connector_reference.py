# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union

from .._models import BaseModel

__all__ = [
    "WikiConnectorReference",
    "ReferenceIDConnector",
    "ReferenceIDDatabase",
    "ReferenceIDSchema",
    "ReferenceIDTable",
    "ReferenceIDColumn",
]


class ReferenceIDConnector:
    pass


class ReferenceIDDatabase:
    pass


class ReferenceIDSchema:
    pass


class ReferenceIDTable:
    pass


class ReferenceIDColumn:
    pass


class WikiConnectorReference(BaseModel):
    is_deleted: bool

    name: str

    path: List[str]

    reference_id: Union[
        ReferenceIDConnector, ReferenceIDDatabase, ReferenceIDSchema, ReferenceIDTable, ReferenceIDColumn
    ]
