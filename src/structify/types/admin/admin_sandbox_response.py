# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union, Optional
from datetime import datetime
from typing_extensions import Literal, Annotated, TypeAlias

from ..._utils import PropertyInfo
from ..._models import BaseModel

__all__ = ["AdminSandboxResponse", "Dora", "Diego"]


class Dora(BaseModel):
    id: str

    chat_session_id: str

    created_at: datetime

    modal_id: str

    modal_url: str

    sandbox_type: Literal["dora"]

    status: Literal["alive", "terminated"]

    updated_at: datetime

    latest_node: Optional[str] = None


class Diego(BaseModel):
    id: str

    active_count: int

    created_at: datetime

    exploration_run_id: str

    sandbox_type: Literal["diego"]

    status: Literal["alive", "terminated"]

    updated_at: datetime

    modal_id: Optional[str] = None

    modal_url: Optional[str] = None


AdminSandboxResponse: TypeAlias = Annotated[Union[Dora, Diego], PropertyInfo(discriminator="sandbox_type")]
