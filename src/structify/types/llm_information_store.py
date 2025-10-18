# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union
from typing_extensions import Literal, Annotated, TypeAlias

from .._utils import PropertyInfo
from .._models import BaseModel
from .connector_relational_database_descriptor import ConnectorRelationalDatabaseDescriptor

__all__ = ["LlmInformationStore", "RelationalDatabase", "Other"]


class RelationalDatabase(ConnectorRelationalDatabaseDescriptor):
    type: Literal["relational_database"]


class Other(BaseModel):
    data: str

    type: Literal["other"]


LlmInformationStore: TypeAlias = Annotated[Union[RelationalDatabase, Other], PropertyInfo(discriminator="type")]
