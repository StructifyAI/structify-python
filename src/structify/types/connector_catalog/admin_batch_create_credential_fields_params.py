# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

from .create_credential_field_request_param import CreateCredentialFieldRequestParam

__all__ = ["AdminBatchCreateCredentialFieldsParams"]


class AdminBatchCreateCredentialFieldsParams(TypedDict, total=False):
    fields: Required[Iterable[CreateCredentialFieldRequestParam]]
