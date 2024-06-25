# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from structify import Structify, AsyncStructify
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestUpdate:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Structify) -> None:
        update = client.label.update.create(
            0,
            run_uuid="string",
            body=[
                {
                    "input": {"save": {}},
                    "name": "Save",
                },
                {
                    "input": {"save": {}},
                    "name": "Save",
                },
                {
                    "input": {"save": {}},
                    "name": "Save",
                },
            ],
        )
        assert_matches_type(str, update, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Structify) -> None:
        response = client.label.update.with_raw_response.create(
            0,
            run_uuid="string",
            body=[
                {
                    "input": {"save": {}},
                    "name": "Save",
                },
                {
                    "input": {"save": {}},
                    "name": "Save",
                },
                {
                    "input": {"save": {}},
                    "name": "Save",
                },
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        update = response.parse()
        assert_matches_type(str, update, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Structify) -> None:
        with client.label.update.with_streaming_response.create(
            0,
            run_uuid="string",
            body=[
                {
                    "input": {"save": {}},
                    "name": "Save",
                },
                {
                    "input": {"save": {}},
                    "name": "Save",
                },
                {
                    "input": {"save": {}},
                    "name": "Save",
                },
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            update = response.parse()
            assert_matches_type(str, update, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: Structify) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `run_uuid` but received ''"):
            client.label.update.with_raw_response.create(
                0,
                run_uuid="",
                body=[
                    {
                        "input": {"save": {}},
                        "name": "Save",
                    },
                    {
                        "input": {"save": {}},
                        "name": "Save",
                    },
                    {
                        "input": {"save": {}},
                        "name": "Save",
                    },
                ],
            )


class TestAsyncUpdate:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncStructify) -> None:
        update = await async_client.label.update.create(
            0,
            run_uuid="string",
            body=[
                {
                    "input": {"save": {}},
                    "name": "Save",
                },
                {
                    "input": {"save": {}},
                    "name": "Save",
                },
                {
                    "input": {"save": {}},
                    "name": "Save",
                },
            ],
        )
        assert_matches_type(str, update, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncStructify) -> None:
        response = await async_client.label.update.with_raw_response.create(
            0,
            run_uuid="string",
            body=[
                {
                    "input": {"save": {}},
                    "name": "Save",
                },
                {
                    "input": {"save": {}},
                    "name": "Save",
                },
                {
                    "input": {"save": {}},
                    "name": "Save",
                },
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        update = await response.parse()
        assert_matches_type(str, update, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncStructify) -> None:
        async with async_client.label.update.with_streaming_response.create(
            0,
            run_uuid="string",
            body=[
                {
                    "input": {"save": {}},
                    "name": "Save",
                },
                {
                    "input": {"save": {}},
                    "name": "Save",
                },
                {
                    "input": {"save": {}},
                    "name": "Save",
                },
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            update = await response.parse()
            assert_matches_type(str, update, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncStructify) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `run_uuid` but received ''"):
            await async_client.label.update.with_raw_response.create(
                0,
                run_uuid="",
                body=[
                    {
                        "input": {"save": {}},
                        "name": "Save",
                    },
                    {
                        "input": {"save": {}},
                        "name": "Save",
                    },
                    {
                        "input": {"save": {}},
                        "name": "Save",
                    },
                ],
            )
