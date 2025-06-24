# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from structify import Structify, AsyncStructify
from tests.utils import assert_matches_type
from structify.pagination import SyncJobsList, AsyncJobsList
from structify.types.datasets import (
    EvaluateGetResponse,
    EvaluateListResponse,
    EvaluateStatusResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestEvaluate:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: Structify) -> None:
        evaluate = client.datasets.evaluate.list(
            limit=1,
            offset=0,
        )
        assert_matches_type(SyncJobsList[EvaluateListResponse], evaluate, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Structify) -> None:
        response = client.datasets.evaluate.with_raw_response.list(
            limit=1,
            offset=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        evaluate = response.parse()
        assert_matches_type(SyncJobsList[EvaluateListResponse], evaluate, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Structify) -> None:
        with client.datasets.evaluate.with_streaming_response.list(
            limit=1,
            offset=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            evaluate = response.parse()
            assert_matches_type(SyncJobsList[EvaluateListResponse], evaluate, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Structify) -> None:
        evaluate = client.datasets.evaluate.delete(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert evaluate is None

    @parametrize
    def test_raw_response_delete(self, client: Structify) -> None:
        response = client.datasets.evaluate.with_raw_response.delete(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        evaluate = response.parse()
        assert evaluate is None

    @parametrize
    def test_streaming_response_delete(self, client: Structify) -> None:
        with client.datasets.evaluate.with_streaming_response.delete(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            evaluate = response.parse()
            assert evaluate is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip
    @parametrize
    def test_method_get(self, client: Structify) -> None:
        evaluate = client.datasets.evaluate.get(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(EvaluateGetResponse, evaluate, path=["response"])

    @pytest.mark.skip
    @parametrize
    def test_raw_response_get(self, client: Structify) -> None:
        response = client.datasets.evaluate.with_raw_response.get(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        evaluate = response.parse()
        assert_matches_type(EvaluateGetResponse, evaluate, path=["response"])

    @pytest.mark.skip
    @parametrize
    def test_streaming_response_get(self, client: Structify) -> None:
        with client.datasets.evaluate.with_streaming_response.get(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            evaluate = response.parse()
            assert_matches_type(EvaluateGetResponse, evaluate, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_run(self, client: Structify) -> None:
        evaluate = client.datasets.evaluate.run(
            dataset_1="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            dataset_2="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            dataset_2_is_ground_truth=True,
        )
        assert_matches_type(str, evaluate, path=["response"])

    @parametrize
    def test_method_run_with_all_params(self, client: Structify) -> None:
        evaluate = client.datasets.evaluate.run(
            dataset_1="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            dataset_2="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            dataset_2_is_ground_truth=True,
            merge_threshold_override=0,
        )
        assert_matches_type(str, evaluate, path=["response"])

    @parametrize
    def test_raw_response_run(self, client: Structify) -> None:
        response = client.datasets.evaluate.with_raw_response.run(
            dataset_1="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            dataset_2="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            dataset_2_is_ground_truth=True,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        evaluate = response.parse()
        assert_matches_type(str, evaluate, path=["response"])

    @parametrize
    def test_streaming_response_run(self, client: Structify) -> None:
        with client.datasets.evaluate.with_streaming_response.run(
            dataset_1="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            dataset_2="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            dataset_2_is_ground_truth=True,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            evaluate = response.parse()
            assert_matches_type(str, evaluate, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_status(self, client: Structify) -> None:
        evaluate = client.datasets.evaluate.status(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(EvaluateStatusResponse, evaluate, path=["response"])

    @parametrize
    def test_raw_response_status(self, client: Structify) -> None:
        response = client.datasets.evaluate.with_raw_response.status(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        evaluate = response.parse()
        assert_matches_type(EvaluateStatusResponse, evaluate, path=["response"])

    @parametrize
    def test_streaming_response_status(self, client: Structify) -> None:
        with client.datasets.evaluate.with_streaming_response.status(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            evaluate = response.parse()
            assert_matches_type(EvaluateStatusResponse, evaluate, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncEvaluate:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_list(self, async_client: AsyncStructify) -> None:
        evaluate = await async_client.datasets.evaluate.list(
            limit=1,
            offset=0,
        )
        assert_matches_type(AsyncJobsList[EvaluateListResponse], evaluate, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncStructify) -> None:
        response = await async_client.datasets.evaluate.with_raw_response.list(
            limit=1,
            offset=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        evaluate = await response.parse()
        assert_matches_type(AsyncJobsList[EvaluateListResponse], evaluate, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncStructify) -> None:
        async with async_client.datasets.evaluate.with_streaming_response.list(
            limit=1,
            offset=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            evaluate = await response.parse()
            assert_matches_type(AsyncJobsList[EvaluateListResponse], evaluate, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncStructify) -> None:
        evaluate = await async_client.datasets.evaluate.delete(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert evaluate is None

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncStructify) -> None:
        response = await async_client.datasets.evaluate.with_raw_response.delete(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        evaluate = await response.parse()
        assert evaluate is None

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncStructify) -> None:
        async with async_client.datasets.evaluate.with_streaming_response.delete(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            evaluate = await response.parse()
            assert evaluate is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip
    @parametrize
    async def test_method_get(self, async_client: AsyncStructify) -> None:
        evaluate = await async_client.datasets.evaluate.get(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(EvaluateGetResponse, evaluate, path=["response"])

    @pytest.mark.skip
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncStructify) -> None:
        response = await async_client.datasets.evaluate.with_raw_response.get(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        evaluate = await response.parse()
        assert_matches_type(EvaluateGetResponse, evaluate, path=["response"])

    @pytest.mark.skip
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncStructify) -> None:
        async with async_client.datasets.evaluate.with_streaming_response.get(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            evaluate = await response.parse()
            assert_matches_type(EvaluateGetResponse, evaluate, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_run(self, async_client: AsyncStructify) -> None:
        evaluate = await async_client.datasets.evaluate.run(
            dataset_1="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            dataset_2="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            dataset_2_is_ground_truth=True,
        )
        assert_matches_type(str, evaluate, path=["response"])

    @parametrize
    async def test_method_run_with_all_params(self, async_client: AsyncStructify) -> None:
        evaluate = await async_client.datasets.evaluate.run(
            dataset_1="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            dataset_2="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            dataset_2_is_ground_truth=True,
            merge_threshold_override=0,
        )
        assert_matches_type(str, evaluate, path=["response"])

    @parametrize
    async def test_raw_response_run(self, async_client: AsyncStructify) -> None:
        response = await async_client.datasets.evaluate.with_raw_response.run(
            dataset_1="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            dataset_2="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            dataset_2_is_ground_truth=True,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        evaluate = await response.parse()
        assert_matches_type(str, evaluate, path=["response"])

    @parametrize
    async def test_streaming_response_run(self, async_client: AsyncStructify) -> None:
        async with async_client.datasets.evaluate.with_streaming_response.run(
            dataset_1="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            dataset_2="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            dataset_2_is_ground_truth=True,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            evaluate = await response.parse()
            assert_matches_type(str, evaluate, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_status(self, async_client: AsyncStructify) -> None:
        evaluate = await async_client.datasets.evaluate.status(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(EvaluateStatusResponse, evaluate, path=["response"])

    @parametrize
    async def test_raw_response_status(self, async_client: AsyncStructify) -> None:
        response = await async_client.datasets.evaluate.with_raw_response.status(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        evaluate = await response.parse()
        assert_matches_type(EvaluateStatusResponse, evaluate, path=["response"])

    @parametrize
    async def test_streaming_response_status(self, async_client: AsyncStructify) -> None:
        async with async_client.datasets.evaluate.with_streaming_response.status(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            evaluate = await response.parse()
            assert_matches_type(EvaluateStatusResponse, evaluate, path=["response"])

        assert cast(Any, response.is_closed) is True
