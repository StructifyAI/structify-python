# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional

import httpx

from ..types import label_run_params, label_submit_params, label_get_messages_params
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import (
    maybe_transform,
    async_maybe_transform,
)
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.knowledge_graph_param import KnowledgeGraphParam
from ..types.label_llm_assist_response import LabelLlmAssistResponse
from ..types.label_get_messages_response import LabelGetMessagesResponse

__all__ = ["LabelResource", "AsyncLabelResource"]


class LabelResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> LabelResourceWithRawResponse:
        return LabelResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> LabelResourceWithStreamingResponse:
        return LabelResourceWithStreamingResponse(self)

    def get_messages(
        self,
        *,
        uuid: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[LabelGetMessagesResponse]:
        """
        web requests that would be cancelled by cloudflare in prod.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/label/refresh",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"uuid": uuid}, label_get_messages_params.LabelGetMessagesParams),
            ),
            cast_to=LabelGetMessagesResponse,
        )

    def llm_assist(
        self,
        uuid: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> LabelLlmAssistResponse:
        """
        web requests that would be cancelled by cloudflare in prod.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not uuid:
            raise ValueError(f"Expected a non-empty value for `uuid` but received {uuid!r}")
        return self._get(
            f"/label/llm_assist/{uuid}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LabelLlmAssistResponse,
        )

    def run(
        self,
        *,
        dataset_name: str,
        structure_input: label_run_params.StructureInput,
        seeded_entity: KnowledgeGraphParam | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> str:
        """
        Returns a token that can be waited on until the request is finished.

        Args:
          structure_input: These are all the types that can be converted into a BasicInputType

          seeded_entity: Knowledge graph info structured to deserialize and display in the same format
              that the LLM outputs. Also the first representation of an LLM output in the
              pipeline from raw tool output to being merged into a Neo4j DB

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "text/plain", **(extra_headers or {})}
        return self._post(
            "/label/run_async",
            body=maybe_transform(
                {
                    "dataset_name": dataset_name,
                    "structure_input": structure_input,
                    "seeded_entity": seeded_entity,
                },
                label_run_params.LabelRunParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=str,
        )

    def submit(
        self,
        uuid: str,
        *,
        label: Optional[Iterable[label_submit_params.Label]],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> str:
        """
        Submit a label as part of the human LLM.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not uuid:
            raise ValueError(f"Expected a non-empty value for `uuid` but received {uuid!r}")
        extra_headers = {"Accept": "text/plain", **(extra_headers or {})}
        return self._post(
            f"/label/submit/{uuid}",
            body=maybe_transform(label, label_submit_params.LabelSubmitParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=str,
        )


class AsyncLabelResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncLabelResourceWithRawResponse:
        return AsyncLabelResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncLabelResourceWithStreamingResponse:
        return AsyncLabelResourceWithStreamingResponse(self)

    async def get_messages(
        self,
        *,
        uuid: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[LabelGetMessagesResponse]:
        """
        web requests that would be cancelled by cloudflare in prod.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/label/refresh",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"uuid": uuid}, label_get_messages_params.LabelGetMessagesParams),
            ),
            cast_to=LabelGetMessagesResponse,
        )

    async def llm_assist(
        self,
        uuid: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> LabelLlmAssistResponse:
        """
        web requests that would be cancelled by cloudflare in prod.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not uuid:
            raise ValueError(f"Expected a non-empty value for `uuid` but received {uuid!r}")
        return await self._get(
            f"/label/llm_assist/{uuid}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LabelLlmAssistResponse,
        )

    async def run(
        self,
        *,
        dataset_name: str,
        structure_input: label_run_params.StructureInput,
        seeded_entity: KnowledgeGraphParam | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> str:
        """
        Returns a token that can be waited on until the request is finished.

        Args:
          structure_input: These are all the types that can be converted into a BasicInputType

          seeded_entity: Knowledge graph info structured to deserialize and display in the same format
              that the LLM outputs. Also the first representation of an LLM output in the
              pipeline from raw tool output to being merged into a Neo4j DB

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "text/plain", **(extra_headers or {})}
        return await self._post(
            "/label/run_async",
            body=await async_maybe_transform(
                {
                    "dataset_name": dataset_name,
                    "structure_input": structure_input,
                    "seeded_entity": seeded_entity,
                },
                label_run_params.LabelRunParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=str,
        )

    async def submit(
        self,
        uuid: str,
        *,
        label: Optional[Iterable[label_submit_params.Label]],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> str:
        """
        Submit a label as part of the human LLM.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not uuid:
            raise ValueError(f"Expected a non-empty value for `uuid` but received {uuid!r}")
        extra_headers = {"Accept": "text/plain", **(extra_headers or {})}
        return await self._post(
            f"/label/submit/{uuid}",
            body=await async_maybe_transform(label, label_submit_params.LabelSubmitParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=str,
        )


class LabelResourceWithRawResponse:
    def __init__(self, label: LabelResource) -> None:
        self._label = label

        self.get_messages = to_raw_response_wrapper(
            label.get_messages,
        )
        self.llm_assist = to_raw_response_wrapper(
            label.llm_assist,
        )
        self.run = to_raw_response_wrapper(
            label.run,
        )
        self.submit = to_raw_response_wrapper(
            label.submit,
        )


class AsyncLabelResourceWithRawResponse:
    def __init__(self, label: AsyncLabelResource) -> None:
        self._label = label

        self.get_messages = async_to_raw_response_wrapper(
            label.get_messages,
        )
        self.llm_assist = async_to_raw_response_wrapper(
            label.llm_assist,
        )
        self.run = async_to_raw_response_wrapper(
            label.run,
        )
        self.submit = async_to_raw_response_wrapper(
            label.submit,
        )


class LabelResourceWithStreamingResponse:
    def __init__(self, label: LabelResource) -> None:
        self._label = label

        self.get_messages = to_streamed_response_wrapper(
            label.get_messages,
        )
        self.llm_assist = to_streamed_response_wrapper(
            label.llm_assist,
        )
        self.run = to_streamed_response_wrapper(
            label.run,
        )
        self.submit = to_streamed_response_wrapper(
            label.submit,
        )


class AsyncLabelResourceWithStreamingResponse:
    def __init__(self, label: AsyncLabelResource) -> None:
        self._label = label

        self.get_messages = async_to_streamed_response_wrapper(
            label.get_messages,
        )
        self.llm_assist = async_to_streamed_response_wrapper(
            label.llm_assist,
        )
        self.run = async_to_streamed_response_wrapper(
            label.run,
        )
        self.submit = async_to_streamed_response_wrapper(
            label.submit,
        )
