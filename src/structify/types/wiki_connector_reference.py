# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union
from typing_extensions import Literal, Annotated, TypeAlias

from .._utils import PropertyInfo
from .._models import BaseModel

__all__ = [
    "WikiConnectorReference",
    "ReferenceID",
    "ReferenceIDConnector",
    "ReferenceIDDatabase",
    "ReferenceIDSchema",
    "ReferenceIDTable",
    "ReferenceIDColumn",
]


class ReferenceIDConnector(BaseModel):
    id: str

    reference_type: Literal["connector"]


class ReferenceIDDatabase(BaseModel):
    id: str

    reference_type: Literal["database"]


class ReferenceIDSchema(BaseModel):
    id: str

    reference_type: Literal["schema"]


class ReferenceIDTable(BaseModel):
    id: str

    reference_type: Literal["table"]


class ReferenceIDColumn(BaseModel):
    id: str

    reference_type: Literal["column"]


ReferenceID: TypeAlias = Annotated[
    Union[ReferenceIDConnector, ReferenceIDDatabase, ReferenceIDSchema, ReferenceIDTable, ReferenceIDColumn],
    PropertyInfo(discriminator="reference_type"),
]


class WikiConnectorReference(BaseModel):
    is_deleted: bool

    name: str

    path: List[str]

    reference_id: ReferenceID
