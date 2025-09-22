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
from ...types.external import news_sources_params, news_everything_params, news_top_headlines_params
from ...types.external.sources_response import SourcesResponse
from ...types.external.everything_response import EverythingResponse
from ...types.external.top_headlines_response import TopHeadlinesResponse

__all__ = ["NewsResource", "AsyncNewsResource"]


class NewsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> NewsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/StructifyAI/structify-python#accessing-raw-response-data-eg-headers
        """
        return NewsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> NewsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/StructifyAI/structify-python#with_streaming_response
        """
        return NewsResourceWithStreamingResponse(self)

    def everything(
        self,
        *,
        domains: Optional[str] | Omit = omit,
        exclude_domains: Optional[str] | Omit = omit,
        from_: Optional[str] | Omit = omit,
        language: Optional[str] | Omit = omit,
        page: Optional[int] | Omit = omit,
        page_size: Optional[int] | Omit = omit,
        q: Optional[str] | Omit = omit,
        q_in_title: Optional[str] | Omit = omit,
        sort_by: Optional[str] | Omit = omit,
        sources: Optional[str] | Omit = omit,
        to: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EverythingResponse:
        """
        Search through millions of articles from over 80,000 large and small news
        sources and blogs

        Args:
          domains: Comma-separated domains

          exclude_domains: Domains to exclude

          from_: Oldest article date (ISO 8601)

          language: Language code (ISO 639-1)

          page: Page number

          page_size: Results per page (max 100)

          q: Keywords

          q_in_title: Keywords in title only

          sort_by: Sort order

          sources: Comma-separated sources

          to: Newest article date (ISO 8601)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/external/news/everything",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "domains": domains,
                        "exclude_domains": exclude_domains,
                        "from_": from_,
                        "language": language,
                        "page": page,
                        "page_size": page_size,
                        "q": q,
                        "q_in_title": q_in_title,
                        "sort_by": sort_by,
                        "sources": sources,
                        "to": to,
                    },
                    news_everything_params.NewsEverythingParams,
                ),
            ),
            cast_to=EverythingResponse,
        )

    def sources(
        self,
        *,
        category: Optional[str] | Omit = omit,
        country: Optional[str] | Omit = omit,
        language: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SourcesResponse:
        """
        Returns the subset of news publishers that top headlines are available from

        Args:
          category: News category

          country: Country code

          language: Language code

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/external/news/sources",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "category": category,
                        "country": country,
                        "language": language,
                    },
                    news_sources_params.NewsSourcesParams,
                ),
            ),
            cast_to=SourcesResponse,
        )

    def top_headlines(
        self,
        *,
        category: Optional[str] | Omit = omit,
        country: Optional[str] | Omit = omit,
        page: Optional[int] | Omit = omit,
        page_size: Optional[int] | Omit = omit,
        q: Optional[str] | Omit = omit,
        sources: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TopHeadlinesResponse:
        """
        Provides live top and breaking headlines for a country, specific category, or
        specific sources

        Args:
          category: Category

          country: Country code (ISO 3166-1)

          page: Page number

          page_size: Results per page (max 100)

          q: Keywords

          sources: Comma-separated sources

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/external/news/top-headlines",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "category": category,
                        "country": country,
                        "page": page,
                        "page_size": page_size,
                        "q": q,
                        "sources": sources,
                    },
                    news_top_headlines_params.NewsTopHeadlinesParams,
                ),
            ),
            cast_to=TopHeadlinesResponse,
        )


class AsyncNewsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncNewsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/StructifyAI/structify-python#accessing-raw-response-data-eg-headers
        """
        return AsyncNewsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncNewsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/StructifyAI/structify-python#with_streaming_response
        """
        return AsyncNewsResourceWithStreamingResponse(self)

    async def everything(
        self,
        *,
        domains: Optional[str] | Omit = omit,
        exclude_domains: Optional[str] | Omit = omit,
        from_: Optional[str] | Omit = omit,
        language: Optional[str] | Omit = omit,
        page: Optional[int] | Omit = omit,
        page_size: Optional[int] | Omit = omit,
        q: Optional[str] | Omit = omit,
        q_in_title: Optional[str] | Omit = omit,
        sort_by: Optional[str] | Omit = omit,
        sources: Optional[str] | Omit = omit,
        to: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EverythingResponse:
        """
        Search through millions of articles from over 80,000 large and small news
        sources and blogs

        Args:
          domains: Comma-separated domains

          exclude_domains: Domains to exclude

          from_: Oldest article date (ISO 8601)

          language: Language code (ISO 639-1)

          page: Page number

          page_size: Results per page (max 100)

          q: Keywords

          q_in_title: Keywords in title only

          sort_by: Sort order

          sources: Comma-separated sources

          to: Newest article date (ISO 8601)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/external/news/everything",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "domains": domains,
                        "exclude_domains": exclude_domains,
                        "from_": from_,
                        "language": language,
                        "page": page,
                        "page_size": page_size,
                        "q": q,
                        "q_in_title": q_in_title,
                        "sort_by": sort_by,
                        "sources": sources,
                        "to": to,
                    },
                    news_everything_params.NewsEverythingParams,
                ),
            ),
            cast_to=EverythingResponse,
        )

    async def sources(
        self,
        *,
        category: Optional[str] | Omit = omit,
        country: Optional[str] | Omit = omit,
        language: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SourcesResponse:
        """
        Returns the subset of news publishers that top headlines are available from

        Args:
          category: News category

          country: Country code

          language: Language code

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/external/news/sources",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "category": category,
                        "country": country,
                        "language": language,
                    },
                    news_sources_params.NewsSourcesParams,
                ),
            ),
            cast_to=SourcesResponse,
        )

    async def top_headlines(
        self,
        *,
        category: Optional[str] | Omit = omit,
        country: Optional[str] | Omit = omit,
        page: Optional[int] | Omit = omit,
        page_size: Optional[int] | Omit = omit,
        q: Optional[str] | Omit = omit,
        sources: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TopHeadlinesResponse:
        """
        Provides live top and breaking headlines for a country, specific category, or
        specific sources

        Args:
          category: Category

          country: Country code (ISO 3166-1)

          page: Page number

          page_size: Results per page (max 100)

          q: Keywords

          sources: Comma-separated sources

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/external/news/top-headlines",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "category": category,
                        "country": country,
                        "page": page,
                        "page_size": page_size,
                        "q": q,
                        "sources": sources,
                    },
                    news_top_headlines_params.NewsTopHeadlinesParams,
                ),
            ),
            cast_to=TopHeadlinesResponse,
        )


class NewsResourceWithRawResponse:
    def __init__(self, news: NewsResource) -> None:
        self._news = news

        self.everything = to_raw_response_wrapper(
            news.everything,
        )
        self.sources = to_raw_response_wrapper(
            news.sources,
        )
        self.top_headlines = to_raw_response_wrapper(
            news.top_headlines,
        )


class AsyncNewsResourceWithRawResponse:
    def __init__(self, news: AsyncNewsResource) -> None:
        self._news = news

        self.everything = async_to_raw_response_wrapper(
            news.everything,
        )
        self.sources = async_to_raw_response_wrapper(
            news.sources,
        )
        self.top_headlines = async_to_raw_response_wrapper(
            news.top_headlines,
        )


class NewsResourceWithStreamingResponse:
    def __init__(self, news: NewsResource) -> None:
        self._news = news

        self.everything = to_streamed_response_wrapper(
            news.everything,
        )
        self.sources = to_streamed_response_wrapper(
            news.sources,
        )
        self.top_headlines = to_streamed_response_wrapper(
            news.top_headlines,
        )


class AsyncNewsResourceWithStreamingResponse:
    def __init__(self, news: AsyncNewsResource) -> None:
        self._news = news

        self.everything = async_to_streamed_response_wrapper(
            news.everything,
        )
        self.sources = async_to_streamed_response_wrapper(
            news.sources,
        )
        self.top_headlines = async_to_streamed_response_wrapper(
            news.top_headlines,
        )
