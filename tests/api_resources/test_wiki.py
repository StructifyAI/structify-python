# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from structify import Structify, AsyncStructify
from tests.utils import assert_matches_type
from structify.types import (
    TeamWikiPage,
    WikiListResponse,
    WikiPageWithReferences,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestWiki:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Structify) -> None:
        wiki = client.wiki.create(
            team_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            content={"foo": "bar"},
            slug="slug",
            title="title",
        )
        assert_matches_type(TeamWikiPage, wiki, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Structify) -> None:
        response = client.wiki.with_raw_response.create(
            team_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            content={"foo": "bar"},
            slug="slug",
            title="title",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        wiki = response.parse()
        assert_matches_type(TeamWikiPage, wiki, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Structify) -> None:
        with client.wiki.with_streaming_response.create(
            team_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            content={"foo": "bar"},
            slug="slug",
            title="title",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            wiki = response.parse()
            assert_matches_type(TeamWikiPage, wiki, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: Structify) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `team_id` but received ''"):
            client.wiki.with_raw_response.create(
                team_id="",
                content={"foo": "bar"},
                slug="slug",
                title="title",
            )

    @parametrize
    def test_method_update(self, client: Structify) -> None:
        wiki = client.wiki.update(
            slug="slug",
            team_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            content={"foo": "bar"},
        )
        assert_matches_type(TeamWikiPage, wiki, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Structify) -> None:
        wiki = client.wiki.update(
            slug="slug",
            team_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            content={"foo": "bar"},
            title="title",
        )
        assert_matches_type(TeamWikiPage, wiki, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Structify) -> None:
        response = client.wiki.with_raw_response.update(
            slug="slug",
            team_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            content={"foo": "bar"},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        wiki = response.parse()
        assert_matches_type(TeamWikiPage, wiki, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Structify) -> None:
        with client.wiki.with_streaming_response.update(
            slug="slug",
            team_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            content={"foo": "bar"},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            wiki = response.parse()
            assert_matches_type(TeamWikiPage, wiki, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Structify) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `team_id` but received ''"):
            client.wiki.with_raw_response.update(
                slug="slug",
                team_id="",
                content={"foo": "bar"},
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `slug` but received ''"):
            client.wiki.with_raw_response.update(
                slug="",
                team_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                content={"foo": "bar"},
            )

    @parametrize
    def test_method_list(self, client: Structify) -> None:
        wiki = client.wiki.list(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(WikiListResponse, wiki, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Structify) -> None:
        response = client.wiki.with_raw_response.list(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        wiki = response.parse()
        assert_matches_type(WikiListResponse, wiki, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Structify) -> None:
        with client.wiki.with_streaming_response.list(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            wiki = response.parse()
            assert_matches_type(WikiListResponse, wiki, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Structify) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `team_id` but received ''"):
            client.wiki.with_raw_response.list(
                "",
            )

    @parametrize
    def test_method_delete(self, client: Structify) -> None:
        wiki = client.wiki.delete(
            slug="slug",
            team_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert wiki is None

    @parametrize
    def test_raw_response_delete(self, client: Structify) -> None:
        response = client.wiki.with_raw_response.delete(
            slug="slug",
            team_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        wiki = response.parse()
        assert wiki is None

    @parametrize
    def test_streaming_response_delete(self, client: Structify) -> None:
        with client.wiki.with_streaming_response.delete(
            slug="slug",
            team_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            wiki = response.parse()
            assert wiki is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Structify) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `team_id` but received ''"):
            client.wiki.with_raw_response.delete(
                slug="slug",
                team_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `slug` but received ''"):
            client.wiki.with_raw_response.delete(
                slug="",
                team_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @parametrize
    def test_method_get(self, client: Structify) -> None:
        wiki = client.wiki.get(
            slug="slug",
            team_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(WikiPageWithReferences, wiki, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Structify) -> None:
        response = client.wiki.with_raw_response.get(
            slug="slug",
            team_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        wiki = response.parse()
        assert_matches_type(WikiPageWithReferences, wiki, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Structify) -> None:
        with client.wiki.with_streaming_response.get(
            slug="slug",
            team_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            wiki = response.parse()
            assert_matches_type(WikiPageWithReferences, wiki, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Structify) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `team_id` but received ''"):
            client.wiki.with_raw_response.get(
                slug="slug",
                team_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `slug` but received ''"):
            client.wiki.with_raw_response.get(
                slug="",
                team_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )


class TestAsyncWiki:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncStructify) -> None:
        wiki = await async_client.wiki.create(
            team_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            content={"foo": "bar"},
            slug="slug",
            title="title",
        )
        assert_matches_type(TeamWikiPage, wiki, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncStructify) -> None:
        response = await async_client.wiki.with_raw_response.create(
            team_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            content={"foo": "bar"},
            slug="slug",
            title="title",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        wiki = await response.parse()
        assert_matches_type(TeamWikiPage, wiki, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncStructify) -> None:
        async with async_client.wiki.with_streaming_response.create(
            team_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            content={"foo": "bar"},
            slug="slug",
            title="title",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            wiki = await response.parse()
            assert_matches_type(TeamWikiPage, wiki, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncStructify) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `team_id` but received ''"):
            await async_client.wiki.with_raw_response.create(
                team_id="",
                content={"foo": "bar"},
                slug="slug",
                title="title",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncStructify) -> None:
        wiki = await async_client.wiki.update(
            slug="slug",
            team_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            content={"foo": "bar"},
        )
        assert_matches_type(TeamWikiPage, wiki, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncStructify) -> None:
        wiki = await async_client.wiki.update(
            slug="slug",
            team_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            content={"foo": "bar"},
            title="title",
        )
        assert_matches_type(TeamWikiPage, wiki, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncStructify) -> None:
        response = await async_client.wiki.with_raw_response.update(
            slug="slug",
            team_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            content={"foo": "bar"},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        wiki = await response.parse()
        assert_matches_type(TeamWikiPage, wiki, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncStructify) -> None:
        async with async_client.wiki.with_streaming_response.update(
            slug="slug",
            team_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            content={"foo": "bar"},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            wiki = await response.parse()
            assert_matches_type(TeamWikiPage, wiki, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncStructify) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `team_id` but received ''"):
            await async_client.wiki.with_raw_response.update(
                slug="slug",
                team_id="",
                content={"foo": "bar"},
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `slug` but received ''"):
            await async_client.wiki.with_raw_response.update(
                slug="",
                team_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                content={"foo": "bar"},
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncStructify) -> None:
        wiki = await async_client.wiki.list(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(WikiListResponse, wiki, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncStructify) -> None:
        response = await async_client.wiki.with_raw_response.list(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        wiki = await response.parse()
        assert_matches_type(WikiListResponse, wiki, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncStructify) -> None:
        async with async_client.wiki.with_streaming_response.list(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            wiki = await response.parse()
            assert_matches_type(WikiListResponse, wiki, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncStructify) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `team_id` but received ''"):
            await async_client.wiki.with_raw_response.list(
                "",
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncStructify) -> None:
        wiki = await async_client.wiki.delete(
            slug="slug",
            team_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert wiki is None

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncStructify) -> None:
        response = await async_client.wiki.with_raw_response.delete(
            slug="slug",
            team_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        wiki = await response.parse()
        assert wiki is None

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncStructify) -> None:
        async with async_client.wiki.with_streaming_response.delete(
            slug="slug",
            team_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            wiki = await response.parse()
            assert wiki is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncStructify) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `team_id` but received ''"):
            await async_client.wiki.with_raw_response.delete(
                slug="slug",
                team_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `slug` but received ''"):
            await async_client.wiki.with_raw_response.delete(
                slug="",
                team_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @parametrize
    async def test_method_get(self, async_client: AsyncStructify) -> None:
        wiki = await async_client.wiki.get(
            slug="slug",
            team_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(WikiPageWithReferences, wiki, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncStructify) -> None:
        response = await async_client.wiki.with_raw_response.get(
            slug="slug",
            team_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        wiki = await response.parse()
        assert_matches_type(WikiPageWithReferences, wiki, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncStructify) -> None:
        async with async_client.wiki.with_streaming_response.get(
            slug="slug",
            team_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            wiki = await response.parse()
            assert_matches_type(WikiPageWithReferences, wiki, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncStructify) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `team_id` but received ''"):
            await async_client.wiki.with_raw_response.get(
                slug="slug",
                team_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `slug` but received ''"):
            await async_client.wiki.with_raw_response.get(
                slug="",
                team_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )
