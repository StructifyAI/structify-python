# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from structify import Structify, AsyncStructify
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestRun:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create_overload_1(self, client: Structify) -> None:
        run = client.structure.run.create(
            dataset_name="string",
            text={"text_content": "string"},
        )
        assert_matches_type(object, run, path=["response"])

    @parametrize
    def test_method_create_with_all_params_overload_1(self, client: Structify) -> None:
        run = client.structure.run.create(
            dataset_name="string",
            text={"text_content": "string"},
            custom_instruction="string",
        )
        assert_matches_type(object, run, path=["response"])

    @parametrize
    def test_raw_response_create_overload_1(self, client: Structify) -> None:
        response = client.structure.run.with_raw_response.create(
            dataset_name="string",
            text={"text_content": "string"},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        run = response.parse()
        assert_matches_type(object, run, path=["response"])

    @parametrize
    def test_streaming_response_create_overload_1(self, client: Structify) -> None:
        with client.structure.run.with_streaming_response.create(
            dataset_name="string",
            text={"text_content": "string"},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            run = response.parse()
            assert_matches_type(object, run, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_create_overload_2(self, client: Structify) -> None:
        run = client.structure.run.create(
            dataset_name="string",
            document={"path": "string"},
        )
        assert_matches_type(object, run, path=["response"])

    @parametrize
    def test_method_create_with_all_params_overload_2(self, client: Structify) -> None:
        run = client.structure.run.create(
            dataset_name="string",
            document={"path": "string"},
            custom_instruction="string",
        )
        assert_matches_type(object, run, path=["response"])

    @parametrize
    def test_raw_response_create_overload_2(self, client: Structify) -> None:
        response = client.structure.run.with_raw_response.create(
            dataset_name="string",
            document={"path": "string"},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        run = response.parse()
        assert_matches_type(object, run, path=["response"])

    @parametrize
    def test_streaming_response_create_overload_2(self, client: Structify) -> None:
        with client.structure.run.with_streaming_response.create(
            dataset_name="string",
            document={"path": "string"},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            run = response.parse()
            assert_matches_type(object, run, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_create_overload_3(self, client: Structify) -> None:
        run = client.structure.run.create(
            dataset_name="string",
            web={"phrase": "string"},
        )
        assert_matches_type(object, run, path=["response"])

    @parametrize
    def test_method_create_with_all_params_overload_3(self, client: Structify) -> None:
        run = client.structure.run.create(
            dataset_name="string",
            web={
                "phrase": "string",
                "starting_website": "string",
            },
            custom_instruction="string",
        )
        assert_matches_type(object, run, path=["response"])

    @parametrize
    def test_raw_response_create_overload_3(self, client: Structify) -> None:
        response = client.structure.run.with_raw_response.create(
            dataset_name="string",
            web={"phrase": "string"},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        run = response.parse()
        assert_matches_type(object, run, path=["response"])

    @parametrize
    def test_streaming_response_create_overload_3(self, client: Structify) -> None:
        with client.structure.run.with_streaming_response.create(
            dataset_name="string",
            web={"phrase": "string"},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            run = response.parse()
            assert_matches_type(object, run, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_create_overload_4(self, client: Structify) -> None:
        run = client.structure.run.create(
            dataset_name="string",
            sec_filing={},
        )
        assert_matches_type(object, run, path=["response"])

    @parametrize
    def test_method_create_with_all_params_overload_4(self, client: Structify) -> None:
        run = client.structure.run.create(
            dataset_name="string",
            sec_filing={
                "accession_number": "string",
                "quarter": 0,
                "year": 0,
            },
            custom_instruction="string",
        )
        assert_matches_type(object, run, path=["response"])

    @parametrize
    def test_raw_response_create_overload_4(self, client: Structify) -> None:
        response = client.structure.run.with_raw_response.create(
            dataset_name="string",
            sec_filing={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        run = response.parse()
        assert_matches_type(object, run, path=["response"])

    @parametrize
    def test_streaming_response_create_overload_4(self, client: Structify) -> None:
        with client.structure.run.with_streaming_response.create(
            dataset_name="string",
            sec_filing={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            run = response.parse()
            assert_matches_type(object, run, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncRun:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create_overload_1(self, async_client: AsyncStructify) -> None:
        run = await async_client.structure.run.create(
            dataset_name="string",
            text={"text_content": "string"},
        )
        assert_matches_type(object, run, path=["response"])

    @parametrize
    async def test_method_create_with_all_params_overload_1(self, async_client: AsyncStructify) -> None:
        run = await async_client.structure.run.create(
            dataset_name="string",
            text={"text_content": "string"},
            custom_instruction="string",
        )
        assert_matches_type(object, run, path=["response"])

    @parametrize
    async def test_raw_response_create_overload_1(self, async_client: AsyncStructify) -> None:
        response = await async_client.structure.run.with_raw_response.create(
            dataset_name="string",
            text={"text_content": "string"},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        run = await response.parse()
        assert_matches_type(object, run, path=["response"])

    @parametrize
    async def test_streaming_response_create_overload_1(self, async_client: AsyncStructify) -> None:
        async with async_client.structure.run.with_streaming_response.create(
            dataset_name="string",
            text={"text_content": "string"},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            run = await response.parse()
            assert_matches_type(object, run, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_create_overload_2(self, async_client: AsyncStructify) -> None:
        run = await async_client.structure.run.create(
            dataset_name="string",
            document={"path": "string"},
        )
        assert_matches_type(object, run, path=["response"])

    @parametrize
    async def test_method_create_with_all_params_overload_2(self, async_client: AsyncStructify) -> None:
        run = await async_client.structure.run.create(
            dataset_name="string",
            document={"path": "string"},
            custom_instruction="string",
        )
        assert_matches_type(object, run, path=["response"])

    @parametrize
    async def test_raw_response_create_overload_2(self, async_client: AsyncStructify) -> None:
        response = await async_client.structure.run.with_raw_response.create(
            dataset_name="string",
            document={"path": "string"},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        run = await response.parse()
        assert_matches_type(object, run, path=["response"])

    @parametrize
    async def test_streaming_response_create_overload_2(self, async_client: AsyncStructify) -> None:
        async with async_client.structure.run.with_streaming_response.create(
            dataset_name="string",
            document={"path": "string"},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            run = await response.parse()
            assert_matches_type(object, run, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_create_overload_3(self, async_client: AsyncStructify) -> None:
        run = await async_client.structure.run.create(
            dataset_name="string",
            web={"phrase": "string"},
        )
        assert_matches_type(object, run, path=["response"])

    @parametrize
    async def test_method_create_with_all_params_overload_3(self, async_client: AsyncStructify) -> None:
        run = await async_client.structure.run.create(
            dataset_name="string",
            web={
                "phrase": "string",
                "starting_website": "string",
            },
            custom_instruction="string",
        )
        assert_matches_type(object, run, path=["response"])

    @parametrize
    async def test_raw_response_create_overload_3(self, async_client: AsyncStructify) -> None:
        response = await async_client.structure.run.with_raw_response.create(
            dataset_name="string",
            web={"phrase": "string"},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        run = await response.parse()
        assert_matches_type(object, run, path=["response"])

    @parametrize
    async def test_streaming_response_create_overload_3(self, async_client: AsyncStructify) -> None:
        async with async_client.structure.run.with_streaming_response.create(
            dataset_name="string",
            web={"phrase": "string"},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            run = await response.parse()
            assert_matches_type(object, run, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_create_overload_4(self, async_client: AsyncStructify) -> None:
        run = await async_client.structure.run.create(
            dataset_name="string",
            sec_filing={},
        )
        assert_matches_type(object, run, path=["response"])

    @parametrize
    async def test_method_create_with_all_params_overload_4(self, async_client: AsyncStructify) -> None:
        run = await async_client.structure.run.create(
            dataset_name="string",
            sec_filing={
                "accession_number": "string",
                "quarter": 0,
                "year": 0,
            },
            custom_instruction="string",
        )
        assert_matches_type(object, run, path=["response"])

    @parametrize
    async def test_raw_response_create_overload_4(self, async_client: AsyncStructify) -> None:
        response = await async_client.structure.run.with_raw_response.create(
            dataset_name="string",
            sec_filing={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        run = await response.parse()
        assert_matches_type(object, run, path=["response"])

    @parametrize
    async def test_streaming_response_create_overload_4(self, async_client: AsyncStructify) -> None:
        async with async_client.structure.run.with_streaming_response.create(
            dataset_name="string",
            sec_filing={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            run = await response.parse()
            assert_matches_type(object, run, path=["response"])

        assert cast(Any, response.is_closed) is True
