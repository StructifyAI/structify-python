# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .pending_nango_integration import PendingNangoIntegration

__all__ = ["AdminListNangoPendingResponse"]

AdminListNangoPendingResponse: TypeAlias = List[PendingNangoIntegration]
