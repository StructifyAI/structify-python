# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import httpx
import pytest
from respx import MockRouter

from structify import Structify, AsyncStructify
from tests.utils import assert_matches_type
from structify._utils import parse_datetime
from structify._response import (
    BinaryAPIResponse,
    AsyncBinaryAPIResponse,
    StreamedBinaryAPIResponse,
    AsyncStreamedBinaryAPIResponse,
)
from structify.types.admin import (
    TrainingDatumResponse,
    TrainingDatasetListResponse,
    TrainingDatasetSizeResponse,
    TrainingDatasetListDatumsResponse,
    TrainingDatasetSuspiciousCountResponse,
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
    def test_method_delete(self, client: Structify) -> None:
        training_dataset = client.admin.training_datasets.delete(
            dataset_name="dataset_name",
        )
        assert training_dataset is None

    @parametrize
    def test_raw_response_delete(self, client: Structify) -> None:
        response = client.admin.training_datasets.with_raw_response.delete(
            dataset_name="dataset_name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        training_dataset = response.parse()
        assert training_dataset is None

    @parametrize
    def test_streaming_response_delete(self, client: Structify) -> None:
        with client.admin.training_datasets.with_streaming_response.delete(
            dataset_name="dataset_name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            training_dataset = response.parse()
            assert training_dataset is None

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
    @pytest.mark.respx(base_url=base_url)
    def test_method_download_datum(self, client: Structify, respx_mock: MockRouter) -> None:
        respx_mock.get("/admin/training_datasets/download_datum_step").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        training_dataset = client.admin.training_datasets.download_datum(
            datum_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert training_dataset.is_closed
        assert training_dataset.json() == {"foo": "bar"}
        assert cast(Any, training_dataset.is_closed) is True
        assert isinstance(training_dataset, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_download_datum_with_all_params(self, client: Structify, respx_mock: MockRouter) -> None:
        respx_mock.get("/admin/training_datasets/download_datum_step").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        training_dataset = client.admin.training_datasets.download_datum(
            datum_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            require_labels=True,
        )
        assert training_dataset.is_closed
        assert training_dataset.json() == {"foo": "bar"}
        assert cast(Any, training_dataset.is_closed) is True
        assert isinstance(training_dataset, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_raw_response_download_datum(self, client: Structify, respx_mock: MockRouter) -> None:
        respx_mock.get("/admin/training_datasets/download_datum_step").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )

        training_dataset = client.admin.training_datasets.with_raw_response.download_datum(
            datum_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert training_dataset.is_closed is True
        assert training_dataset.http_request.headers.get("X-Stainless-Lang") == "python"
        assert training_dataset.json() == {"foo": "bar"}
        assert isinstance(training_dataset, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_streaming_response_download_datum(self, client: Structify, respx_mock: MockRouter) -> None:
        respx_mock.get("/admin/training_datasets/download_datum_step").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        with client.admin.training_datasets.with_streaming_response.download_datum(
            datum_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as training_dataset:
            assert not training_dataset.is_closed
            assert training_dataset.http_request.headers.get("X-Stainless-Lang") == "python"

            assert training_dataset.json() == {"foo": "bar"}
            assert cast(Any, training_dataset.is_closed) is True
            assert isinstance(training_dataset, StreamedBinaryAPIResponse)

        assert cast(Any, training_dataset.is_closed) is True

    @parametrize
    def test_method_get_datum_info(self, client: Structify) -> None:
        training_dataset = client.admin.training_datasets.get_datum_info(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(TrainingDatumResponse, training_dataset, path=["response"])

    @parametrize
    def test_raw_response_get_datum_info(self, client: Structify) -> None:
        response = client.admin.training_datasets.with_raw_response.get_datum_info(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        training_dataset = response.parse()
        assert_matches_type(TrainingDatumResponse, training_dataset, path=["response"])

    @parametrize
    def test_streaming_response_get_datum_info(self, client: Structify) -> None:
        with client.admin.training_datasets.with_streaming_response.get_datum_info(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            training_dataset = response.parse()
            assert_matches_type(TrainingDatumResponse, training_dataset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_get_labeller_stats(self, client: Structify) -> None:
        training_dataset = client.admin.training_datasets.get_labeller_stats()
        assert_matches_type(TrainingDatasetGetLabellerStatsResponse, training_dataset, path=["response"])

    @parametrize
    def test_method_get_labeller_stats_with_all_params(self, client: Structify) -> None:
        training_dataset = client.admin.training_datasets.get_labeller_stats(
            end_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            labeled_status="None",
            max_prop_count=0,
            start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            time_bucket="Second",
        )
        assert_matches_type(TrainingDatasetGetLabellerStatsResponse, training_dataset, path=["response"])

    @parametrize
    def test_raw_response_get_labeller_stats(self, client: Structify) -> None:
        response = client.admin.training_datasets.with_raw_response.get_labeller_stats()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        training_dataset = response.parse()
        assert_matches_type(TrainingDatasetGetLabellerStatsResponse, training_dataset, path=["response"])

    @parametrize
    def test_streaming_response_get_labeller_stats(self, client: Structify) -> None:
        with client.admin.training_datasets.with_streaming_response.get_labeller_stats() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            training_dataset = response.parse()
            assert_matches_type(TrainingDatasetGetLabellerStatsResponse, training_dataset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_get_next_for_labeling(self, client: Structify) -> None:
        training_dataset = client.admin.training_datasets.get_next_for_labeling(
            dataset_name="dataset_name",
            status="unlabeled",
        )
        assert_matches_type(Optional[TrainingDatumResponse], training_dataset, path=["response"])

    @parametrize
    def test_raw_response_get_next_for_labeling(self, client: Structify) -> None:
        response = client.admin.training_datasets.with_raw_response.get_next_for_labeling(
            dataset_name="dataset_name",
            status="unlabeled",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        training_dataset = response.parse()
        assert_matches_type(Optional[TrainingDatumResponse], training_dataset, path=["response"])

    @parametrize
    def test_streaming_response_get_next_for_labeling(self, client: Structify) -> None:
        with client.admin.training_datasets.with_streaming_response.get_next_for_labeling(
            dataset_name="dataset_name",
            status="unlabeled",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            training_dataset = response.parse()
            assert_matches_type(Optional[TrainingDatumResponse], training_dataset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_get_next_for_qa(self, client: Structify) -> None:
        training_dataset = client.admin.training_datasets.get_next_for_qa(
            is_final_qa=True,
            status="unlabeled",
        )
        assert_matches_type(Optional[TrainingDatumResponse], training_dataset, path=["response"])

    @parametrize
    def test_method_get_next_for_qa_with_all_params(self, client: Structify) -> None:
        training_dataset = client.admin.training_datasets.get_next_for_qa(
            is_final_qa=True,
            status="unlabeled",
            dataset_name="dataset_name",
        )
        assert_matches_type(Optional[TrainingDatumResponse], training_dataset, path=["response"])

    @parametrize
    def test_raw_response_get_next_for_qa(self, client: Structify) -> None:
        response = client.admin.training_datasets.with_raw_response.get_next_for_qa(
            is_final_qa=True,
            status="unlabeled",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        training_dataset = response.parse()
        assert_matches_type(Optional[TrainingDatumResponse], training_dataset, path=["response"])

    @parametrize
    def test_streaming_response_get_next_for_qa(self, client: Structify) -> None:
        with client.admin.training_datasets.with_streaming_response.get_next_for_qa(
            is_final_qa=True,
            status="unlabeled",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            training_dataset = response.parse()
            assert_matches_type(Optional[TrainingDatumResponse], training_dataset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_get_next_suspicious(self, client: Structify) -> None:
        training_dataset = client.admin.training_datasets.get_next_suspicious(
            status="unlabeled",
        )
        assert_matches_type(Optional[TrainingDatumResponse], training_dataset, path=["response"])

    @parametrize
    def test_method_get_next_suspicious_with_all_params(self, client: Structify) -> None:
        training_dataset = client.admin.training_datasets.get_next_suspicious(
            status="unlabeled",
            dataset_name="dataset_name",
            user_restriction=True,
        )
        assert_matches_type(Optional[TrainingDatumResponse], training_dataset, path=["response"])

    @parametrize
    def test_raw_response_get_next_suspicious(self, client: Structify) -> None:
        response = client.admin.training_datasets.with_raw_response.get_next_suspicious(
            status="unlabeled",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        training_dataset = response.parse()
        assert_matches_type(Optional[TrainingDatumResponse], training_dataset, path=["response"])

    @parametrize
    def test_streaming_response_get_next_suspicious(self, client: Structify) -> None:
        with client.admin.training_datasets.with_streaming_response.get_next_suspicious(
            status="unlabeled",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            training_dataset = response.parse()
            assert_matches_type(Optional[TrainingDatumResponse], training_dataset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_label_datum(self, client: Structify) -> None:
        training_dataset = client.admin.training_datasets.label_datum(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            status="unlabeled",
            updated_tool_calls=[
                {
                    "input": {
                        "save": {
                            "entities": [
                                {
                                    "id": 0,
                                    "properties": {"foo": "string"},
                                    "type": "type",
                                }
                            ],
                            "relationships": [
                                {
                                    "source": 0,
                                    "target": 0,
                                    "type": "type",
                                }
                            ],
                        }
                    },
                    "name": "Exit",
                }
            ],
        )
        assert training_dataset is None

    @parametrize
    def test_raw_response_label_datum(self, client: Structify) -> None:
        response = client.admin.training_datasets.with_raw_response.label_datum(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            status="unlabeled",
            updated_tool_calls=[
                {
                    "input": {
                        "save": {
                            "entities": [
                                {
                                    "id": 0,
                                    "properties": {"foo": "string"},
                                    "type": "type",
                                }
                            ],
                            "relationships": [
                                {
                                    "source": 0,
                                    "target": 0,
                                    "type": "type",
                                }
                            ],
                        }
                    },
                    "name": "Exit",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        training_dataset = response.parse()
        assert training_dataset is None

    @parametrize
    def test_streaming_response_label_datum(self, client: Structify) -> None:
        with client.admin.training_datasets.with_streaming_response.label_datum(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            status="unlabeled",
            updated_tool_calls=[
                {
                    "input": {
                        "save": {
                            "entities": [
                                {
                                    "id": 0,
                                    "properties": {"foo": "string"},
                                    "type": "type",
                                }
                            ],
                            "relationships": [
                                {
                                    "source": 0,
                                    "target": 0,
                                    "type": "type",
                                }
                            ],
                        }
                    },
                    "name": "Exit",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            training_dataset = response.parse()
            assert training_dataset is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_list_datums(self, client: Structify) -> None:
        training_dataset = client.admin.training_datasets.list_datums(
            dataset_name="dataset_name",
        )
        assert_matches_type(TrainingDatasetListDatumsResponse, training_dataset, path=["response"])

    @parametrize
    def test_method_list_datums_with_all_params(self, client: Structify) -> None:
        training_dataset = client.admin.training_datasets.list_datums(
            dataset_name="dataset_name",
            last_updated=parse_datetime("2019-12-27T18:11:19.117Z"),
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
    def test_method_mark_datum_suspicious(self, client: Structify) -> None:
        training_dataset = client.admin.training_datasets.mark_datum_suspicious(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            message="message",
            status="unlabeled",
            suspicious_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert training_dataset is None

    @parametrize
    def test_raw_response_mark_datum_suspicious(self, client: Structify) -> None:
        response = client.admin.training_datasets.with_raw_response.mark_datum_suspicious(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            message="message",
            status="unlabeled",
            suspicious_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        training_dataset = response.parse()
        assert training_dataset is None

    @parametrize
    def test_streaming_response_mark_datum_suspicious(self, client: Structify) -> None:
        with client.admin.training_datasets.with_streaming_response.mark_datum_suspicious(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            message="message",
            status="unlabeled",
            suspicious_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            training_dataset = response.parse()
            assert training_dataset is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_remove_datum(self, client: Structify) -> None:
        training_dataset = client.admin.training_datasets.remove_datum(
            datum_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert training_dataset is None

    @parametrize
    def test_raw_response_remove_datum(self, client: Structify) -> None:
        response = client.admin.training_datasets.with_raw_response.remove_datum(
            datum_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        training_dataset = response.parse()
        assert training_dataset is None

    @parametrize
    def test_streaming_response_remove_datum(self, client: Structify) -> None:
        with client.admin.training_datasets.with_streaming_response.remove_datum(
            datum_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            training_dataset = response.parse()
            assert training_dataset is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_size(self, client: Structify) -> None:
        training_dataset = client.admin.training_datasets.size()
        assert_matches_type(TrainingDatasetSizeResponse, training_dataset, path=["response"])

    @parametrize
    def test_method_size_with_all_params(self, client: Structify) -> None:
        training_dataset = client.admin.training_datasets.size(
            dataset_name="dataset_name",
            end_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(TrainingDatasetSizeResponse, training_dataset, path=["response"])

    @parametrize
    def test_raw_response_size(self, client: Structify) -> None:
        response = client.admin.training_datasets.with_raw_response.size()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        training_dataset = response.parse()
        assert_matches_type(TrainingDatasetSizeResponse, training_dataset, path=["response"])

    @parametrize
    def test_streaming_response_size(self, client: Structify) -> None:
        with client.admin.training_datasets.with_streaming_response.size() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            training_dataset = response.parse()
            assert_matches_type(TrainingDatasetSizeResponse, training_dataset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_suspicious_count(self, client: Structify) -> None:
        training_dataset = client.admin.training_datasets.suspicious_count(
            status="unlabeled",
        )
        assert_matches_type(TrainingDatasetSuspiciousCountResponse, training_dataset, path=["response"])

    @parametrize
    def test_method_suspicious_count_with_all_params(self, client: Structify) -> None:
        training_dataset = client.admin.training_datasets.suspicious_count(
            status="unlabeled",
            dataset_name="dataset_name",
            user_restriction=True,
        )
        assert_matches_type(TrainingDatasetSuspiciousCountResponse, training_dataset, path=["response"])

    @parametrize
    def test_raw_response_suspicious_count(self, client: Structify) -> None:
        response = client.admin.training_datasets.with_raw_response.suspicious_count(
            status="unlabeled",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        training_dataset = response.parse()
        assert_matches_type(TrainingDatasetSuspiciousCountResponse, training_dataset, path=["response"])

    @parametrize
    def test_streaming_response_suspicious_count(self, client: Structify) -> None:
        with client.admin.training_datasets.with_streaming_response.suspicious_count(
            status="unlabeled",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            training_dataset = response.parse()
            assert_matches_type(TrainingDatasetSuspiciousCountResponse, training_dataset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_switch_dataset(self, client: Structify) -> None:
        training_dataset = client.admin.training_datasets.switch_dataset(
            dataset_name="dataset_name",
            datum_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert training_dataset is None

    @parametrize
    def test_raw_response_switch_dataset(self, client: Structify) -> None:
        response = client.admin.training_datasets.with_raw_response.switch_dataset(
            dataset_name="dataset_name",
            datum_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        training_dataset = response.parse()
        assert training_dataset is None

    @parametrize
    def test_streaming_response_switch_dataset(self, client: Structify) -> None:
        with client.admin.training_datasets.with_streaming_response.switch_dataset(
            dataset_name="dataset_name",
            datum_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            training_dataset = response.parse()
            assert training_dataset is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_update_datum_status(self, client: Structify) -> None:
        training_dataset = client.admin.training_datasets.update_datum_status(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            status="unlabeled",
        )
        assert training_dataset is None

    @parametrize
    def test_method_update_datum_status_with_all_params(self, client: Structify) -> None:
        training_dataset = client.admin.training_datasets.update_datum_status(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            status="unlabeled",
            review_message="review_message",
        )
        assert training_dataset is None

    @parametrize
    def test_raw_response_update_datum_status(self, client: Structify) -> None:
        response = client.admin.training_datasets.with_raw_response.update_datum_status(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            status="unlabeled",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        training_dataset = response.parse()
        assert training_dataset is None

    @parametrize
    def test_streaming_response_update_datum_status(self, client: Structify) -> None:
        with client.admin.training_datasets.with_streaming_response.update_datum_status(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            status="unlabeled",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            training_dataset = response.parse()
            assert training_dataset is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_upload_labeled_step(self, client: Structify) -> None:
        training_dataset = client.admin.training_datasets.upload_labeled_step(
            dataset_name=b"raw file contents",
            step_bytes=b"raw file contents",
        )
        assert training_dataset is None

    @parametrize
    def test_raw_response_upload_labeled_step(self, client: Structify) -> None:
        response = client.admin.training_datasets.with_raw_response.upload_labeled_step(
            dataset_name=b"raw file contents",
            step_bytes=b"raw file contents",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        training_dataset = response.parse()
        assert training_dataset is None

    @parametrize
    def test_streaming_response_upload_labeled_step(self, client: Structify) -> None:
        with client.admin.training_datasets.with_streaming_response.upload_labeled_step(
            dataset_name=b"raw file contents",
            step_bytes=b"raw file contents",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            training_dataset = response.parse()
            assert training_dataset is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_verify_datum(self, client: Structify) -> None:
        training_dataset = client.admin.training_datasets.verify_datum(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            status="unlabeled",
            verified_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert training_dataset is None

    @parametrize
    def test_raw_response_verify_datum(self, client: Structify) -> None:
        response = client.admin.training_datasets.with_raw_response.verify_datum(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            status="unlabeled",
            verified_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        training_dataset = response.parse()
        assert training_dataset is None

    @parametrize
    def test_streaming_response_verify_datum(self, client: Structify) -> None:
        with client.admin.training_datasets.with_streaming_response.verify_datum(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            status="unlabeled",
            verified_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            training_dataset = response.parse()
            assert training_dataset is None

        assert cast(Any, response.is_closed) is True


class TestAsyncTrainingDatasets:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

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
    async def test_method_delete(self, async_client: AsyncStructify) -> None:
        training_dataset = await async_client.admin.training_datasets.delete(
            dataset_name="dataset_name",
        )
        assert training_dataset is None

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncStructify) -> None:
        response = await async_client.admin.training_datasets.with_raw_response.delete(
            dataset_name="dataset_name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        training_dataset = await response.parse()
        assert training_dataset is None

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncStructify) -> None:
        async with async_client.admin.training_datasets.with_streaming_response.delete(
            dataset_name="dataset_name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            training_dataset = await response.parse()
            assert training_dataset is None

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
    @pytest.mark.respx(base_url=base_url)
    async def test_method_download_datum(self, async_client: AsyncStructify, respx_mock: MockRouter) -> None:
        respx_mock.get("/admin/training_datasets/download_datum_step").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        training_dataset = await async_client.admin.training_datasets.download_datum(
            datum_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert training_dataset.is_closed
        assert await training_dataset.json() == {"foo": "bar"}
        assert cast(Any, training_dataset.is_closed) is True
        assert isinstance(training_dataset, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_download_datum_with_all_params(
        self, async_client: AsyncStructify, respx_mock: MockRouter
    ) -> None:
        respx_mock.get("/admin/training_datasets/download_datum_step").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        training_dataset = await async_client.admin.training_datasets.download_datum(
            datum_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            require_labels=True,
        )
        assert training_dataset.is_closed
        assert await training_dataset.json() == {"foo": "bar"}
        assert cast(Any, training_dataset.is_closed) is True
        assert isinstance(training_dataset, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_raw_response_download_datum(self, async_client: AsyncStructify, respx_mock: MockRouter) -> None:
        respx_mock.get("/admin/training_datasets/download_datum_step").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )

        training_dataset = await async_client.admin.training_datasets.with_raw_response.download_datum(
            datum_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert training_dataset.is_closed is True
        assert training_dataset.http_request.headers.get("X-Stainless-Lang") == "python"
        assert await training_dataset.json() == {"foo": "bar"}
        assert isinstance(training_dataset, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_streaming_response_download_datum(
        self, async_client: AsyncStructify, respx_mock: MockRouter
    ) -> None:
        respx_mock.get("/admin/training_datasets/download_datum_step").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        async with async_client.admin.training_datasets.with_streaming_response.download_datum(
            datum_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as training_dataset:
            assert not training_dataset.is_closed
            assert training_dataset.http_request.headers.get("X-Stainless-Lang") == "python"

            assert await training_dataset.json() == {"foo": "bar"}
            assert cast(Any, training_dataset.is_closed) is True
            assert isinstance(training_dataset, AsyncStreamedBinaryAPIResponse)

        assert cast(Any, training_dataset.is_closed) is True

    @parametrize
    async def test_method_get_datum_info(self, async_client: AsyncStructify) -> None:
        training_dataset = await async_client.admin.training_datasets.get_datum_info(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(TrainingDatumResponse, training_dataset, path=["response"])

    @parametrize
    async def test_raw_response_get_datum_info(self, async_client: AsyncStructify) -> None:
        response = await async_client.admin.training_datasets.with_raw_response.get_datum_info(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        training_dataset = await response.parse()
        assert_matches_type(TrainingDatumResponse, training_dataset, path=["response"])

    @parametrize
    async def test_streaming_response_get_datum_info(self, async_client: AsyncStructify) -> None:
        async with async_client.admin.training_datasets.with_streaming_response.get_datum_info(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            training_dataset = await response.parse()
            assert_matches_type(TrainingDatumResponse, training_dataset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_get_labeller_stats(self, async_client: AsyncStructify) -> None:
        training_dataset = await async_client.admin.training_datasets.get_labeller_stats()
        assert_matches_type(TrainingDatasetGetLabellerStatsResponse, training_dataset, path=["response"])

    @parametrize
    async def test_method_get_labeller_stats_with_all_params(self, async_client: AsyncStructify) -> None:
        training_dataset = await async_client.admin.training_datasets.get_labeller_stats(
            end_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            labeled_status="None",
            max_prop_count=0,
            start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            time_bucket="Second",
        )
        assert_matches_type(TrainingDatasetGetLabellerStatsResponse, training_dataset, path=["response"])

    @parametrize
    async def test_raw_response_get_labeller_stats(self, async_client: AsyncStructify) -> None:
        response = await async_client.admin.training_datasets.with_raw_response.get_labeller_stats()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        training_dataset = await response.parse()
        assert_matches_type(TrainingDatasetGetLabellerStatsResponse, training_dataset, path=["response"])

    @parametrize
    async def test_streaming_response_get_labeller_stats(self, async_client: AsyncStructify) -> None:
        async with async_client.admin.training_datasets.with_streaming_response.get_labeller_stats() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            training_dataset = await response.parse()
            assert_matches_type(TrainingDatasetGetLabellerStatsResponse, training_dataset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_get_next_for_labeling(self, async_client: AsyncStructify) -> None:
        training_dataset = await async_client.admin.training_datasets.get_next_for_labeling(
            dataset_name="dataset_name",
            status="unlabeled",
        )
        assert_matches_type(Optional[TrainingDatumResponse], training_dataset, path=["response"])

    @parametrize
    async def test_raw_response_get_next_for_labeling(self, async_client: AsyncStructify) -> None:
        response = await async_client.admin.training_datasets.with_raw_response.get_next_for_labeling(
            dataset_name="dataset_name",
            status="unlabeled",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        training_dataset = await response.parse()
        assert_matches_type(Optional[TrainingDatumResponse], training_dataset, path=["response"])

    @parametrize
    async def test_streaming_response_get_next_for_labeling(self, async_client: AsyncStructify) -> None:
        async with async_client.admin.training_datasets.with_streaming_response.get_next_for_labeling(
            dataset_name="dataset_name",
            status="unlabeled",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            training_dataset = await response.parse()
            assert_matches_type(Optional[TrainingDatumResponse], training_dataset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_get_next_for_qa(self, async_client: AsyncStructify) -> None:
        training_dataset = await async_client.admin.training_datasets.get_next_for_qa(
            is_final_qa=True,
            status="unlabeled",
        )
        assert_matches_type(Optional[TrainingDatumResponse], training_dataset, path=["response"])

    @parametrize
    async def test_method_get_next_for_qa_with_all_params(self, async_client: AsyncStructify) -> None:
        training_dataset = await async_client.admin.training_datasets.get_next_for_qa(
            is_final_qa=True,
            status="unlabeled",
            dataset_name="dataset_name",
        )
        assert_matches_type(Optional[TrainingDatumResponse], training_dataset, path=["response"])

    @parametrize
    async def test_raw_response_get_next_for_qa(self, async_client: AsyncStructify) -> None:
        response = await async_client.admin.training_datasets.with_raw_response.get_next_for_qa(
            is_final_qa=True,
            status="unlabeled",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        training_dataset = await response.parse()
        assert_matches_type(Optional[TrainingDatumResponse], training_dataset, path=["response"])

    @parametrize
    async def test_streaming_response_get_next_for_qa(self, async_client: AsyncStructify) -> None:
        async with async_client.admin.training_datasets.with_streaming_response.get_next_for_qa(
            is_final_qa=True,
            status="unlabeled",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            training_dataset = await response.parse()
            assert_matches_type(Optional[TrainingDatumResponse], training_dataset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_get_next_suspicious(self, async_client: AsyncStructify) -> None:
        training_dataset = await async_client.admin.training_datasets.get_next_suspicious(
            status="unlabeled",
        )
        assert_matches_type(Optional[TrainingDatumResponse], training_dataset, path=["response"])

    @parametrize
    async def test_method_get_next_suspicious_with_all_params(self, async_client: AsyncStructify) -> None:
        training_dataset = await async_client.admin.training_datasets.get_next_suspicious(
            status="unlabeled",
            dataset_name="dataset_name",
            user_restriction=True,
        )
        assert_matches_type(Optional[TrainingDatumResponse], training_dataset, path=["response"])

    @parametrize
    async def test_raw_response_get_next_suspicious(self, async_client: AsyncStructify) -> None:
        response = await async_client.admin.training_datasets.with_raw_response.get_next_suspicious(
            status="unlabeled",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        training_dataset = await response.parse()
        assert_matches_type(Optional[TrainingDatumResponse], training_dataset, path=["response"])

    @parametrize
    async def test_streaming_response_get_next_suspicious(self, async_client: AsyncStructify) -> None:
        async with async_client.admin.training_datasets.with_streaming_response.get_next_suspicious(
            status="unlabeled",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            training_dataset = await response.parse()
            assert_matches_type(Optional[TrainingDatumResponse], training_dataset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_label_datum(self, async_client: AsyncStructify) -> None:
        training_dataset = await async_client.admin.training_datasets.label_datum(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            status="unlabeled",
            updated_tool_calls=[
                {
                    "input": {
                        "save": {
                            "entities": [
                                {
                                    "id": 0,
                                    "properties": {"foo": "string"},
                                    "type": "type",
                                }
                            ],
                            "relationships": [
                                {
                                    "source": 0,
                                    "target": 0,
                                    "type": "type",
                                }
                            ],
                        }
                    },
                    "name": "Exit",
                }
            ],
        )
        assert training_dataset is None

    @parametrize
    async def test_raw_response_label_datum(self, async_client: AsyncStructify) -> None:
        response = await async_client.admin.training_datasets.with_raw_response.label_datum(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            status="unlabeled",
            updated_tool_calls=[
                {
                    "input": {
                        "save": {
                            "entities": [
                                {
                                    "id": 0,
                                    "properties": {"foo": "string"},
                                    "type": "type",
                                }
                            ],
                            "relationships": [
                                {
                                    "source": 0,
                                    "target": 0,
                                    "type": "type",
                                }
                            ],
                        }
                    },
                    "name": "Exit",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        training_dataset = await response.parse()
        assert training_dataset is None

    @parametrize
    async def test_streaming_response_label_datum(self, async_client: AsyncStructify) -> None:
        async with async_client.admin.training_datasets.with_streaming_response.label_datum(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            status="unlabeled",
            updated_tool_calls=[
                {
                    "input": {
                        "save": {
                            "entities": [
                                {
                                    "id": 0,
                                    "properties": {"foo": "string"},
                                    "type": "type",
                                }
                            ],
                            "relationships": [
                                {
                                    "source": 0,
                                    "target": 0,
                                    "type": "type",
                                }
                            ],
                        }
                    },
                    "name": "Exit",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            training_dataset = await response.parse()
            assert training_dataset is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_list_datums(self, async_client: AsyncStructify) -> None:
        training_dataset = await async_client.admin.training_datasets.list_datums(
            dataset_name="dataset_name",
        )
        assert_matches_type(TrainingDatasetListDatumsResponse, training_dataset, path=["response"])

    @parametrize
    async def test_method_list_datums_with_all_params(self, async_client: AsyncStructify) -> None:
        training_dataset = await async_client.admin.training_datasets.list_datums(
            dataset_name="dataset_name",
            last_updated=parse_datetime("2019-12-27T18:11:19.117Z"),
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
    async def test_method_mark_datum_suspicious(self, async_client: AsyncStructify) -> None:
        training_dataset = await async_client.admin.training_datasets.mark_datum_suspicious(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            message="message",
            status="unlabeled",
            suspicious_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert training_dataset is None

    @parametrize
    async def test_raw_response_mark_datum_suspicious(self, async_client: AsyncStructify) -> None:
        response = await async_client.admin.training_datasets.with_raw_response.mark_datum_suspicious(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            message="message",
            status="unlabeled",
            suspicious_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        training_dataset = await response.parse()
        assert training_dataset is None

    @parametrize
    async def test_streaming_response_mark_datum_suspicious(self, async_client: AsyncStructify) -> None:
        async with async_client.admin.training_datasets.with_streaming_response.mark_datum_suspicious(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            message="message",
            status="unlabeled",
            suspicious_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            training_dataset = await response.parse()
            assert training_dataset is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_remove_datum(self, async_client: AsyncStructify) -> None:
        training_dataset = await async_client.admin.training_datasets.remove_datum(
            datum_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert training_dataset is None

    @parametrize
    async def test_raw_response_remove_datum(self, async_client: AsyncStructify) -> None:
        response = await async_client.admin.training_datasets.with_raw_response.remove_datum(
            datum_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        training_dataset = await response.parse()
        assert training_dataset is None

    @parametrize
    async def test_streaming_response_remove_datum(self, async_client: AsyncStructify) -> None:
        async with async_client.admin.training_datasets.with_streaming_response.remove_datum(
            datum_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            training_dataset = await response.parse()
            assert training_dataset is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_size(self, async_client: AsyncStructify) -> None:
        training_dataset = await async_client.admin.training_datasets.size()
        assert_matches_type(TrainingDatasetSizeResponse, training_dataset, path=["response"])

    @parametrize
    async def test_method_size_with_all_params(self, async_client: AsyncStructify) -> None:
        training_dataset = await async_client.admin.training_datasets.size(
            dataset_name="dataset_name",
            end_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(TrainingDatasetSizeResponse, training_dataset, path=["response"])

    @parametrize
    async def test_raw_response_size(self, async_client: AsyncStructify) -> None:
        response = await async_client.admin.training_datasets.with_raw_response.size()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        training_dataset = await response.parse()
        assert_matches_type(TrainingDatasetSizeResponse, training_dataset, path=["response"])

    @parametrize
    async def test_streaming_response_size(self, async_client: AsyncStructify) -> None:
        async with async_client.admin.training_datasets.with_streaming_response.size() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            training_dataset = await response.parse()
            assert_matches_type(TrainingDatasetSizeResponse, training_dataset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_suspicious_count(self, async_client: AsyncStructify) -> None:
        training_dataset = await async_client.admin.training_datasets.suspicious_count(
            status="unlabeled",
        )
        assert_matches_type(TrainingDatasetSuspiciousCountResponse, training_dataset, path=["response"])

    @parametrize
    async def test_method_suspicious_count_with_all_params(self, async_client: AsyncStructify) -> None:
        training_dataset = await async_client.admin.training_datasets.suspicious_count(
            status="unlabeled",
            dataset_name="dataset_name",
            user_restriction=True,
        )
        assert_matches_type(TrainingDatasetSuspiciousCountResponse, training_dataset, path=["response"])

    @parametrize
    async def test_raw_response_suspicious_count(self, async_client: AsyncStructify) -> None:
        response = await async_client.admin.training_datasets.with_raw_response.suspicious_count(
            status="unlabeled",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        training_dataset = await response.parse()
        assert_matches_type(TrainingDatasetSuspiciousCountResponse, training_dataset, path=["response"])

    @parametrize
    async def test_streaming_response_suspicious_count(self, async_client: AsyncStructify) -> None:
        async with async_client.admin.training_datasets.with_streaming_response.suspicious_count(
            status="unlabeled",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            training_dataset = await response.parse()
            assert_matches_type(TrainingDatasetSuspiciousCountResponse, training_dataset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_switch_dataset(self, async_client: AsyncStructify) -> None:
        training_dataset = await async_client.admin.training_datasets.switch_dataset(
            dataset_name="dataset_name",
            datum_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert training_dataset is None

    @parametrize
    async def test_raw_response_switch_dataset(self, async_client: AsyncStructify) -> None:
        response = await async_client.admin.training_datasets.with_raw_response.switch_dataset(
            dataset_name="dataset_name",
            datum_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        training_dataset = await response.parse()
        assert training_dataset is None

    @parametrize
    async def test_streaming_response_switch_dataset(self, async_client: AsyncStructify) -> None:
        async with async_client.admin.training_datasets.with_streaming_response.switch_dataset(
            dataset_name="dataset_name",
            datum_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            training_dataset = await response.parse()
            assert training_dataset is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_update_datum_status(self, async_client: AsyncStructify) -> None:
        training_dataset = await async_client.admin.training_datasets.update_datum_status(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            status="unlabeled",
        )
        assert training_dataset is None

    @parametrize
    async def test_method_update_datum_status_with_all_params(self, async_client: AsyncStructify) -> None:
        training_dataset = await async_client.admin.training_datasets.update_datum_status(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            status="unlabeled",
            review_message="review_message",
        )
        assert training_dataset is None

    @parametrize
    async def test_raw_response_update_datum_status(self, async_client: AsyncStructify) -> None:
        response = await async_client.admin.training_datasets.with_raw_response.update_datum_status(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            status="unlabeled",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        training_dataset = await response.parse()
        assert training_dataset is None

    @parametrize
    async def test_streaming_response_update_datum_status(self, async_client: AsyncStructify) -> None:
        async with async_client.admin.training_datasets.with_streaming_response.update_datum_status(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            status="unlabeled",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            training_dataset = await response.parse()
            assert training_dataset is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_upload_labeled_step(self, async_client: AsyncStructify) -> None:
        training_dataset = await async_client.admin.training_datasets.upload_labeled_step(
            dataset_name=b"raw file contents",
            step_bytes=b"raw file contents",
        )
        assert training_dataset is None

    @parametrize
    async def test_raw_response_upload_labeled_step(self, async_client: AsyncStructify) -> None:
        response = await async_client.admin.training_datasets.with_raw_response.upload_labeled_step(
            dataset_name=b"raw file contents",
            step_bytes=b"raw file contents",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        training_dataset = await response.parse()
        assert training_dataset is None

    @parametrize
    async def test_streaming_response_upload_labeled_step(self, async_client: AsyncStructify) -> None:
        async with async_client.admin.training_datasets.with_streaming_response.upload_labeled_step(
            dataset_name=b"raw file contents",
            step_bytes=b"raw file contents",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            training_dataset = await response.parse()
            assert training_dataset is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_verify_datum(self, async_client: AsyncStructify) -> None:
        training_dataset = await async_client.admin.training_datasets.verify_datum(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            status="unlabeled",
            verified_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert training_dataset is None

    @parametrize
    async def test_raw_response_verify_datum(self, async_client: AsyncStructify) -> None:
        response = await async_client.admin.training_datasets.with_raw_response.verify_datum(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            status="unlabeled",
            verified_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        training_dataset = await response.parse()
        assert training_dataset is None

    @parametrize
    async def test_streaming_response_verify_datum(self, async_client: AsyncStructify) -> None:
        async with async_client.admin.training_datasets.with_streaming_response.verify_datum(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            status="unlabeled",
            verified_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            training_dataset = await response.parse()
            assert training_dataset is None

        assert cast(Any, response.is_closed) is True
