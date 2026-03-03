# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .jobs import (
    JobsResource,
    AsyncJobsResource,
    JobsResourceWithRawResponse,
    AsyncJobsResourceWithRawResponse,
    JobsResourceWithStreamingResponse,
    AsyncJobsResourceWithStreamingResponse,
)
from .teams import (
    TeamsResource,
    AsyncTeamsResource,
    TeamsResourceWithRawResponse,
    AsyncTeamsResourceWithRawResponse,
    TeamsResourceWithStreamingResponse,
    AsyncTeamsResourceWithStreamingResponse,
)
from .users import (
    UsersResource,
    AsyncUsersResource,
    UsersResourceWithRawResponse,
    AsyncUsersResourceWithRawResponse,
    UsersResourceWithStreamingResponse,
    AsyncUsersResourceWithStreamingResponse,
)
from ...types import admin_report_critical_params
from .dataset import (
    DatasetResource,
    AsyncDatasetResource,
    DatasetResourceWithRawResponse,
    AsyncDatasetResourceWithRawResponse,
    DatasetResourceWithStreamingResponse,
    AsyncDatasetResourceWithStreamingResponse,
)
from .sandbox import (
    SandboxResource,
    AsyncSandboxResource,
    SandboxResourceWithRawResponse,
    AsyncSandboxResourceWithRawResponse,
    SandboxResourceWithStreamingResponse,
    AsyncSandboxResourceWithStreamingResponse,
)
from ..._types import Body, Query, Headers, NoneType, NotGiven, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from .connector import (
    ConnectorResource,
    AsyncConnectorResource,
    ConnectorResourceWithRawResponse,
    AsyncConnectorResourceWithRawResponse,
    ConnectorResourceWithStreamingResponse,
    AsyncConnectorResourceWithStreamingResponse,
)
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from .chat_templates import (
    ChatTemplatesResource,
    AsyncChatTemplatesResource,
    ChatTemplatesResourceWithRawResponse,
    AsyncChatTemplatesResourceWithRawResponse,
    ChatTemplatesResourceWithStreamingResponse,
    AsyncChatTemplatesResourceWithStreamingResponse,
)
from .functional_tests import (
    FunctionalTestsResource,
    AsyncFunctionalTestsResource,
    FunctionalTestsResourceWithRawResponse,
    AsyncFunctionalTestsResourceWithRawResponse,
    FunctionalTestsResourceWithStreamingResponse,
    AsyncFunctionalTestsResourceWithStreamingResponse,
)

__all__ = ["AdminResource", "AsyncAdminResource"]


class AdminResource(SyncAPIResource):
    """Admin endpoints"""

    @cached_property
    def teams(self) -> TeamsResource:
        """Admin endpoints"""
        return TeamsResource(self._client)

    @cached_property
    def dataset(self) -> DatasetResource:
        """Admin endpoints"""
        return DatasetResource(self._client)

    @cached_property
    def jobs(self) -> JobsResource:
        """Admin endpoints"""
        return JobsResource(self._client)

    @cached_property
    def sandbox(self) -> SandboxResource:
        """Admin endpoints"""
        return SandboxResource(self._client)

    @cached_property
    def functional_tests(self) -> FunctionalTestsResource:
        """Admin endpoints"""
        return FunctionalTestsResource(self._client)

    @cached_property
    def users(self) -> UsersResource:
        """Admin endpoints"""
        return UsersResource(self._client)

    @cached_property
    def chat_templates(self) -> ChatTemplatesResource:
        """Admin endpoints"""
        return ChatTemplatesResource(self._client)

    @cached_property
    def connector(self) -> ConnectorResource:
        """Admin endpoints"""
        return ConnectorResource(self._client)

    @cached_property
    def with_raw_response(self) -> AdminResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/StructifyAI/structify-python#accessing-raw-response-data-eg-headers
        """
        return AdminResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AdminResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/StructifyAI/structify-python#with_streaming_response
        """
        return AdminResourceWithStreamingResponse(self)

    def report_critical(
        self,
        *,
        message: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/admin/critical",
            body=maybe_transform({"message": message}, admin_report_critical_params.AdminReportCriticalParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncAdminResource(AsyncAPIResource):
    """Admin endpoints"""

    @cached_property
    def teams(self) -> AsyncTeamsResource:
        """Admin endpoints"""
        return AsyncTeamsResource(self._client)

    @cached_property
    def dataset(self) -> AsyncDatasetResource:
        """Admin endpoints"""
        return AsyncDatasetResource(self._client)

    @cached_property
    def jobs(self) -> AsyncJobsResource:
        """Admin endpoints"""
        return AsyncJobsResource(self._client)

    @cached_property
    def sandbox(self) -> AsyncSandboxResource:
        """Admin endpoints"""
        return AsyncSandboxResource(self._client)

    @cached_property
    def functional_tests(self) -> AsyncFunctionalTestsResource:
        """Admin endpoints"""
        return AsyncFunctionalTestsResource(self._client)

    @cached_property
    def users(self) -> AsyncUsersResource:
        """Admin endpoints"""
        return AsyncUsersResource(self._client)

    @cached_property
    def chat_templates(self) -> AsyncChatTemplatesResource:
        """Admin endpoints"""
        return AsyncChatTemplatesResource(self._client)

    @cached_property
    def connector(self) -> AsyncConnectorResource:
        """Admin endpoints"""
        return AsyncConnectorResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncAdminResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/StructifyAI/structify-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAdminResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAdminResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/StructifyAI/structify-python#with_streaming_response
        """
        return AsyncAdminResourceWithStreamingResponse(self)

    async def report_critical(
        self,
        *,
        message: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/admin/critical",
            body=await async_maybe_transform(
                {"message": message}, admin_report_critical_params.AdminReportCriticalParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AdminResourceWithRawResponse:
    def __init__(self, admin: AdminResource) -> None:
        self._admin = admin

        self.report_critical = to_raw_response_wrapper(
            admin.report_critical,
        )

    @cached_property
    def teams(self) -> TeamsResourceWithRawResponse:
        """Admin endpoints"""
        return TeamsResourceWithRawResponse(self._admin.teams)

    @cached_property
    def dataset(self) -> DatasetResourceWithRawResponse:
        """Admin endpoints"""
        return DatasetResourceWithRawResponse(self._admin.dataset)

    @cached_property
    def jobs(self) -> JobsResourceWithRawResponse:
        """Admin endpoints"""
        return JobsResourceWithRawResponse(self._admin.jobs)

    @cached_property
    def sandbox(self) -> SandboxResourceWithRawResponse:
        """Admin endpoints"""
        return SandboxResourceWithRawResponse(self._admin.sandbox)

    @cached_property
    def functional_tests(self) -> FunctionalTestsResourceWithRawResponse:
        """Admin endpoints"""
        return FunctionalTestsResourceWithRawResponse(self._admin.functional_tests)

    @cached_property
    def users(self) -> UsersResourceWithRawResponse:
        """Admin endpoints"""
        return UsersResourceWithRawResponse(self._admin.users)

    @cached_property
    def chat_templates(self) -> ChatTemplatesResourceWithRawResponse:
        """Admin endpoints"""
        return ChatTemplatesResourceWithRawResponse(self._admin.chat_templates)

    @cached_property
    def connector(self) -> ConnectorResourceWithRawResponse:
        """Admin endpoints"""
        return ConnectorResourceWithRawResponse(self._admin.connector)


class AsyncAdminResourceWithRawResponse:
    def __init__(self, admin: AsyncAdminResource) -> None:
        self._admin = admin

        self.report_critical = async_to_raw_response_wrapper(
            admin.report_critical,
        )

    @cached_property
    def teams(self) -> AsyncTeamsResourceWithRawResponse:
        """Admin endpoints"""
        return AsyncTeamsResourceWithRawResponse(self._admin.teams)

    @cached_property
    def dataset(self) -> AsyncDatasetResourceWithRawResponse:
        """Admin endpoints"""
        return AsyncDatasetResourceWithRawResponse(self._admin.dataset)

    @cached_property
    def jobs(self) -> AsyncJobsResourceWithRawResponse:
        """Admin endpoints"""
        return AsyncJobsResourceWithRawResponse(self._admin.jobs)

    @cached_property
    def sandbox(self) -> AsyncSandboxResourceWithRawResponse:
        """Admin endpoints"""
        return AsyncSandboxResourceWithRawResponse(self._admin.sandbox)

    @cached_property
    def functional_tests(self) -> AsyncFunctionalTestsResourceWithRawResponse:
        """Admin endpoints"""
        return AsyncFunctionalTestsResourceWithRawResponse(self._admin.functional_tests)

    @cached_property
    def users(self) -> AsyncUsersResourceWithRawResponse:
        """Admin endpoints"""
        return AsyncUsersResourceWithRawResponse(self._admin.users)

    @cached_property
    def chat_templates(self) -> AsyncChatTemplatesResourceWithRawResponse:
        """Admin endpoints"""
        return AsyncChatTemplatesResourceWithRawResponse(self._admin.chat_templates)

    @cached_property
    def connector(self) -> AsyncConnectorResourceWithRawResponse:
        """Admin endpoints"""
        return AsyncConnectorResourceWithRawResponse(self._admin.connector)


class AdminResourceWithStreamingResponse:
    def __init__(self, admin: AdminResource) -> None:
        self._admin = admin

        self.report_critical = to_streamed_response_wrapper(
            admin.report_critical,
        )

    @cached_property
    def teams(self) -> TeamsResourceWithStreamingResponse:
        """Admin endpoints"""
        return TeamsResourceWithStreamingResponse(self._admin.teams)

    @cached_property
    def dataset(self) -> DatasetResourceWithStreamingResponse:
        """Admin endpoints"""
        return DatasetResourceWithStreamingResponse(self._admin.dataset)

    @cached_property
    def jobs(self) -> JobsResourceWithStreamingResponse:
        """Admin endpoints"""
        return JobsResourceWithStreamingResponse(self._admin.jobs)

    @cached_property
    def sandbox(self) -> SandboxResourceWithStreamingResponse:
        """Admin endpoints"""
        return SandboxResourceWithStreamingResponse(self._admin.sandbox)

    @cached_property
    def functional_tests(self) -> FunctionalTestsResourceWithStreamingResponse:
        """Admin endpoints"""
        return FunctionalTestsResourceWithStreamingResponse(self._admin.functional_tests)

    @cached_property
    def users(self) -> UsersResourceWithStreamingResponse:
        """Admin endpoints"""
        return UsersResourceWithStreamingResponse(self._admin.users)

    @cached_property
    def chat_templates(self) -> ChatTemplatesResourceWithStreamingResponse:
        """Admin endpoints"""
        return ChatTemplatesResourceWithStreamingResponse(self._admin.chat_templates)

    @cached_property
    def connector(self) -> ConnectorResourceWithStreamingResponse:
        """Admin endpoints"""
        return ConnectorResourceWithStreamingResponse(self._admin.connector)


class AsyncAdminResourceWithStreamingResponse:
    def __init__(self, admin: AsyncAdminResource) -> None:
        self._admin = admin

        self.report_critical = async_to_streamed_response_wrapper(
            admin.report_critical,
        )

    @cached_property
    def teams(self) -> AsyncTeamsResourceWithStreamingResponse:
        """Admin endpoints"""
        return AsyncTeamsResourceWithStreamingResponse(self._admin.teams)

    @cached_property
    def dataset(self) -> AsyncDatasetResourceWithStreamingResponse:
        """Admin endpoints"""
        return AsyncDatasetResourceWithStreamingResponse(self._admin.dataset)

    @cached_property
    def jobs(self) -> AsyncJobsResourceWithStreamingResponse:
        """Admin endpoints"""
        return AsyncJobsResourceWithStreamingResponse(self._admin.jobs)

    @cached_property
    def sandbox(self) -> AsyncSandboxResourceWithStreamingResponse:
        """Admin endpoints"""
        return AsyncSandboxResourceWithStreamingResponse(self._admin.sandbox)

    @cached_property
    def functional_tests(self) -> AsyncFunctionalTestsResourceWithStreamingResponse:
        """Admin endpoints"""
        return AsyncFunctionalTestsResourceWithStreamingResponse(self._admin.functional_tests)

    @cached_property
    def users(self) -> AsyncUsersResourceWithStreamingResponse:
        """Admin endpoints"""
        return AsyncUsersResourceWithStreamingResponse(self._admin.users)

    @cached_property
    def chat_templates(self) -> AsyncChatTemplatesResourceWithStreamingResponse:
        """Admin endpoints"""
        return AsyncChatTemplatesResourceWithStreamingResponse(self._admin.chat_templates)

    @cached_property
    def connector(self) -> AsyncConnectorResourceWithStreamingResponse:
        """Admin endpoints"""
        return AsyncConnectorResourceWithStreamingResponse(self._admin.connector)
