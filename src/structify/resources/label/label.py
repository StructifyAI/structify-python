# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .submit import (
    SubmitResource,
    AsyncSubmitResource,
    SubmitResourceWithRawResponse,
    AsyncSubmitResourceWithRawResponse,
    SubmitResourceWithStreamingResponse,
    AsyncSubmitResourceWithStreamingResponse,
)
from .update import (
    UpdateResource,
    AsyncUpdateResource,
    UpdateResourceWithRawResponse,
    AsyncUpdateResourceWithRawResponse,
    UpdateResourceWithStreamingResponse,
    AsyncUpdateResourceWithStreamingResponse,
)
from .refresh import (
    RefreshResource,
    AsyncRefreshResource,
    RefreshResourceWithRawResponse,
    AsyncRefreshResourceWithRawResponse,
    RefreshResourceWithStreamingResponse,
    AsyncRefreshResourceWithStreamingResponse,
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
from .llm_assist import (
    LlmAssistResource,
    AsyncLlmAssistResource,
    LlmAssistResourceWithRawResponse,
    AsyncLlmAssistResourceWithRawResponse,
    LlmAssistResourceWithStreamingResponse,
    AsyncLlmAssistResourceWithStreamingResponse,
)
from ..._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["LabelResource", "AsyncLabelResource"]


class LabelResource(SyncAPIResource):
    @cached_property
    def llm_assist(self) -> LlmAssistResource:
        return LlmAssistResource(self._client)

    @cached_property
    def refresh(self) -> RefreshResource:
        return RefreshResource(self._client)

    @cached_property
    def run_async(self) -> RunAsyncResource:
        return RunAsyncResource(self._client)

    @cached_property
    def submit(self) -> SubmitResource:
        return SubmitResource(self._client)

    @cached_property
    def update(self) -> UpdateResource:
        return UpdateResource(self._client)

    @cached_property
    def with_raw_response(self) -> LabelResourceWithRawResponse:
        return LabelResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> LabelResourceWithStreamingResponse:
        return LabelResourceWithStreamingResponse(self)


class AsyncLabelResource(AsyncAPIResource):
    @cached_property
    def llm_assist(self) -> AsyncLlmAssistResource:
        return AsyncLlmAssistResource(self._client)

    @cached_property
    def refresh(self) -> AsyncRefreshResource:
        return AsyncRefreshResource(self._client)

    @cached_property
    def run_async(self) -> AsyncRunAsyncResource:
        return AsyncRunAsyncResource(self._client)

    @cached_property
    def submit(self) -> AsyncSubmitResource:
        return AsyncSubmitResource(self._client)

    @cached_property
    def update(self) -> AsyncUpdateResource:
        return AsyncUpdateResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncLabelResourceWithRawResponse:
        return AsyncLabelResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncLabelResourceWithStreamingResponse:
        return AsyncLabelResourceWithStreamingResponse(self)


class LabelResourceWithRawResponse:
    def __init__(self, label: LabelResource) -> None:
        self._label = label

    @cached_property
    def llm_assist(self) -> LlmAssistResourceWithRawResponse:
        return LlmAssistResourceWithRawResponse(self._label.llm_assist)

    @cached_property
    def refresh(self) -> RefreshResourceWithRawResponse:
        return RefreshResourceWithRawResponse(self._label.refresh)

    @cached_property
    def run_async(self) -> RunAsyncResourceWithRawResponse:
        return RunAsyncResourceWithRawResponse(self._label.run_async)

    @cached_property
    def submit(self) -> SubmitResourceWithRawResponse:
        return SubmitResourceWithRawResponse(self._label.submit)

    @cached_property
    def update(self) -> UpdateResourceWithRawResponse:
        return UpdateResourceWithRawResponse(self._label.update)


class AsyncLabelResourceWithRawResponse:
    def __init__(self, label: AsyncLabelResource) -> None:
        self._label = label

    @cached_property
    def llm_assist(self) -> AsyncLlmAssistResourceWithRawResponse:
        return AsyncLlmAssistResourceWithRawResponse(self._label.llm_assist)

    @cached_property
    def refresh(self) -> AsyncRefreshResourceWithRawResponse:
        return AsyncRefreshResourceWithRawResponse(self._label.refresh)

    @cached_property
    def run_async(self) -> AsyncRunAsyncResourceWithRawResponse:
        return AsyncRunAsyncResourceWithRawResponse(self._label.run_async)

    @cached_property
    def submit(self) -> AsyncSubmitResourceWithRawResponse:
        return AsyncSubmitResourceWithRawResponse(self._label.submit)

    @cached_property
    def update(self) -> AsyncUpdateResourceWithRawResponse:
        return AsyncUpdateResourceWithRawResponse(self._label.update)


class LabelResourceWithStreamingResponse:
    def __init__(self, label: LabelResource) -> None:
        self._label = label

    @cached_property
    def llm_assist(self) -> LlmAssistResourceWithStreamingResponse:
        return LlmAssistResourceWithStreamingResponse(self._label.llm_assist)

    @cached_property
    def refresh(self) -> RefreshResourceWithStreamingResponse:
        return RefreshResourceWithStreamingResponse(self._label.refresh)

    @cached_property
    def run_async(self) -> RunAsyncResourceWithStreamingResponse:
        return RunAsyncResourceWithStreamingResponse(self._label.run_async)

    @cached_property
    def submit(self) -> SubmitResourceWithStreamingResponse:
        return SubmitResourceWithStreamingResponse(self._label.submit)

    @cached_property
    def update(self) -> UpdateResourceWithStreamingResponse:
        return UpdateResourceWithStreamingResponse(self._label.update)


class AsyncLabelResourceWithStreamingResponse:
    def __init__(self, label: AsyncLabelResource) -> None:
        self._label = label

    @cached_property
    def llm_assist(self) -> AsyncLlmAssistResourceWithStreamingResponse:
        return AsyncLlmAssistResourceWithStreamingResponse(self._label.llm_assist)

    @cached_property
    def refresh(self) -> AsyncRefreshResourceWithStreamingResponse:
        return AsyncRefreshResourceWithStreamingResponse(self._label.refresh)

    @cached_property
    def run_async(self) -> AsyncRunAsyncResourceWithStreamingResponse:
        return AsyncRunAsyncResourceWithStreamingResponse(self._label.run_async)

    @cached_property
    def submit(self) -> AsyncSubmitResourceWithStreamingResponse:
        return AsyncSubmitResourceWithStreamingResponse(self._label.submit)

    @cached_property
    def update(self) -> AsyncUpdateResourceWithStreamingResponse:
        return AsyncUpdateResourceWithStreamingResponse(self._label.update)
