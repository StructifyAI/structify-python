# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

import httpx

from ..types import SignedUploadTarget, upload_init_params, upload_complete_params
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from .._utils import maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.signed_upload_target import SignedUploadTarget
from ..types.signed_upload_init_response import SignedUploadInitResponse
from ..types.signed_upload_complete_response import SignedUploadCompleteResponse

__all__ = ["UploadsResource", "AsyncUploadsResource"]


class UploadsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> UploadsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/StructifyAI/structify-python#accessing-raw-response-data-eg-headers
        """
        return UploadsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> UploadsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/StructifyAI/structify-python#with_streaming_response
        """
        return UploadsResourceWithStreamingResponse(self)

    def complete(
        self,
        *,
        blob_name: str,
        content_type: str,
        target: SignedUploadTarget,
        cache_final_rows: Optional[int] | Omit = omit,
        cache_final_size_bytes: Optional[int] | Omit = omit,
        cache_max_bytes: Optional[int] | Omit = omit,
        cache_original_rows: Optional[int] | Omit = omit,
        cache_original_size_bytes: Optional[int] | Omit = omit,
        cache_truncated: Optional[bool] | Omit = omit,
        chat_id: Optional[str] | Omit = omit,
        file_name: Optional[str] | Omit = omit,
        node_id: Optional[str] | Omit = omit,
        output_schema: object | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SignedUploadCompleteResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/chat/input-files/upload/complete",
            body=maybe_transform(
                {
                    "blob_name": blob_name,
                    "content_type": content_type,
                    "target": target,
                    "cache_final_rows": cache_final_rows,
                    "cache_final_size_bytes": cache_final_size_bytes,
                    "cache_max_bytes": cache_max_bytes,
                    "cache_original_rows": cache_original_rows,
                    "cache_original_size_bytes": cache_original_size_bytes,
                    "cache_truncated": cache_truncated,
                    "chat_id": chat_id,
                    "file_name": file_name,
                    "node_id": node_id,
                    "output_schema": output_schema,
                },
                upload_complete_params.UploadCompleteParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SignedUploadCompleteResponse,
        )

    def init(
        self,
        *,
        content_type: str,
        file_size: int,
        target: SignedUploadTarget,
        chat_id: Optional[str] | Omit = omit,
        node_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SignedUploadInitResponse:
        """
        Upload an input file to a chat session's bucket storage

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/chat/input-files/upload/init",
            body=maybe_transform(
                {
                    "content_type": content_type,
                    "file_size": file_size,
                    "target": target,
                    "chat_id": chat_id,
                    "node_id": node_id,
                },
                upload_init_params.UploadInitParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SignedUploadInitResponse,
        )


class AsyncUploadsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncUploadsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/StructifyAI/structify-python#accessing-raw-response-data-eg-headers
        """
        return AsyncUploadsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncUploadsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/StructifyAI/structify-python#with_streaming_response
        """
        return AsyncUploadsResourceWithStreamingResponse(self)

    async def complete(
        self,
        *,
        blob_name: str,
        content_type: str,
        target: SignedUploadTarget,
        cache_final_rows: Optional[int] | Omit = omit,
        cache_final_size_bytes: Optional[int] | Omit = omit,
        cache_max_bytes: Optional[int] | Omit = omit,
        cache_original_rows: Optional[int] | Omit = omit,
        cache_original_size_bytes: Optional[int] | Omit = omit,
        cache_truncated: Optional[bool] | Omit = omit,
        chat_id: Optional[str] | Omit = omit,
        file_name: Optional[str] | Omit = omit,
        node_id: Optional[str] | Omit = omit,
        output_schema: object | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SignedUploadCompleteResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/chat/input-files/upload/complete",
            body=await async_maybe_transform(
                {
                    "blob_name": blob_name,
                    "content_type": content_type,
                    "target": target,
                    "cache_final_rows": cache_final_rows,
                    "cache_final_size_bytes": cache_final_size_bytes,
                    "cache_max_bytes": cache_max_bytes,
                    "cache_original_rows": cache_original_rows,
                    "cache_original_size_bytes": cache_original_size_bytes,
                    "cache_truncated": cache_truncated,
                    "chat_id": chat_id,
                    "file_name": file_name,
                    "node_id": node_id,
                    "output_schema": output_schema,
                },
                upload_complete_params.UploadCompleteParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SignedUploadCompleteResponse,
        )

    async def init(
        self,
        *,
        content_type: str,
        file_size: int,
        target: SignedUploadTarget,
        chat_id: Optional[str] | Omit = omit,
        node_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SignedUploadInitResponse:
        """
        Upload an input file to a chat session's bucket storage

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/chat/input-files/upload/init",
            body=await async_maybe_transform(
                {
                    "content_type": content_type,
                    "file_size": file_size,
                    "target": target,
                    "chat_id": chat_id,
                    "node_id": node_id,
                },
                upload_init_params.UploadInitParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SignedUploadInitResponse,
        )


class UploadsResourceWithRawResponse:
    def __init__(self, uploads: UploadsResource) -> None:
        self._uploads = uploads

        self.complete = to_raw_response_wrapper(
            uploads.complete,
        )
        self.init = to_raw_response_wrapper(
            uploads.init,
        )


class AsyncUploadsResourceWithRawResponse:
    def __init__(self, uploads: AsyncUploadsResource) -> None:
        self._uploads = uploads

        self.complete = async_to_raw_response_wrapper(
            uploads.complete,
        )
        self.init = async_to_raw_response_wrapper(
            uploads.init,
        )


class UploadsResourceWithStreamingResponse:
    def __init__(self, uploads: UploadsResource) -> None:
        self._uploads = uploads

        self.complete = to_streamed_response_wrapper(
            uploads.complete,
        )
        self.init = to_streamed_response_wrapper(
            uploads.init,
        )


class AsyncUploadsResourceWithStreamingResponse:
    def __init__(self, uploads: AsyncUploadsResource) -> None:
        self._uploads = uploads

        self.complete = async_to_streamed_response_wrapper(
            uploads.complete,
        )
        self.init = async_to_streamed_response_wrapper(
            uploads.init,
        )
