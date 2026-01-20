# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from structify import Structify, AsyncStructify
from tests.utils import assert_matches_type
from structify.types import EstimateCostResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestWhitelabel:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_estimate_cost(self, client: Structify) -> None:
        whitelabel = client.whitelabel.estimate_cost(
            path="path",
            service="service",
        )
        assert_matches_type(EstimateCostResponse, whitelabel, path=["response"])

    @parametrize
    def test_raw_response_estimate_cost(self, client: Structify) -> None:
        response = client.whitelabel.with_raw_response.estimate_cost(
            path="path",
            service="service",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        whitelabel = response.parse()
        assert_matches_type(EstimateCostResponse, whitelabel, path=["response"])

    @parametrize
    def test_streaming_response_estimate_cost(self, client: Structify) -> None:
        with client.whitelabel.with_streaming_response.estimate_cost(
            path="path",
            service="service",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            whitelabel = response.parse()
            assert_matches_type(EstimateCostResponse, whitelabel, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_estimate_cost(self, client: Structify) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `service` but received ''"):
            client.whitelabel.with_raw_response.estimate_cost(
                path="path",
                service="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path` but received ''"):
            client.whitelabel.with_raw_response.estimate_cost(
                path="",
                service="service",
            )

    @parametrize
    def test_method_proxy_get(self, client: Structify) -> None:
        whitelabel = client.whitelabel.proxy_get(
            path="path",
            service="service",
        )
        assert whitelabel is None

    @parametrize
    def test_raw_response_proxy_get(self, client: Structify) -> None:
        response = client.whitelabel.with_raw_response.proxy_get(
            path="path",
            service="service",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        whitelabel = response.parse()
        assert whitelabel is None

    @parametrize
    def test_streaming_response_proxy_get(self, client: Structify) -> None:
        with client.whitelabel.with_streaming_response.proxy_get(
            path="path",
            service="service",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            whitelabel = response.parse()
            assert whitelabel is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_proxy_get(self, client: Structify) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `service` but received ''"):
            client.whitelabel.with_raw_response.proxy_get(
                path="path",
                service="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path` but received ''"):
            client.whitelabel.with_raw_response.proxy_get(
                path="",
                service="service",
            )

    @parametrize
    def test_method_proxy_post(self, client: Structify) -> None:
        whitelabel = client.whitelabel.proxy_post(
            path="path",
            service="service",
        )
        assert whitelabel is None

    @parametrize
    def test_raw_response_proxy_post(self, client: Structify) -> None:
        response = client.whitelabel.with_raw_response.proxy_post(
            path="path",
            service="service",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        whitelabel = response.parse()
        assert whitelabel is None

    @parametrize
    def test_streaming_response_proxy_post(self, client: Structify) -> None:
        with client.whitelabel.with_streaming_response.proxy_post(
            path="path",
            service="service",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            whitelabel = response.parse()
            assert whitelabel is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_proxy_post(self, client: Structify) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `service` but received ''"):
            client.whitelabel.with_raw_response.proxy_post(
                path="path",
                service="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path` but received ''"):
            client.whitelabel.with_raw_response.proxy_post(
                path="",
                service="service",
            )


class TestAsyncWhitelabel:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_estimate_cost(self, async_client: AsyncStructify) -> None:
        whitelabel = await async_client.whitelabel.estimate_cost(
            path="path",
            service="service",
        )
        assert_matches_type(EstimateCostResponse, whitelabel, path=["response"])

    @parametrize
    async def test_raw_response_estimate_cost(self, async_client: AsyncStructify) -> None:
        response = await async_client.whitelabel.with_raw_response.estimate_cost(
            path="path",
            service="service",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        whitelabel = await response.parse()
        assert_matches_type(EstimateCostResponse, whitelabel, path=["response"])

    @parametrize
    async def test_streaming_response_estimate_cost(self, async_client: AsyncStructify) -> None:
        async with async_client.whitelabel.with_streaming_response.estimate_cost(
            path="path",
            service="service",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            whitelabel = await response.parse()
            assert_matches_type(EstimateCostResponse, whitelabel, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_estimate_cost(self, async_client: AsyncStructify) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `service` but received ''"):
            await async_client.whitelabel.with_raw_response.estimate_cost(
                path="path",
                service="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path` but received ''"):
            await async_client.whitelabel.with_raw_response.estimate_cost(
                path="",
                service="service",
            )

    @parametrize
    async def test_method_proxy_get(self, async_client: AsyncStructify) -> None:
        whitelabel = await async_client.whitelabel.proxy_get(
            path="path",
            service="service",
        )
        assert whitelabel is None

    @parametrize
    async def test_raw_response_proxy_get(self, async_client: AsyncStructify) -> None:
        response = await async_client.whitelabel.with_raw_response.proxy_get(
            path="path",
            service="service",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        whitelabel = await response.parse()
        assert whitelabel is None

    @parametrize
    async def test_streaming_response_proxy_get(self, async_client: AsyncStructify) -> None:
        async with async_client.whitelabel.with_streaming_response.proxy_get(
            path="path",
            service="service",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            whitelabel = await response.parse()
            assert whitelabel is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_proxy_get(self, async_client: AsyncStructify) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `service` but received ''"):
            await async_client.whitelabel.with_raw_response.proxy_get(
                path="path",
                service="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path` but received ''"):
            await async_client.whitelabel.with_raw_response.proxy_get(
                path="",
                service="service",
            )

    @parametrize
    async def test_method_proxy_post(self, async_client: AsyncStructify) -> None:
        whitelabel = await async_client.whitelabel.proxy_post(
            path="path",
            service="service",
        )
        assert whitelabel is None

    @parametrize
    async def test_raw_response_proxy_post(self, async_client: AsyncStructify) -> None:
        response = await async_client.whitelabel.with_raw_response.proxy_post(
            path="path",
            service="service",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        whitelabel = await response.parse()
        assert whitelabel is None

    @parametrize
    async def test_streaming_response_proxy_post(self, async_client: AsyncStructify) -> None:
        async with async_client.whitelabel.with_streaming_response.proxy_post(
            path="path",
            service="service",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            whitelabel = await response.parse()
            assert whitelabel is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_proxy_post(self, async_client: AsyncStructify) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `service` but received ''"):
            await async_client.whitelabel.with_raw_response.proxy_post(
                path="path",
                service="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path` but received ''"):
            await async_client.whitelabel.with_raw_response.proxy_post(
                path="",
                service="service",
            )
