# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

import httpx

from ..types import code_generate_code_params
from .._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
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

__all__ = ["CodeResource", "AsyncCodeResource"]


class CodeResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CodeResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/StructifyAI/structify-python#accessing-raw-response-data-eg-headers
        """
        return CodeResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CodeResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/StructifyAI/structify-python#with_streaming_response
        """
        return CodeResourceWithStreamingResponse(self)

    def generate_code(
        self,
        *,
        chat_session_id: str,
        prompt: str,
        message_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Protocol:

        - event: `chat_event` — data is a JSON object, one of (serde external-tagged
          enum):
        - `{ "TextMessage": { "message": string } }`
        - `{ "Connector": { "name": string, "description"?: string, "env_vars": string[] } }`
        - `{ "Thinking": { "content": string } }`
        - `{ "File": { "path": string, "content"?: string } }`
        - `{ "Action": { "actions": Array<{ name: string, description: string }> } }`
        - `{ "ToolCall": { "name": string, "input": any, "result_id"?: string, "result_text"?: string } }`
        - event: `error` — data is a JSON object: `{ "message": string }` describing the
          error.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/code/generate-code",
            body=maybe_transform(
                {
                    "chat_session_id": chat_session_id,
                    "prompt": prompt,
                    "message_id": message_id,
                },
                code_generate_code_params.CodeGenerateCodeParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncCodeResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCodeResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/StructifyAI/structify-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCodeResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCodeResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/StructifyAI/structify-python#with_streaming_response
        """
        return AsyncCodeResourceWithStreamingResponse(self)

    async def generate_code(
        self,
        *,
        chat_session_id: str,
        prompt: str,
        message_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Protocol:

        - event: `chat_event` — data is a JSON object, one of (serde external-tagged
          enum):
        - `{ "TextMessage": { "message": string } }`
        - `{ "Connector": { "name": string, "description"?: string, "env_vars": string[] } }`
        - `{ "Thinking": { "content": string } }`
        - `{ "File": { "path": string, "content"?: string } }`
        - `{ "Action": { "actions": Array<{ name: string, description: string }> } }`
        - `{ "ToolCall": { "name": string, "input": any, "result_id"?: string, "result_text"?: string } }`
        - event: `error` — data is a JSON object: `{ "message": string }` describing the
          error.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/code/generate-code",
            body=await async_maybe_transform(
                {
                    "chat_session_id": chat_session_id,
                    "prompt": prompt,
                    "message_id": message_id,
                },
                code_generate_code_params.CodeGenerateCodeParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class CodeResourceWithRawResponse:
    def __init__(self, code: CodeResource) -> None:
        self._code = code

        self.generate_code = to_raw_response_wrapper(
            code.generate_code,
        )


class AsyncCodeResourceWithRawResponse:
    def __init__(self, code: AsyncCodeResource) -> None:
        self._code = code

        self.generate_code = async_to_raw_response_wrapper(
            code.generate_code,
        )


class CodeResourceWithStreamingResponse:
    def __init__(self, code: CodeResource) -> None:
        self._code = code

        self.generate_code = to_streamed_response_wrapper(
            code.generate_code,
        )


class AsyncCodeResourceWithStreamingResponse:
    def __init__(self, code: AsyncCodeResource) -> None:
        self._code = code

        self.generate_code = async_to_streamed_response_wrapper(
            code.generate_code,
        )
