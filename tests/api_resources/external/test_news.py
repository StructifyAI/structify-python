# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from structify import Structify, AsyncStructify
from tests.utils import assert_matches_type
from structify.types.external import (
    SourcesResponse,
    EverythingResponse,
    TopHeadlinesResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestNews:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_everything(self, client: Structify) -> None:
        news = client.external.news.everything()
        assert_matches_type(EverythingResponse, news, path=["response"])

    @parametrize
    def test_method_everything_with_all_params(self, client: Structify) -> None:
        news = client.external.news.everything(
            domains="domains",
            exclude_domains="exclude_domains",
            from_="from",
            language="language",
            page=0,
            page_size=0,
            q="q",
            q_in_title="q_in_title",
            sort_by="sort_by",
            sources="sources",
            to="to",
        )
        assert_matches_type(EverythingResponse, news, path=["response"])

    @parametrize
    def test_raw_response_everything(self, client: Structify) -> None:
        response = client.external.news.with_raw_response.everything()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        news = response.parse()
        assert_matches_type(EverythingResponse, news, path=["response"])

    @parametrize
    def test_streaming_response_everything(self, client: Structify) -> None:
        with client.external.news.with_streaming_response.everything() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            news = response.parse()
            assert_matches_type(EverythingResponse, news, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_sources(self, client: Structify) -> None:
        news = client.external.news.sources()
        assert_matches_type(SourcesResponse, news, path=["response"])

    @parametrize
    def test_method_sources_with_all_params(self, client: Structify) -> None:
        news = client.external.news.sources(
            category="category",
            country="country",
            language="language",
        )
        assert_matches_type(SourcesResponse, news, path=["response"])

    @parametrize
    def test_raw_response_sources(self, client: Structify) -> None:
        response = client.external.news.with_raw_response.sources()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        news = response.parse()
        assert_matches_type(SourcesResponse, news, path=["response"])

    @parametrize
    def test_streaming_response_sources(self, client: Structify) -> None:
        with client.external.news.with_streaming_response.sources() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            news = response.parse()
            assert_matches_type(SourcesResponse, news, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_top_headlines(self, client: Structify) -> None:
        news = client.external.news.top_headlines()
        assert_matches_type(TopHeadlinesResponse, news, path=["response"])

    @parametrize
    def test_method_top_headlines_with_all_params(self, client: Structify) -> None:
        news = client.external.news.top_headlines(
            category="category",
            country="country",
            page=0,
            page_size=0,
            q="q",
            sources="sources",
        )
        assert_matches_type(TopHeadlinesResponse, news, path=["response"])

    @parametrize
    def test_raw_response_top_headlines(self, client: Structify) -> None:
        response = client.external.news.with_raw_response.top_headlines()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        news = response.parse()
        assert_matches_type(TopHeadlinesResponse, news, path=["response"])

    @parametrize
    def test_streaming_response_top_headlines(self, client: Structify) -> None:
        with client.external.news.with_streaming_response.top_headlines() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            news = response.parse()
            assert_matches_type(TopHeadlinesResponse, news, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncNews:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_everything(self, async_client: AsyncStructify) -> None:
        news = await async_client.external.news.everything()
        assert_matches_type(EverythingResponse, news, path=["response"])

    @parametrize
    async def test_method_everything_with_all_params(self, async_client: AsyncStructify) -> None:
        news = await async_client.external.news.everything(
            domains="domains",
            exclude_domains="exclude_domains",
            from_="from",
            language="language",
            page=0,
            page_size=0,
            q="q",
            q_in_title="q_in_title",
            sort_by="sort_by",
            sources="sources",
            to="to",
        )
        assert_matches_type(EverythingResponse, news, path=["response"])

    @parametrize
    async def test_raw_response_everything(self, async_client: AsyncStructify) -> None:
        response = await async_client.external.news.with_raw_response.everything()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        news = await response.parse()
        assert_matches_type(EverythingResponse, news, path=["response"])

    @parametrize
    async def test_streaming_response_everything(self, async_client: AsyncStructify) -> None:
        async with async_client.external.news.with_streaming_response.everything() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            news = await response.parse()
            assert_matches_type(EverythingResponse, news, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_sources(self, async_client: AsyncStructify) -> None:
        news = await async_client.external.news.sources()
        assert_matches_type(SourcesResponse, news, path=["response"])

    @parametrize
    async def test_method_sources_with_all_params(self, async_client: AsyncStructify) -> None:
        news = await async_client.external.news.sources(
            category="category",
            country="country",
            language="language",
        )
        assert_matches_type(SourcesResponse, news, path=["response"])

    @parametrize
    async def test_raw_response_sources(self, async_client: AsyncStructify) -> None:
        response = await async_client.external.news.with_raw_response.sources()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        news = await response.parse()
        assert_matches_type(SourcesResponse, news, path=["response"])

    @parametrize
    async def test_streaming_response_sources(self, async_client: AsyncStructify) -> None:
        async with async_client.external.news.with_streaming_response.sources() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            news = await response.parse()
            assert_matches_type(SourcesResponse, news, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_top_headlines(self, async_client: AsyncStructify) -> None:
        news = await async_client.external.news.top_headlines()
        assert_matches_type(TopHeadlinesResponse, news, path=["response"])

    @parametrize
    async def test_method_top_headlines_with_all_params(self, async_client: AsyncStructify) -> None:
        news = await async_client.external.news.top_headlines(
            category="category",
            country="country",
            page=0,
            page_size=0,
            q="q",
            sources="sources",
        )
        assert_matches_type(TopHeadlinesResponse, news, path=["response"])

    @parametrize
    async def test_raw_response_top_headlines(self, async_client: AsyncStructify) -> None:
        response = await async_client.external.news.with_raw_response.top_headlines()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        news = await response.parse()
        assert_matches_type(TopHeadlinesResponse, news, path=["response"])

    @parametrize
    async def test_streaming_response_top_headlines(self, async_client: AsyncStructify) -> None:
        async with async_client.external.news.with_streaming_response.top_headlines() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            news = await response.parse()
            assert_matches_type(TopHeadlinesResponse, news, path=["response"])

        assert cast(Any, response.is_closed) is True
