# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable

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
from ...types.label import update_create_params
from ..._base_client import (
    make_request_options,
)

__all__ = ["UpdateResource", "AsyncUpdateResource"]


class UpdateResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> UpdateResourceWithRawResponse:
        return UpdateResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> UpdateResourceWithStreamingResponse:
        return UpdateResourceWithStreamingResponse(self)

    def create(
        self,
        run_idx: int,
        *,
        run_uuid: str,
        body: Iterable[update_create_params.Body],
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
        if not run_uuid:
            raise ValueError(f"Expected a non-empty value for `run_uuid` but received {run_uuid!r}")
        extra_headers = {"Accept": "text/plain", **(extra_headers or {})}
        return self._post(
            f"/label/update/{run_uuid}/{run_idx}",
            body=maybe_transform(body, update_create_params.UpdateCreateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=str,
        )


class AsyncUpdateResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncUpdateResourceWithRawResponse:
        return AsyncUpdateResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncUpdateResourceWithStreamingResponse:
        return AsyncUpdateResourceWithStreamingResponse(self)

    async def create(
        self,
        run_idx: int,
        *,
        run_uuid: str,
        body: Iterable[update_create_params.Body],
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
        if not run_uuid:
            raise ValueError(f"Expected a non-empty value for `run_uuid` but received {run_uuid!r}")
        extra_headers = {"Accept": "text/plain", **(extra_headers or {})}
        return await self._post(
            f"/label/update/{run_uuid}/{run_idx}",
            body=await async_maybe_transform(body, update_create_params.UpdateCreateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=str,
        )


class UpdateResourceWithRawResponse:
    def __init__(self, update: UpdateResource) -> None:
        self._update = update

        self.create = to_raw_response_wrapper(
            update.create,
        )


class AsyncUpdateResourceWithRawResponse:
    def __init__(self, update: AsyncUpdateResource) -> None:
        self._update = update

        self.create = async_to_raw_response_wrapper(
            update.create,
        )


class UpdateResourceWithStreamingResponse:
    def __init__(self, update: UpdateResource) -> None:
        self._update = update

        self.create = to_streamed_response_wrapper(
            update.create,
        )


class AsyncUpdateResourceWithStreamingResponse:
    def __init__(self, update: AsyncUpdateResource) -> None:
        self._update = update

        self.create = async_to_streamed_response_wrapper(
            update.create,
        )
