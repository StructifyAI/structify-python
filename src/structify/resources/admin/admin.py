# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .users import UsersResource, AsyncUsersResource

from ..._compat import cached_property

import warnings
from typing import TYPE_CHECKING, Optional, Union, List, Dict, Any, Mapping, cast, overload
from typing_extensions import Literal
from ..._utils import extract_files, maybe_transform, required_args, deepcopy_minimal, strip_not_given
from ..._types import NotGiven, Timeout, Headers, NoneType, Query, Body, NOT_GIVEN, FileTypes, BinaryResponseContent
from ..._resource import SyncAPIResource, AsyncAPIResource
from ...types import shared_params
from .users import UsersResource, AsyncUsersResource, UsersResourceWithRawResponse, AsyncUsersResourceWithRawResponse, UsersResourceWithStreamingResponse, AsyncUsersResourceWithStreamingResponse

__all__ = ["AdminResource", "AsyncAdminResource"]

class AdminResource(SyncAPIResource):
    @cached_property
    def users(self) -> UsersResource:
        return UsersResource(self._client)

    @cached_property
    def with_raw_response(self) -> AdminResourceWithRawResponse:
        return AdminResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AdminResourceWithStreamingResponse:
        return AdminResourceWithStreamingResponse(self)

class AsyncAdminResource(AsyncAPIResource):
    @cached_property
    def users(self) -> AsyncUsersResource:
        return AsyncUsersResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncAdminResourceWithRawResponse:
        return AsyncAdminResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAdminResourceWithStreamingResponse:
        return AsyncAdminResourceWithStreamingResponse(self)

class AdminResourceWithRawResponse:
    def __init__(self, admin: AdminResource) -> None:
        self._admin = admin

    @cached_property
    def users(self) -> UsersResourceWithRawResponse:
        return UsersResourceWithRawResponse(self._admin.users)

class AsyncAdminResourceWithRawResponse:
    def __init__(self, admin: AsyncAdminResource) -> None:
        self._admin = admin

    @cached_property
    def users(self) -> AsyncUsersResourceWithRawResponse:
        return AsyncUsersResourceWithRawResponse(self._admin.users)

class AdminResourceWithStreamingResponse:
    def __init__(self, admin: AdminResource) -> None:
        self._admin = admin

    @cached_property
    def users(self) -> UsersResourceWithStreamingResponse:
        return UsersResourceWithStreamingResponse(self._admin.users)

class AsyncAdminResourceWithStreamingResponse:
    def __init__(self, admin: AsyncAdminResource) -> None:
        self._admin = admin

    @cached_property
    def users(self) -> AsyncUsersResourceWithStreamingResponse:
        return AsyncUsersResourceWithStreamingResponse(self._admin.users)