# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional

import httpx

from ..._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...types.admin import (
    functional_test_create_params,
    functional_test_link_chat_params,
    functional_test_get_results_params,
    functional_test_update_results_params,
)
from ..._base_client import make_request_options
from ...types.admin.functional_test import FunctionalTest
from ...types.admin.functional_test_list_response import FunctionalTestListResponse
from ...types.admin.functional_test_results_response import FunctionalTestResultsResponse

__all__ = ["FunctionalTestsResource", "AsyncFunctionalTestsResource"]


class FunctionalTestsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> FunctionalTestsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/StructifyAI/structify-python#accessing-raw-response-data-eg-headers
        """
        return FunctionalTestsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> FunctionalTestsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/StructifyAI/structify-python#with_streaming_response
        """
        return FunctionalTestsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        team_id: str,
        model_override: Optional[str] | Omit = omit,
        prompt_override: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FunctionalTest:
        """
        Creates a new functional test with optional model and prompt overrides.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/admin/functional_tests/create",
            body=maybe_transform(
                {
                    "team_id": team_id,
                    "model_override": model_override,
                    "prompt_override": prompt_override,
                },
                functional_test_create_params.FunctionalTestCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FunctionalTest,
        )

    def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FunctionalTestListResponse:
        """
        Gets all functional tests with their overrides and creation dates, ordered by
        most recent first.
        """
        return self._get(
            "/admin/functional_tests/list",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FunctionalTestListResponse,
        )

    def get_results(
        self,
        *,
        functional_test_id: Optional[str] | Omit = omit,
        sample_name: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FunctionalTestResultsResponse:
        """
        Gets all results and chat IDs for either a specific functional test or a
        specific sample name. Must provide either functional_test_id or sample_name, but
        not both.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/admin/functional_tests/results",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "functional_test_id": functional_test_id,
                        "sample_name": sample_name,
                    },
                    functional_test_get_results_params.FunctionalTestGetResultsParams,
                ),
            ),
            cast_to=FunctionalTestResultsResponse,
        )

    def link_chat(
        self,
        *,
        chat_session_id: str,
        functional_test_id: str,
        results: Dict[str, object],
        sample_name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Links a chat session to a functional test with a specific sample name and
        initial results.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/admin/functional_tests/link",
            body=maybe_transform(
                {
                    "chat_session_id": chat_session_id,
                    "functional_test_id": functional_test_id,
                    "results": results,
                    "sample_name": sample_name,
                },
                functional_test_link_chat_params.FunctionalTestLinkChatParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def system_prompt(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> str:
        """Returns the current system prompt template used by the code agent."""
        extra_headers = {"Accept": "text/plain", **(extra_headers or {})}
        return self._get(
            "/admin/functional_tests/system_prompt",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=str,
        )

    def update_results(
        self,
        *,
        chat_session_id: str,
        functional_test_id: str,
        results: Dict[str, object],
        sample_name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Updates the results for a specific chat session linked to a functional test.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._put(
            "/admin/functional_tests/update_results",
            body=maybe_transform(
                {
                    "chat_session_id": chat_session_id,
                    "functional_test_id": functional_test_id,
                    "results": results,
                    "sample_name": sample_name,
                },
                functional_test_update_results_params.FunctionalTestUpdateResultsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncFunctionalTestsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncFunctionalTestsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/StructifyAI/structify-python#accessing-raw-response-data-eg-headers
        """
        return AsyncFunctionalTestsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncFunctionalTestsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/StructifyAI/structify-python#with_streaming_response
        """
        return AsyncFunctionalTestsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        team_id: str,
        model_override: Optional[str] | Omit = omit,
        prompt_override: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FunctionalTest:
        """
        Creates a new functional test with optional model and prompt overrides.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/admin/functional_tests/create",
            body=await async_maybe_transform(
                {
                    "team_id": team_id,
                    "model_override": model_override,
                    "prompt_override": prompt_override,
                },
                functional_test_create_params.FunctionalTestCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FunctionalTest,
        )

    async def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FunctionalTestListResponse:
        """
        Gets all functional tests with their overrides and creation dates, ordered by
        most recent first.
        """
        return await self._get(
            "/admin/functional_tests/list",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FunctionalTestListResponse,
        )

    async def get_results(
        self,
        *,
        functional_test_id: Optional[str] | Omit = omit,
        sample_name: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FunctionalTestResultsResponse:
        """
        Gets all results and chat IDs for either a specific functional test or a
        specific sample name. Must provide either functional_test_id or sample_name, but
        not both.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/admin/functional_tests/results",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "functional_test_id": functional_test_id,
                        "sample_name": sample_name,
                    },
                    functional_test_get_results_params.FunctionalTestGetResultsParams,
                ),
            ),
            cast_to=FunctionalTestResultsResponse,
        )

    async def link_chat(
        self,
        *,
        chat_session_id: str,
        functional_test_id: str,
        results: Dict[str, object],
        sample_name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Links a chat session to a functional test with a specific sample name and
        initial results.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/admin/functional_tests/link",
            body=await async_maybe_transform(
                {
                    "chat_session_id": chat_session_id,
                    "functional_test_id": functional_test_id,
                    "results": results,
                    "sample_name": sample_name,
                },
                functional_test_link_chat_params.FunctionalTestLinkChatParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def system_prompt(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> str:
        """Returns the current system prompt template used by the code agent."""
        extra_headers = {"Accept": "text/plain", **(extra_headers or {})}
        return await self._get(
            "/admin/functional_tests/system_prompt",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=str,
        )

    async def update_results(
        self,
        *,
        chat_session_id: str,
        functional_test_id: str,
        results: Dict[str, object],
        sample_name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Updates the results for a specific chat session linked to a functional test.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._put(
            "/admin/functional_tests/update_results",
            body=await async_maybe_transform(
                {
                    "chat_session_id": chat_session_id,
                    "functional_test_id": functional_test_id,
                    "results": results,
                    "sample_name": sample_name,
                },
                functional_test_update_results_params.FunctionalTestUpdateResultsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class FunctionalTestsResourceWithRawResponse:
    def __init__(self, functional_tests: FunctionalTestsResource) -> None:
        self._functional_tests = functional_tests

        self.create = to_raw_response_wrapper(
            functional_tests.create,
        )
        self.list = to_raw_response_wrapper(
            functional_tests.list,
        )
        self.get_results = to_raw_response_wrapper(
            functional_tests.get_results,
        )
        self.link_chat = to_raw_response_wrapper(
            functional_tests.link_chat,
        )
        self.system_prompt = to_raw_response_wrapper(
            functional_tests.system_prompt,
        )
        self.update_results = to_raw_response_wrapper(
            functional_tests.update_results,
        )


class AsyncFunctionalTestsResourceWithRawResponse:
    def __init__(self, functional_tests: AsyncFunctionalTestsResource) -> None:
        self._functional_tests = functional_tests

        self.create = async_to_raw_response_wrapper(
            functional_tests.create,
        )
        self.list = async_to_raw_response_wrapper(
            functional_tests.list,
        )
        self.get_results = async_to_raw_response_wrapper(
            functional_tests.get_results,
        )
        self.link_chat = async_to_raw_response_wrapper(
            functional_tests.link_chat,
        )
        self.system_prompt = async_to_raw_response_wrapper(
            functional_tests.system_prompt,
        )
        self.update_results = async_to_raw_response_wrapper(
            functional_tests.update_results,
        )


class FunctionalTestsResourceWithStreamingResponse:
    def __init__(self, functional_tests: FunctionalTestsResource) -> None:
        self._functional_tests = functional_tests

        self.create = to_streamed_response_wrapper(
            functional_tests.create,
        )
        self.list = to_streamed_response_wrapper(
            functional_tests.list,
        )
        self.get_results = to_streamed_response_wrapper(
            functional_tests.get_results,
        )
        self.link_chat = to_streamed_response_wrapper(
            functional_tests.link_chat,
        )
        self.system_prompt = to_streamed_response_wrapper(
            functional_tests.system_prompt,
        )
        self.update_results = to_streamed_response_wrapper(
            functional_tests.update_results,
        )


class AsyncFunctionalTestsResourceWithStreamingResponse:
    def __init__(self, functional_tests: AsyncFunctionalTestsResource) -> None:
        self._functional_tests = functional_tests

        self.create = async_to_streamed_response_wrapper(
            functional_tests.create,
        )
        self.list = async_to_streamed_response_wrapper(
            functional_tests.list,
        )
        self.get_results = async_to_streamed_response_wrapper(
            functional_tests.get_results,
        )
        self.link_chat = async_to_streamed_response_wrapper(
            functional_tests.link_chat,
        )
        self.system_prompt = async_to_streamed_response_wrapper(
            functional_tests.system_prompt,
        )
        self.update_results = async_to_streamed_response_wrapper(
            functional_tests.update_results,
        )
