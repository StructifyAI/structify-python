# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .._types import Body, Query, Headers, NoneType, NotGiven, not_given
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.estimate_cost_response import EstimateCostResponse

__all__ = ["WhitelabelResource", "AsyncWhitelabelResource"]


class WhitelabelResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> WhitelabelResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/StructifyAI/structify-python#accessing-raw-response-data-eg-headers
        """
        return WhitelabelResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> WhitelabelResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/StructifyAI/structify-python#with_streaming_response
        """
        return WhitelabelResourceWithStreamingResponse(self)

    def estimate_cost(
        self,
        path: str,
        *,
        service: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EstimateCostResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not service:
            raise ValueError(f"Expected a non-empty value for `service` but received {service!r}")
        if not path:
            raise ValueError(f"Expected a non-empty value for `path` but received {path!r}")
        return self._get(
            f"/whitelabel/{service}/estimate-cost/{path}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EstimateCostResponse,
        )

    def proxy_get(
        self,
        path: str,
        *,
        service: str,
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
        if not service:
            raise ValueError(f"Expected a non-empty value for `service` but received {service!r}")
        if not path:
            raise ValueError(f"Expected a non-empty value for `path` but received {path!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._get(
            f"/whitelabel/{service}/{path}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def proxy_post(
        self,
        path: str,
        *,
        service: str,
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
        if not service:
            raise ValueError(f"Expected a non-empty value for `service` but received {service!r}")
        if not path:
            raise ValueError(f"Expected a non-empty value for `path` but received {path!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            f"/whitelabel/{service}/{path}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncWhitelabelResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncWhitelabelResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/StructifyAI/structify-python#accessing-raw-response-data-eg-headers
        """
        return AsyncWhitelabelResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncWhitelabelResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/StructifyAI/structify-python#with_streaming_response
        """
        return AsyncWhitelabelResourceWithStreamingResponse(self)

    async def estimate_cost(
        self,
        path: str,
        *,
        service: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EstimateCostResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not service:
            raise ValueError(f"Expected a non-empty value for `service` but received {service!r}")
        if not path:
            raise ValueError(f"Expected a non-empty value for `path` but received {path!r}")
        return await self._get(
            f"/whitelabel/{service}/estimate-cost/{path}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EstimateCostResponse,
        )

    async def proxy_get(
        self,
        path: str,
        *,
        service: str,
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
        if not service:
            raise ValueError(f"Expected a non-empty value for `service` but received {service!r}")
        if not path:
            raise ValueError(f"Expected a non-empty value for `path` but received {path!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._get(
            f"/whitelabel/{service}/{path}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def proxy_post(
        self,
        path: str,
        *,
        service: str,
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
        if not service:
            raise ValueError(f"Expected a non-empty value for `service` but received {service!r}")
        if not path:
            raise ValueError(f"Expected a non-empty value for `path` but received {path!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            f"/whitelabel/{service}/{path}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class WhitelabelResourceWithRawResponse:
    def __init__(self, whitelabel: WhitelabelResource) -> None:
        self._whitelabel = whitelabel

        self.estimate_cost = to_raw_response_wrapper(
            whitelabel.estimate_cost,
        )
        self.proxy_get = to_raw_response_wrapper(
            whitelabel.proxy_get,
        )
        self.proxy_post = to_raw_response_wrapper(
            whitelabel.proxy_post,
        )


class AsyncWhitelabelResourceWithRawResponse:
    def __init__(self, whitelabel: AsyncWhitelabelResource) -> None:
        self._whitelabel = whitelabel

        self.estimate_cost = async_to_raw_response_wrapper(
            whitelabel.estimate_cost,
        )
        self.proxy_get = async_to_raw_response_wrapper(
            whitelabel.proxy_get,
        )
        self.proxy_post = async_to_raw_response_wrapper(
            whitelabel.proxy_post,
        )


class WhitelabelResourceWithStreamingResponse:
    def __init__(self, whitelabel: WhitelabelResource) -> None:
        self._whitelabel = whitelabel

        self.estimate_cost = to_streamed_response_wrapper(
            whitelabel.estimate_cost,
        )
        self.proxy_get = to_streamed_response_wrapper(
            whitelabel.proxy_get,
        )
        self.proxy_post = to_streamed_response_wrapper(
            whitelabel.proxy_post,
        )


class AsyncWhitelabelResourceWithStreamingResponse:
    def __init__(self, whitelabel: AsyncWhitelabelResource) -> None:
        self._whitelabel = whitelabel

        self.estimate_cost = async_to_streamed_response_wrapper(
            whitelabel.estimate_cost,
        )
        self.proxy_get = async_to_streamed_response_wrapper(
            whitelabel.proxy_get,
        )
        self.proxy_post = async_to_streamed_response_wrapper(
            whitelabel.proxy_post,
        )
