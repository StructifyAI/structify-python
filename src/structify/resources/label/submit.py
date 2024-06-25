# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import (
    maybe_transform,
    async_maybe_transform,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...types.label import submit_create_params
from ..._base_client import (
    make_request_options,
)
from ...types.label.tool_input_param import ToolInputParam

__all__ = ["SubmitResource", "AsyncSubmitResource"]


class SubmitResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SubmitResourceWithRawResponse:
        return SubmitResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SubmitResourceWithStreamingResponse:
        return SubmitResourceWithStreamingResponse(self)

    def create(
        self,
        uuid: str,
        *,
        body: Optional[Iterable[ToolInputParam]],
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
            body=maybe_transform(body, submit_create_params.SubmitCreateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=str,
        )


class AsyncSubmitResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSubmitResourceWithRawResponse:
        return AsyncSubmitResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSubmitResourceWithStreamingResponse:
        return AsyncSubmitResourceWithStreamingResponse(self)

    async def create(
        self,
        uuid: str,
        *,
        body: Optional[Iterable[ToolInputParam]],
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
            body=await async_maybe_transform(body, submit_create_params.SubmitCreateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=str,
        )


class SubmitResourceWithRawResponse:
    def __init__(self, submit: SubmitResource) -> None:
        self._submit = submit

        self.create = to_raw_response_wrapper(
            submit.create,
        )


class AsyncSubmitResourceWithRawResponse:
    def __init__(self, submit: AsyncSubmitResource) -> None:
        self._submit = submit

        self.create = async_to_raw_response_wrapper(
            submit.create,
        )


class SubmitResourceWithStreamingResponse:
    def __init__(self, submit: SubmitResource) -> None:
        self._submit = submit

        self.create = to_streamed_response_wrapper(
            submit.create,
        )


class AsyncSubmitResourceWithStreamingResponse:
    def __init__(self, submit: AsyncSubmitResource) -> None:
        self._submit = submit

        self.create = async_to_streamed_response_wrapper(
            submit.create,
        )
