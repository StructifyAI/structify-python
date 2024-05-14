# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .run import (
    RunResource,
    AsyncRunResource,
    RunResourceWithRawResponse,
    AsyncRunResourceWithRawResponse,
    RunResourceWithStreamingResponse,
    AsyncRunResourceWithStreamingResponse,
)
from ..._compat import cached_property
from .run_async import (
    RunAsyncResource,
    AsyncRunAsyncResource,
    RunAsyncResourceWithRawResponse,
    AsyncRunAsyncResourceWithRawResponse,
    RunAsyncResourceWithStreamingResponse,
    AsyncRunAsyncResourceWithStreamingResponse,
)
from .job_status import (
    JobStatusResource,
    AsyncJobStatusResource,
    JobStatusResourceWithRawResponse,
    AsyncJobStatusResourceWithRawResponse,
    JobStatusResourceWithStreamingResponse,
    AsyncJobStatusResourceWithStreamingResponse,
)
from ..._resource import SyncAPIResource, AsyncAPIResource
from .is_complete import (
    IsCompleteResource,
    AsyncIsCompleteResource,
    IsCompleteResourceWithRawResponse,
    AsyncIsCompleteResourceWithRawResponse,
    IsCompleteResourceWithStreamingResponse,
    AsyncIsCompleteResourceWithStreamingResponse,
)

__all__ = ["StructureResource", "AsyncStructureResource"]


class StructureResource(SyncAPIResource):
    @cached_property
    def is_complete(self) -> IsCompleteResource:
        return IsCompleteResource(self._client)

    @cached_property
    def job_status(self) -> JobStatusResource:
        return JobStatusResource(self._client)

    @cached_property
    def run(self) -> RunResource:
        return RunResource(self._client)

    @cached_property
    def run_async(self) -> RunAsyncResource:
        return RunAsyncResource(self._client)

    @cached_property
    def with_raw_response(self) -> StructureResourceWithRawResponse:
        return StructureResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> StructureResourceWithStreamingResponse:
        return StructureResourceWithStreamingResponse(self)


class AsyncStructureResource(AsyncAPIResource):
    @cached_property
    def is_complete(self) -> AsyncIsCompleteResource:
        return AsyncIsCompleteResource(self._client)

    @cached_property
    def job_status(self) -> AsyncJobStatusResource:
        return AsyncJobStatusResource(self._client)

    @cached_property
    def run(self) -> AsyncRunResource:
        return AsyncRunResource(self._client)

    @cached_property
    def run_async(self) -> AsyncRunAsyncResource:
        return AsyncRunAsyncResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncStructureResourceWithRawResponse:
        return AsyncStructureResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncStructureResourceWithStreamingResponse:
        return AsyncStructureResourceWithStreamingResponse(self)


class StructureResourceWithRawResponse:
    def __init__(self, structure: StructureResource) -> None:
        self._structure = structure

    @cached_property
    def is_complete(self) -> IsCompleteResourceWithRawResponse:
        return IsCompleteResourceWithRawResponse(self._structure.is_complete)

    @cached_property
    def job_status(self) -> JobStatusResourceWithRawResponse:
        return JobStatusResourceWithRawResponse(self._structure.job_status)

    @cached_property
    def run(self) -> RunResourceWithRawResponse:
        return RunResourceWithRawResponse(self._structure.run)

    @cached_property
    def run_async(self) -> RunAsyncResourceWithRawResponse:
        return RunAsyncResourceWithRawResponse(self._structure.run_async)


class AsyncStructureResourceWithRawResponse:
    def __init__(self, structure: AsyncStructureResource) -> None:
        self._structure = structure

    @cached_property
    def is_complete(self) -> AsyncIsCompleteResourceWithRawResponse:
        return AsyncIsCompleteResourceWithRawResponse(self._structure.is_complete)

    @cached_property
    def job_status(self) -> AsyncJobStatusResourceWithRawResponse:
        return AsyncJobStatusResourceWithRawResponse(self._structure.job_status)

    @cached_property
    def run(self) -> AsyncRunResourceWithRawResponse:
        return AsyncRunResourceWithRawResponse(self._structure.run)

    @cached_property
    def run_async(self) -> AsyncRunAsyncResourceWithRawResponse:
        return AsyncRunAsyncResourceWithRawResponse(self._structure.run_async)


class StructureResourceWithStreamingResponse:
    def __init__(self, structure: StructureResource) -> None:
        self._structure = structure

    @cached_property
    def is_complete(self) -> IsCompleteResourceWithStreamingResponse:
        return IsCompleteResourceWithStreamingResponse(self._structure.is_complete)

    @cached_property
    def job_status(self) -> JobStatusResourceWithStreamingResponse:
        return JobStatusResourceWithStreamingResponse(self._structure.job_status)

    @cached_property
    def run(self) -> RunResourceWithStreamingResponse:
        return RunResourceWithStreamingResponse(self._structure.run)

    @cached_property
    def run_async(self) -> RunAsyncResourceWithStreamingResponse:
        return RunAsyncResourceWithStreamingResponse(self._structure.run_async)


class AsyncStructureResourceWithStreamingResponse:
    def __init__(self, structure: AsyncStructureResource) -> None:
        self._structure = structure

    @cached_property
    def is_complete(self) -> AsyncIsCompleteResourceWithStreamingResponse:
        return AsyncIsCompleteResourceWithStreamingResponse(self._structure.is_complete)

    @cached_property
    def job_status(self) -> AsyncJobStatusResourceWithStreamingResponse:
        return AsyncJobStatusResourceWithStreamingResponse(self._structure.job_status)

    @cached_property
    def run(self) -> AsyncRunResourceWithStreamingResponse:
        return AsyncRunResourceWithStreamingResponse(self._structure.run)

    @cached_property
    def run_async(self) -> AsyncRunAsyncResourceWithStreamingResponse:
        return AsyncRunAsyncResourceWithStreamingResponse(self._structure.run_async)
