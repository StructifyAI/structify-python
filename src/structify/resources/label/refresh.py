# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

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
from ...types.label import refresh_retrieve_params
from ..._base_client import (
    make_request_options,
)
from ...types.label.refresh_response import RefreshResponse

__all__ = ["RefreshResource", "AsyncRefreshResource"]


class RefreshResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> RefreshResourceWithRawResponse:
        return RefreshResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RefreshResourceWithStreamingResponse:
        return RefreshResourceWithStreamingResponse(self)

    def retrieve(
        self,
        *,
        uuid: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[RefreshResponse]:
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
                query=maybe_transform({"uuid": uuid}, refresh_retrieve_params.RefreshRetrieveParams),
            ),
            cast_to=RefreshResponse,
        )


class AsyncRefreshResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncRefreshResourceWithRawResponse:
        return AsyncRefreshResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRefreshResourceWithStreamingResponse:
        return AsyncRefreshResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        *,
        uuid: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[RefreshResponse]:
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
                query=await async_maybe_transform({"uuid": uuid}, refresh_retrieve_params.RefreshRetrieveParams),
            ),
            cast_to=RefreshResponse,
        )


class RefreshResourceWithRawResponse:
    def __init__(self, refresh: RefreshResource) -> None:
        self._refresh = refresh

        self.retrieve = to_raw_response_wrapper(
            refresh.retrieve,
        )


class AsyncRefreshResourceWithRawResponse:
    def __init__(self, refresh: AsyncRefreshResource) -> None:
        self._refresh = refresh

        self.retrieve = async_to_raw_response_wrapper(
            refresh.retrieve,
        )


class RefreshResourceWithStreamingResponse:
    def __init__(self, refresh: RefreshResource) -> None:
        self._refresh = refresh

        self.retrieve = to_streamed_response_wrapper(
            refresh.retrieve,
        )


class AsyncRefreshResourceWithStreamingResponse:
    def __init__(self, refresh: AsyncRefreshResource) -> None:
        self._refresh = refresh

        self.retrieve = async_to_streamed_response_wrapper(
            refresh.retrieve,
        )
