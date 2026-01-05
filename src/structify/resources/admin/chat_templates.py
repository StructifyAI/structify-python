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
from ...types.admin import chat_template_list_params, chat_template_create_params, chat_template_update_params
from ..._base_client import make_request_options
from ...types.chat_template import ChatTemplate
from ...types.admin.chat_template_list_response import ChatTemplateListResponse

__all__ = ["ChatTemplatesResource", "AsyncChatTemplatesResource"]


class ChatTemplatesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ChatTemplatesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/StructifyAI/structify-python#accessing-raw-response-data-eg-headers
        """
        return ChatTemplatesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ChatTemplatesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/StructifyAI/structify-python#with_streaming_response
        """
        return ChatTemplatesResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        chat_session_id: str,
        description: str,
        display_order: int,
        image_url: str,
        is_active: bool,
        title: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ChatTemplate:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/admin/chat/templates",
            body=maybe_transform(
                {
                    "chat_session_id": chat_session_id,
                    "description": description,
                    "display_order": display_order,
                    "image_url": image_url,
                    "is_active": is_active,
                    "title": title,
                },
                chat_template_create_params.ChatTemplateCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ChatTemplate,
        )

    def update(
        self,
        template_id: str,
        *,
        description: Optional[str] | Omit = omit,
        display_order: Optional[int] | Omit = omit,
        image_url: Optional[str] | Omit = omit,
        is_active: Optional[bool] | Omit = omit,
        title: Optional[str] | Omit = omit,
        updated_by: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ChatTemplate:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not template_id:
            raise ValueError(f"Expected a non-empty value for `template_id` but received {template_id!r}")
        return self._patch(
            f"/admin/chat/templates/{template_id}",
            body=maybe_transform(
                {
                    "description": description,
                    "display_order": display_order,
                    "image_url": image_url,
                    "is_active": is_active,
                    "title": title,
                    "updated_by": updated_by,
                },
                chat_template_update_params.ChatTemplateUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ChatTemplate,
        )

    def list(
        self,
        *,
        chat_session_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ChatTemplateListResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/admin/chat/templates",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"chat_session_id": chat_session_id}, chat_template_list_params.ChatTemplateListParams
                ),
            ),
            cast_to=ChatTemplateListResponse,
        )


class AsyncChatTemplatesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncChatTemplatesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/StructifyAI/structify-python#accessing-raw-response-data-eg-headers
        """
        return AsyncChatTemplatesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncChatTemplatesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/StructifyAI/structify-python#with_streaming_response
        """
        return AsyncChatTemplatesResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        chat_session_id: str,
        description: str,
        display_order: int,
        image_url: str,
        is_active: bool,
        title: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ChatTemplate:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/admin/chat/templates",
            body=await async_maybe_transform(
                {
                    "chat_session_id": chat_session_id,
                    "description": description,
                    "display_order": display_order,
                    "image_url": image_url,
                    "is_active": is_active,
                    "title": title,
                },
                chat_template_create_params.ChatTemplateCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ChatTemplate,
        )

    async def update(
        self,
        template_id: str,
        *,
        description: Optional[str] | Omit = omit,
        display_order: Optional[int] | Omit = omit,
        image_url: Optional[str] | Omit = omit,
        is_active: Optional[bool] | Omit = omit,
        title: Optional[str] | Omit = omit,
        updated_by: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ChatTemplate:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not template_id:
            raise ValueError(f"Expected a non-empty value for `template_id` but received {template_id!r}")
        return await self._patch(
            f"/admin/chat/templates/{template_id}",
            body=await async_maybe_transform(
                {
                    "description": description,
                    "display_order": display_order,
                    "image_url": image_url,
                    "is_active": is_active,
                    "title": title,
                    "updated_by": updated_by,
                },
                chat_template_update_params.ChatTemplateUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ChatTemplate,
        )

    async def list(
        self,
        *,
        chat_session_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ChatTemplateListResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/admin/chat/templates",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"chat_session_id": chat_session_id}, chat_template_list_params.ChatTemplateListParams
                ),
            ),
            cast_to=ChatTemplateListResponse,
        )


class ChatTemplatesResourceWithRawResponse:
    def __init__(self, chat_templates: ChatTemplatesResource) -> None:
        self._chat_templates = chat_templates

        self.create = to_raw_response_wrapper(
            chat_templates.create,
        )
        self.update = to_raw_response_wrapper(
            chat_templates.update,
        )
        self.list = to_raw_response_wrapper(
            chat_templates.list,
        )


class AsyncChatTemplatesResourceWithRawResponse:
    def __init__(self, chat_templates: AsyncChatTemplatesResource) -> None:
        self._chat_templates = chat_templates

        self.create = async_to_raw_response_wrapper(
            chat_templates.create,
        )
        self.update = async_to_raw_response_wrapper(
            chat_templates.update,
        )
        self.list = async_to_raw_response_wrapper(
            chat_templates.list,
        )


class ChatTemplatesResourceWithStreamingResponse:
    def __init__(self, chat_templates: ChatTemplatesResource) -> None:
        self._chat_templates = chat_templates

        self.create = to_streamed_response_wrapper(
            chat_templates.create,
        )
        self.update = to_streamed_response_wrapper(
            chat_templates.update,
        )
        self.list = to_streamed_response_wrapper(
            chat_templates.list,
        )


class AsyncChatTemplatesResourceWithStreamingResponse:
    def __init__(self, chat_templates: AsyncChatTemplatesResource) -> None:
        self._chat_templates = chat_templates

        self.create = async_to_streamed_response_wrapper(
            chat_templates.create,
        )
        self.update = async_to_streamed_response_wrapper(
            chat_templates.update,
        )
        self.list = async_to_streamed_response_wrapper(
            chat_templates.list,
        )
