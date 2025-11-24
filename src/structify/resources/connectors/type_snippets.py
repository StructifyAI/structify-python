# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.connectors import type_snippet_upsert_params
from ...types.connectors.snippet import Snippet

__all__ = ["TypeSnippetsResource", "AsyncTypeSnippetsResource"]


class TypeSnippetsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> TypeSnippetsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/StructifyAI/structify-python#accessing-raw-response-data-eg-headers
        """
        return TypeSnippetsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TypeSnippetsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/StructifyAI/structify-python#with_streaming_response
        """
        return TypeSnippetsResourceWithStreamingResponse(self)

    def upsert(
        self,
        connector_type: str,
        *,
        usage_snippet: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Snippet:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not connector_type:
            raise ValueError(f"Expected a non-empty value for `connector_type` but received {connector_type!r}")
        return self._put(
            f"/connector-type-snippets/{connector_type}",
            body=maybe_transform({"usage_snippet": usage_snippet}, type_snippet_upsert_params.TypeSnippetUpsertParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Snippet,
        )


class AsyncTypeSnippetsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncTypeSnippetsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/StructifyAI/structify-python#accessing-raw-response-data-eg-headers
        """
        return AsyncTypeSnippetsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTypeSnippetsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/StructifyAI/structify-python#with_streaming_response
        """
        return AsyncTypeSnippetsResourceWithStreamingResponse(self)

    async def upsert(
        self,
        connector_type: str,
        *,
        usage_snippet: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Snippet:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not connector_type:
            raise ValueError(f"Expected a non-empty value for `connector_type` but received {connector_type!r}")
        return await self._put(
            f"/connector-type-snippets/{connector_type}",
            body=await async_maybe_transform(
                {"usage_snippet": usage_snippet}, type_snippet_upsert_params.TypeSnippetUpsertParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Snippet,
        )


class TypeSnippetsResourceWithRawResponse:
    def __init__(self, type_snippets: TypeSnippetsResource) -> None:
        self._type_snippets = type_snippets

        self.upsert = to_raw_response_wrapper(
            type_snippets.upsert,
        )


class AsyncTypeSnippetsResourceWithRawResponse:
    def __init__(self, type_snippets: AsyncTypeSnippetsResource) -> None:
        self._type_snippets = type_snippets

        self.upsert = async_to_raw_response_wrapper(
            type_snippets.upsert,
        )


class TypeSnippetsResourceWithStreamingResponse:
    def __init__(self, type_snippets: TypeSnippetsResource) -> None:
        self._type_snippets = type_snippets

        self.upsert = to_streamed_response_wrapper(
            type_snippets.upsert,
        )


class AsyncTypeSnippetsResourceWithStreamingResponse:
    def __init__(self, type_snippets: AsyncTypeSnippetsResource) -> None:
        self._type_snippets = type_snippets

        self.upsert = async_to_streamed_response_wrapper(
            type_snippets.upsert,
        )
