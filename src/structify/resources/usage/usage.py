# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from .get_job_info import (
    GetJobInfoResource,
    AsyncGetJobInfoResource,
    GetJobInfoResourceWithRawResponse,
    AsyncGetJobInfoResourceWithRawResponse,
    GetJobInfoResourceWithStreamingResponse,
    AsyncGetJobInfoResourceWithStreamingResponse,
)

__all__ = ["UsageResource", "AsyncUsageResource"]


class UsageResource(SyncAPIResource):
    @cached_property
    def get_job_info(self) -> GetJobInfoResource:
        return GetJobInfoResource(self._client)

    @cached_property
    def with_raw_response(self) -> UsageResourceWithRawResponse:
        return UsageResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> UsageResourceWithStreamingResponse:
        return UsageResourceWithStreamingResponse(self)


class AsyncUsageResource(AsyncAPIResource):
    @cached_property
    def get_job_info(self) -> AsyncGetJobInfoResource:
        return AsyncGetJobInfoResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncUsageResourceWithRawResponse:
        return AsyncUsageResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncUsageResourceWithStreamingResponse:
        return AsyncUsageResourceWithStreamingResponse(self)


class UsageResourceWithRawResponse:
    def __init__(self, usage: UsageResource) -> None:
        self._usage = usage

    @cached_property
    def get_job_info(self) -> GetJobInfoResourceWithRawResponse:
        return GetJobInfoResourceWithRawResponse(self._usage.get_job_info)


class AsyncUsageResourceWithRawResponse:
    def __init__(self, usage: AsyncUsageResource) -> None:
        self._usage = usage

    @cached_property
    def get_job_info(self) -> AsyncGetJobInfoResourceWithRawResponse:
        return AsyncGetJobInfoResourceWithRawResponse(self._usage.get_job_info)


class UsageResourceWithStreamingResponse:
    def __init__(self, usage: UsageResource) -> None:
        self._usage = usage

    @cached_property
    def get_job_info(self) -> GetJobInfoResourceWithStreamingResponse:
        return GetJobInfoResourceWithStreamingResponse(self._usage.get_job_info)


class AsyncUsageResourceWithStreamingResponse:
    def __init__(self, usage: AsyncUsageResource) -> None:
        self._usage = usage

    @cached_property
    def get_job_info(self) -> AsyncGetJobInfoResourceWithStreamingResponse:
        return AsyncGetJobInfoResourceWithStreamingResponse(self._usage.get_job_info)
