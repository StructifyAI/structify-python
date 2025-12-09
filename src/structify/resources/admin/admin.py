# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

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
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
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
    @cached_property
    def teams(self) -> TeamsResource:
        return TeamsResource(self._client)

    @cached_property
    def dataset(self) -> DatasetResource:
        return DatasetResource(self._client)

    @cached_property
    def jobs(self) -> JobsResource:
        return JobsResource(self._client)

    @cached_property
    def sandbox(self) -> SandboxResource:
        return SandboxResource(self._client)

    @cached_property
    def functional_tests(self) -> FunctionalTestsResource:
        return FunctionalTestsResource(self._client)

    @cached_property
    def users(self) -> UsersResource:
        return UsersResource(self._client)

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


class AsyncAdminResource(AsyncAPIResource):
    @cached_property
    def teams(self) -> AsyncTeamsResource:
        return AsyncTeamsResource(self._client)

    @cached_property
    def dataset(self) -> AsyncDatasetResource:
        return AsyncDatasetResource(self._client)

    @cached_property
    def jobs(self) -> AsyncJobsResource:
        return AsyncJobsResource(self._client)

    @cached_property
    def sandbox(self) -> AsyncSandboxResource:
        return AsyncSandboxResource(self._client)

    @cached_property
    def functional_tests(self) -> AsyncFunctionalTestsResource:
        return AsyncFunctionalTestsResource(self._client)

    @cached_property
    def users(self) -> AsyncUsersResource:
        return AsyncUsersResource(self._client)

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


class AdminResourceWithRawResponse:
    def __init__(self, admin: AdminResource) -> None:
        self._admin = admin

    @cached_property
    def teams(self) -> TeamsResourceWithRawResponse:
        return TeamsResourceWithRawResponse(self._admin.teams)

    @cached_property
    def dataset(self) -> DatasetResourceWithRawResponse:
        return DatasetResourceWithRawResponse(self._admin.dataset)

    @cached_property
    def jobs(self) -> JobsResourceWithRawResponse:
        return JobsResourceWithRawResponse(self._admin.jobs)

    @cached_property
    def sandbox(self) -> SandboxResourceWithRawResponse:
        return SandboxResourceWithRawResponse(self._admin.sandbox)

    @cached_property
    def functional_tests(self) -> FunctionalTestsResourceWithRawResponse:
        return FunctionalTestsResourceWithRawResponse(self._admin.functional_tests)

    @cached_property
    def users(self) -> UsersResourceWithRawResponse:
        return UsersResourceWithRawResponse(self._admin.users)


class AsyncAdminResourceWithRawResponse:
    def __init__(self, admin: AsyncAdminResource) -> None:
        self._admin = admin

    @cached_property
    def teams(self) -> AsyncTeamsResourceWithRawResponse:
        return AsyncTeamsResourceWithRawResponse(self._admin.teams)

    @cached_property
    def dataset(self) -> AsyncDatasetResourceWithRawResponse:
        return AsyncDatasetResourceWithRawResponse(self._admin.dataset)

    @cached_property
    def jobs(self) -> AsyncJobsResourceWithRawResponse:
        return AsyncJobsResourceWithRawResponse(self._admin.jobs)

    @cached_property
    def sandbox(self) -> AsyncSandboxResourceWithRawResponse:
        return AsyncSandboxResourceWithRawResponse(self._admin.sandbox)

    @cached_property
    def functional_tests(self) -> AsyncFunctionalTestsResourceWithRawResponse:
        return AsyncFunctionalTestsResourceWithRawResponse(self._admin.functional_tests)

    @cached_property
    def users(self) -> AsyncUsersResourceWithRawResponse:
        return AsyncUsersResourceWithRawResponse(self._admin.users)


class AdminResourceWithStreamingResponse:
    def __init__(self, admin: AdminResource) -> None:
        self._admin = admin

    @cached_property
    def teams(self) -> TeamsResourceWithStreamingResponse:
        return TeamsResourceWithStreamingResponse(self._admin.teams)

    @cached_property
    def dataset(self) -> DatasetResourceWithStreamingResponse:
        return DatasetResourceWithStreamingResponse(self._admin.dataset)

    @cached_property
    def jobs(self) -> JobsResourceWithStreamingResponse:
        return JobsResourceWithStreamingResponse(self._admin.jobs)

    @cached_property
    def sandbox(self) -> SandboxResourceWithStreamingResponse:
        return SandboxResourceWithStreamingResponse(self._admin.sandbox)

    @cached_property
    def functional_tests(self) -> FunctionalTestsResourceWithStreamingResponse:
        return FunctionalTestsResourceWithStreamingResponse(self._admin.functional_tests)

    @cached_property
    def users(self) -> UsersResourceWithStreamingResponse:
        return UsersResourceWithStreamingResponse(self._admin.users)


class AsyncAdminResourceWithStreamingResponse:
    def __init__(self, admin: AsyncAdminResource) -> None:
        self._admin = admin

    @cached_property
    def teams(self) -> AsyncTeamsResourceWithStreamingResponse:
        return AsyncTeamsResourceWithStreamingResponse(self._admin.teams)

    @cached_property
    def dataset(self) -> AsyncDatasetResourceWithStreamingResponse:
        return AsyncDatasetResourceWithStreamingResponse(self._admin.dataset)

    @cached_property
    def jobs(self) -> AsyncJobsResourceWithStreamingResponse:
        return AsyncJobsResourceWithStreamingResponse(self._admin.jobs)

    @cached_property
    def sandbox(self) -> AsyncSandboxResourceWithStreamingResponse:
        return AsyncSandboxResourceWithStreamingResponse(self._admin.sandbox)

    @cached_property
    def functional_tests(self) -> AsyncFunctionalTestsResourceWithStreamingResponse:
        return AsyncFunctionalTestsResourceWithStreamingResponse(self._admin.functional_tests)

    @cached_property
    def users(self) -> AsyncUsersResourceWithStreamingResponse:
        return AsyncUsersResourceWithStreamingResponse(self._admin.users)
