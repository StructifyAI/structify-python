# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from structify import Structify, AsyncStructify
from tests.utils import assert_matches_type
from structify._utils import parse_datetime
from structify.types.admin import (
    TrainingDatumResponse,
    TrainingDatasetListResponse,
    TrainingDatasetSizeResponse,
    TrainingDatasetListDatumsResponse,
    TrainingDatasetGetLabellerStatsResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTrainingDatasets:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: Structify) -> None:
        training_dataset = client.admin.training_datasets.list()
        assert_matches_type(TrainingDatasetListResponse, training_dataset, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Structify) -> None:
        response = client.admin.training_datasets.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        training_dataset = response.parse()
        assert_matches_type(TrainingDatasetListResponse, training_dataset, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Structify) -> None:
        with client.admin.training_datasets.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            training_dataset = response.parse()
            assert_matches_type(TrainingDatasetListResponse, training_dataset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_add(self, client: Structify) -> None:
        training_dataset = client.admin.training_datasets.add(
            dataset_name="dataset_name",
        )
        assert training_dataset is None

    @parametrize
    def test_raw_response_add(self, client: Structify) -> None:
        response = client.admin.training_datasets.with_raw_response.add(
            dataset_name="dataset_name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        training_dataset = response.parse()
        assert training_dataset is None

    @parametrize
    def test_streaming_response_add(self, client: Structify) -> None:
        with client.admin.training_datasets.with_streaming_response.add(
            dataset_name="dataset_name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            training_dataset = response.parse()
            assert training_dataset is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_add_datum(self, client: Structify) -> None:
        training_dataset = client.admin.training_datasets.add_datum(
            dataset_name="dataset_name",
            step_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert training_dataset is None

    @parametrize
    def test_raw_response_add_datum(self, client: Structify) -> None:
        response = client.admin.training_datasets.with_raw_response.add_datum(
            dataset_name="dataset_name",
            step_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        training_dataset = response.parse()
        assert training_dataset is None

    @parametrize
    def test_streaming_response_add_datum(self, client: Structify) -> None:
        with client.admin.training_datasets.with_streaming_response.add_datum(
            dataset_name="dataset_name",
            step_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            training_dataset = response.parse()
            assert training_dataset is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_get_labeller_stats(self, client: Structify) -> None:
        training_dataset = client.admin.training_datasets.get_labeller_stats(
            status="Unlabeled",
        )
        assert_matches_type(TrainingDatasetGetLabellerStatsResponse, training_dataset, path=["response"])

    @parametrize
    def test_method_get_labeller_stats_with_all_params(self, client: Structify) -> None:
        training_dataset = client.admin.training_datasets.get_labeller_stats(
            status="Unlabeled",
            dataset_name="dataset_name",
            end_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(TrainingDatasetGetLabellerStatsResponse, training_dataset, path=["response"])

    @parametrize
    def test_raw_response_get_labeller_stats(self, client: Structify) -> None:
        response = client.admin.training_datasets.with_raw_response.get_labeller_stats(
            status="Unlabeled",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        training_dataset = response.parse()
        assert_matches_type(TrainingDatasetGetLabellerStatsResponse, training_dataset, path=["response"])

    @parametrize
    def test_streaming_response_get_labeller_stats(self, client: Structify) -> None:
        with client.admin.training_datasets.with_streaming_response.get_labeller_stats(
            status="Unlabeled",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            training_dataset = response.parse()
            assert_matches_type(TrainingDatasetGetLabellerStatsResponse, training_dataset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_get_next_unverified(self, client: Structify) -> None:
        training_dataset = client.admin.training_datasets.get_next_unverified(
            dataset_name="dataset_name",
            status="Unlabeled",
        )
        assert_matches_type(TrainingDatumResponse, training_dataset, path=["response"])

    @parametrize
    def test_raw_response_get_next_unverified(self, client: Structify) -> None:
        response = client.admin.training_datasets.with_raw_response.get_next_unverified(
            dataset_name="dataset_name",
            status="Unlabeled",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        training_dataset = response.parse()
        assert_matches_type(TrainingDatumResponse, training_dataset, path=["response"])

    @parametrize
    def test_streaming_response_get_next_unverified(self, client: Structify) -> None:
        with client.admin.training_datasets.with_streaming_response.get_next_unverified(
            dataset_name="dataset_name",
            status="Unlabeled",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            training_dataset = response.parse()
            assert_matches_type(TrainingDatumResponse, training_dataset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_get_step_by_id(self, client: Structify) -> None:
        training_dataset = client.admin.training_datasets.get_step_by_id(
            step_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(TrainingDatumResponse, training_dataset, path=["response"])

    @parametrize
    def test_raw_response_get_step_by_id(self, client: Structify) -> None:
        response = client.admin.training_datasets.with_raw_response.get_step_by_id(
            step_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        training_dataset = response.parse()
        assert_matches_type(TrainingDatumResponse, training_dataset, path=["response"])

    @parametrize
    def test_streaming_response_get_step_by_id(self, client: Structify) -> None:
        with client.admin.training_datasets.with_streaming_response.get_step_by_id(
            step_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            training_dataset = response.parse()
            assert_matches_type(TrainingDatumResponse, training_dataset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_list_datums(self, client: Structify) -> None:
        training_dataset = client.admin.training_datasets.list_datums(
            dataset_name="dataset_name",
        )
        assert_matches_type(TrainingDatasetListDatumsResponse, training_dataset, path=["response"])

    @parametrize
    def test_raw_response_list_datums(self, client: Structify) -> None:
        response = client.admin.training_datasets.with_raw_response.list_datums(
            dataset_name="dataset_name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        training_dataset = response.parse()
        assert_matches_type(TrainingDatasetListDatumsResponse, training_dataset, path=["response"])

    @parametrize
    def test_streaming_response_list_datums(self, client: Structify) -> None:
        with client.admin.training_datasets.with_streaming_response.list_datums(
            dataset_name="dataset_name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            training_dataset = response.parse()
            assert_matches_type(TrainingDatasetListDatumsResponse, training_dataset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_mark_suspicious_datum(self, client: Structify) -> None:
        training_dataset = client.admin.training_datasets.mark_suspicious_datum(
            reason="reason",
            step_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert training_dataset is None

    @parametrize
    def test_raw_response_mark_suspicious_datum(self, client: Structify) -> None:
        response = client.admin.training_datasets.with_raw_response.mark_suspicious_datum(
            reason="reason",
            step_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        training_dataset = response.parse()
        assert training_dataset is None

    @parametrize
    def test_streaming_response_mark_suspicious_datum(self, client: Structify) -> None:
        with client.admin.training_datasets.with_streaming_response.mark_suspicious_datum(
            reason="reason",
            step_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            training_dataset = response.parse()
            assert training_dataset is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_remove_datum(self, client: Structify) -> None:
        training_dataset = client.admin.training_datasets.remove_datum(
            step_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert training_dataset is None

    @parametrize
    def test_raw_response_remove_datum(self, client: Structify) -> None:
        response = client.admin.training_datasets.with_raw_response.remove_datum(
            step_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        training_dataset = response.parse()
        assert training_dataset is None

    @parametrize
    def test_streaming_response_remove_datum(self, client: Structify) -> None:
        with client.admin.training_datasets.with_streaming_response.remove_datum(
            step_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            training_dataset = response.parse()
            assert training_dataset is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_reset_pending(self, client: Structify) -> None:
        training_dataset = client.admin.training_datasets.reset_pending(
            dataset_name="dataset_name",
        )
        assert training_dataset is None

    @parametrize
    def test_raw_response_reset_pending(self, client: Structify) -> None:
        response = client.admin.training_datasets.with_raw_response.reset_pending(
            dataset_name="dataset_name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        training_dataset = response.parse()
        assert training_dataset is None

    @parametrize
    def test_streaming_response_reset_pending(self, client: Structify) -> None:
        with client.admin.training_datasets.with_streaming_response.reset_pending(
            dataset_name="dataset_name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            training_dataset = response.parse()
            assert training_dataset is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_size(self, client: Structify) -> None:
        training_dataset = client.admin.training_datasets.size(
            dataset_name="dataset_name",
        )
        assert_matches_type(TrainingDatasetSizeResponse, training_dataset, path=["response"])

    @parametrize
    def test_method_size_with_all_params(self, client: Structify) -> None:
        training_dataset = client.admin.training_datasets.size(
            dataset_name="dataset_name",
            end_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            status="Unlabeled",
        )
        assert_matches_type(TrainingDatasetSizeResponse, training_dataset, path=["response"])

    @parametrize
    def test_raw_response_size(self, client: Structify) -> None:
        response = client.admin.training_datasets.with_raw_response.size(
            dataset_name="dataset_name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        training_dataset = response.parse()
        assert_matches_type(TrainingDatasetSizeResponse, training_dataset, path=["response"])

    @parametrize
    def test_streaming_response_size(self, client: Structify) -> None:
        with client.admin.training_datasets.with_streaming_response.size(
            dataset_name="dataset_name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            training_dataset = response.parse()
            assert_matches_type(TrainingDatasetSizeResponse, training_dataset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_update_datum(self, client: Structify) -> None:
        training_dataset = client.admin.training_datasets.update_datum(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            status="Unlabeled",
            updated_tool_calls=[
                {
                    "input": {"save": {}},
                    "name": "Save",
                }
            ],
        )
        assert training_dataset is None

    @parametrize
    def test_raw_response_update_datum(self, client: Structify) -> None:
        response = client.admin.training_datasets.with_raw_response.update_datum(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            status="Unlabeled",
            updated_tool_calls=[
                {
                    "input": {"save": {}},
                    "name": "Save",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        training_dataset = response.parse()
        assert training_dataset is None

    @parametrize
    def test_streaming_response_update_datum(self, client: Structify) -> None:
        with client.admin.training_datasets.with_streaming_response.update_datum(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            status="Unlabeled",
            updated_tool_calls=[
                {
                    "input": {"save": {}},
                    "name": "Save",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            training_dataset = response.parse()
            assert training_dataset is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_upload_datum(self, client: Structify) -> None:
        training_dataset = client.admin.training_datasets.upload_datum(
            dataset_name=b"raw file contents",
            step_bytes=b"raw file contents",
        )
        assert training_dataset is None

    @parametrize
    def test_raw_response_upload_datum(self, client: Structify) -> None:
        response = client.admin.training_datasets.with_raw_response.upload_datum(
            dataset_name=b"raw file contents",
            step_bytes=b"raw file contents",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        training_dataset = response.parse()
        assert training_dataset is None

    @parametrize
    def test_streaming_response_upload_datum(self, client: Structify) -> None:
        with client.admin.training_datasets.with_streaming_response.upload_datum(
            dataset_name=b"raw file contents",
            step_bytes=b"raw file contents",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            training_dataset = response.parse()
            assert training_dataset is None

        assert cast(Any, response.is_closed) is True


class TestAsyncTrainingDatasets:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_list(self, async_client: AsyncStructify) -> None:
        training_dataset = await async_client.admin.training_datasets.list()
        assert_matches_type(TrainingDatasetListResponse, training_dataset, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncStructify) -> None:
        response = await async_client.admin.training_datasets.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        training_dataset = await response.parse()
        assert_matches_type(TrainingDatasetListResponse, training_dataset, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncStructify) -> None:
        async with async_client.admin.training_datasets.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            training_dataset = await response.parse()
            assert_matches_type(TrainingDatasetListResponse, training_dataset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_add(self, async_client: AsyncStructify) -> None:
        training_dataset = await async_client.admin.training_datasets.add(
            dataset_name="dataset_name",
        )
        assert training_dataset is None

    @parametrize
    async def test_raw_response_add(self, async_client: AsyncStructify) -> None:
        response = await async_client.admin.training_datasets.with_raw_response.add(
            dataset_name="dataset_name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        training_dataset = await response.parse()
        assert training_dataset is None

    @parametrize
    async def test_streaming_response_add(self, async_client: AsyncStructify) -> None:
        async with async_client.admin.training_datasets.with_streaming_response.add(
            dataset_name="dataset_name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            training_dataset = await response.parse()
            assert training_dataset is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_add_datum(self, async_client: AsyncStructify) -> None:
        training_dataset = await async_client.admin.training_datasets.add_datum(
            dataset_name="dataset_name",
            step_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert training_dataset is None

    @parametrize
    async def test_raw_response_add_datum(self, async_client: AsyncStructify) -> None:
        response = await async_client.admin.training_datasets.with_raw_response.add_datum(
            dataset_name="dataset_name",
            step_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        training_dataset = await response.parse()
        assert training_dataset is None

    @parametrize
    async def test_streaming_response_add_datum(self, async_client: AsyncStructify) -> None:
        async with async_client.admin.training_datasets.with_streaming_response.add_datum(
            dataset_name="dataset_name",
            step_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            training_dataset = await response.parse()
            assert training_dataset is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_get_labeller_stats(self, async_client: AsyncStructify) -> None:
        training_dataset = await async_client.admin.training_datasets.get_labeller_stats(
            status="Unlabeled",
        )
        assert_matches_type(TrainingDatasetGetLabellerStatsResponse, training_dataset, path=["response"])

    @parametrize
    async def test_method_get_labeller_stats_with_all_params(self, async_client: AsyncStructify) -> None:
        training_dataset = await async_client.admin.training_datasets.get_labeller_stats(
            status="Unlabeled",
            dataset_name="dataset_name",
            end_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(TrainingDatasetGetLabellerStatsResponse, training_dataset, path=["response"])

    @parametrize
    async def test_raw_response_get_labeller_stats(self, async_client: AsyncStructify) -> None:
        response = await async_client.admin.training_datasets.with_raw_response.get_labeller_stats(
            status="Unlabeled",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        training_dataset = await response.parse()
        assert_matches_type(TrainingDatasetGetLabellerStatsResponse, training_dataset, path=["response"])

    @parametrize
    async def test_streaming_response_get_labeller_stats(self, async_client: AsyncStructify) -> None:
        async with async_client.admin.training_datasets.with_streaming_response.get_labeller_stats(
            status="Unlabeled",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            training_dataset = await response.parse()
            assert_matches_type(TrainingDatasetGetLabellerStatsResponse, training_dataset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_get_next_unverified(self, async_client: AsyncStructify) -> None:
        training_dataset = await async_client.admin.training_datasets.get_next_unverified(
            dataset_name="dataset_name",
            status="Unlabeled",
        )
        assert_matches_type(TrainingDatumResponse, training_dataset, path=["response"])

    @parametrize
    async def test_raw_response_get_next_unverified(self, async_client: AsyncStructify) -> None:
        response = await async_client.admin.training_datasets.with_raw_response.get_next_unverified(
            dataset_name="dataset_name",
            status="Unlabeled",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        training_dataset = await response.parse()
        assert_matches_type(TrainingDatumResponse, training_dataset, path=["response"])

    @parametrize
    async def test_streaming_response_get_next_unverified(self, async_client: AsyncStructify) -> None:
        async with async_client.admin.training_datasets.with_streaming_response.get_next_unverified(
            dataset_name="dataset_name",
            status="Unlabeled",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            training_dataset = await response.parse()
            assert_matches_type(TrainingDatumResponse, training_dataset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_get_step_by_id(self, async_client: AsyncStructify) -> None:
        training_dataset = await async_client.admin.training_datasets.get_step_by_id(
            step_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(TrainingDatumResponse, training_dataset, path=["response"])

    @parametrize
    async def test_raw_response_get_step_by_id(self, async_client: AsyncStructify) -> None:
        response = await async_client.admin.training_datasets.with_raw_response.get_step_by_id(
            step_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        training_dataset = await response.parse()
        assert_matches_type(TrainingDatumResponse, training_dataset, path=["response"])

    @parametrize
    async def test_streaming_response_get_step_by_id(self, async_client: AsyncStructify) -> None:
        async with async_client.admin.training_datasets.with_streaming_response.get_step_by_id(
            step_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            training_dataset = await response.parse()
            assert_matches_type(TrainingDatumResponse, training_dataset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_list_datums(self, async_client: AsyncStructify) -> None:
        training_dataset = await async_client.admin.training_datasets.list_datums(
            dataset_name="dataset_name",
        )
        assert_matches_type(TrainingDatasetListDatumsResponse, training_dataset, path=["response"])

    @parametrize
    async def test_raw_response_list_datums(self, async_client: AsyncStructify) -> None:
        response = await async_client.admin.training_datasets.with_raw_response.list_datums(
            dataset_name="dataset_name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        training_dataset = await response.parse()
        assert_matches_type(TrainingDatasetListDatumsResponse, training_dataset, path=["response"])

    @parametrize
    async def test_streaming_response_list_datums(self, async_client: AsyncStructify) -> None:
        async with async_client.admin.training_datasets.with_streaming_response.list_datums(
            dataset_name="dataset_name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            training_dataset = await response.parse()
            assert_matches_type(TrainingDatasetListDatumsResponse, training_dataset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_mark_suspicious_datum(self, async_client: AsyncStructify) -> None:
        training_dataset = await async_client.admin.training_datasets.mark_suspicious_datum(
            reason="reason",
            step_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert training_dataset is None

    @parametrize
    async def test_raw_response_mark_suspicious_datum(self, async_client: AsyncStructify) -> None:
        response = await async_client.admin.training_datasets.with_raw_response.mark_suspicious_datum(
            reason="reason",
            step_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        training_dataset = await response.parse()
        assert training_dataset is None

    @parametrize
    async def test_streaming_response_mark_suspicious_datum(self, async_client: AsyncStructify) -> None:
        async with async_client.admin.training_datasets.with_streaming_response.mark_suspicious_datum(
            reason="reason",
            step_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            training_dataset = await response.parse()
            assert training_dataset is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_remove_datum(self, async_client: AsyncStructify) -> None:
        training_dataset = await async_client.admin.training_datasets.remove_datum(
            step_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert training_dataset is None

    @parametrize
    async def test_raw_response_remove_datum(self, async_client: AsyncStructify) -> None:
        response = await async_client.admin.training_datasets.with_raw_response.remove_datum(
            step_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        training_dataset = await response.parse()
        assert training_dataset is None

    @parametrize
    async def test_streaming_response_remove_datum(self, async_client: AsyncStructify) -> None:
        async with async_client.admin.training_datasets.with_streaming_response.remove_datum(
            step_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            training_dataset = await response.parse()
            assert training_dataset is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_reset_pending(self, async_client: AsyncStructify) -> None:
        training_dataset = await async_client.admin.training_datasets.reset_pending(
            dataset_name="dataset_name",
        )
        assert training_dataset is None

    @parametrize
    async def test_raw_response_reset_pending(self, async_client: AsyncStructify) -> None:
        response = await async_client.admin.training_datasets.with_raw_response.reset_pending(
            dataset_name="dataset_name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        training_dataset = await response.parse()
        assert training_dataset is None

    @parametrize
    async def test_streaming_response_reset_pending(self, async_client: AsyncStructify) -> None:
        async with async_client.admin.training_datasets.with_streaming_response.reset_pending(
            dataset_name="dataset_name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            training_dataset = await response.parse()
            assert training_dataset is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_size(self, async_client: AsyncStructify) -> None:
        training_dataset = await async_client.admin.training_datasets.size(
            dataset_name="dataset_name",
        )
        assert_matches_type(TrainingDatasetSizeResponse, training_dataset, path=["response"])

    @parametrize
    async def test_method_size_with_all_params(self, async_client: AsyncStructify) -> None:
        training_dataset = await async_client.admin.training_datasets.size(
            dataset_name="dataset_name",
            end_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            status="Unlabeled",
        )
        assert_matches_type(TrainingDatasetSizeResponse, training_dataset, path=["response"])

    @parametrize
    async def test_raw_response_size(self, async_client: AsyncStructify) -> None:
        response = await async_client.admin.training_datasets.with_raw_response.size(
            dataset_name="dataset_name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        training_dataset = await response.parse()
        assert_matches_type(TrainingDatasetSizeResponse, training_dataset, path=["response"])

    @parametrize
    async def test_streaming_response_size(self, async_client: AsyncStructify) -> None:
        async with async_client.admin.training_datasets.with_streaming_response.size(
            dataset_name="dataset_name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            training_dataset = await response.parse()
            assert_matches_type(TrainingDatasetSizeResponse, training_dataset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_update_datum(self, async_client: AsyncStructify) -> None:
        training_dataset = await async_client.admin.training_datasets.update_datum(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            status="Unlabeled",
            updated_tool_calls=[
                {
                    "input": {"save": {}},
                    "name": "Save",
                }
            ],
        )
        assert training_dataset is None

    @parametrize
    async def test_raw_response_update_datum(self, async_client: AsyncStructify) -> None:
        response = await async_client.admin.training_datasets.with_raw_response.update_datum(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            status="Unlabeled",
            updated_tool_calls=[
                {
                    "input": {"save": {}},
                    "name": "Save",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        training_dataset = await response.parse()
        assert training_dataset is None

    @parametrize
    async def test_streaming_response_update_datum(self, async_client: AsyncStructify) -> None:
        async with async_client.admin.training_datasets.with_streaming_response.update_datum(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            status="Unlabeled",
            updated_tool_calls=[
                {
                    "input": {"save": {}},
                    "name": "Save",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            training_dataset = await response.parse()
            assert training_dataset is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_upload_datum(self, async_client: AsyncStructify) -> None:
        training_dataset = await async_client.admin.training_datasets.upload_datum(
            dataset_name=b"raw file contents",
            step_bytes=b"raw file contents",
        )
        assert training_dataset is None

    @parametrize
    async def test_raw_response_upload_datum(self, async_client: AsyncStructify) -> None:
        response = await async_client.admin.training_datasets.with_raw_response.upload_datum(
            dataset_name=b"raw file contents",
            step_bytes=b"raw file contents",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        training_dataset = await response.parse()
        assert training_dataset is None

    @parametrize
    async def test_streaming_response_upload_datum(self, async_client: AsyncStructify) -> None:
        async with async_client.admin.training_datasets.with_streaming_response.upload_datum(
            dataset_name=b"raw file contents",
            step_bytes=b"raw file contents",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            training_dataset = await response.parse()
            assert training_dataset is None

        assert cast(Any, response.is_closed) is True
