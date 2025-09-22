# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from structify import Structify, AsyncStructify
from tests.utils import assert_matches_type
from structify.types.external import (
    LocationResponse,
    GoogleSearchResponse,
    SearchAPIGoogleMapsSearchResponse,
    SearchAPIGoogleFlightsSearchResponse,
    SearchAPIGoogleScholarSearchResponse,
    SearchAPIGoogleFlightsCalendarResponse,
    SearchAPIGoogleMapsPlacePhotosResponse,
    SearchAPIGoogleMapsPlaceDetailsResponse,
    SearchAPIGoogleMapsPlaceReviewsResponse,
    SearchAPIGoogleScholarCitationsResponse,
    SearchAPIGoogleScholarAuthorSearchResponse,
    SearchAPIGoogleFlightsLocationSearchResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSearchAPI:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_google_flights_calendar(self, client: Structify) -> None:
        search_api = client.external.search_api.google_flights_calendar(
            arrival_id="arrival_id",
            departure_id="departure_id",
            outbound_date="outbound_date",
        )
        assert_matches_type(SearchAPIGoogleFlightsCalendarResponse, search_api, path=["response"])

    @parametrize
    def test_method_google_flights_calendar_with_all_params(self, client: Structify) -> None:
        search_api = client.external.search_api.google_flights_calendar(
            arrival_id="arrival_id",
            departure_id="departure_id",
            outbound_date="outbound_date",
            currency="currency",
            hl="hl",
            return_date="return_date",
        )
        assert_matches_type(SearchAPIGoogleFlightsCalendarResponse, search_api, path=["response"])

    @parametrize
    def test_raw_response_google_flights_calendar(self, client: Structify) -> None:
        response = client.external.search_api.with_raw_response.google_flights_calendar(
            arrival_id="arrival_id",
            departure_id="departure_id",
            outbound_date="outbound_date",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        search_api = response.parse()
        assert_matches_type(SearchAPIGoogleFlightsCalendarResponse, search_api, path=["response"])

    @parametrize
    def test_streaming_response_google_flights_calendar(self, client: Structify) -> None:
        with client.external.search_api.with_streaming_response.google_flights_calendar(
            arrival_id="arrival_id",
            departure_id="departure_id",
            outbound_date="outbound_date",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            search_api = response.parse()
            assert_matches_type(SearchAPIGoogleFlightsCalendarResponse, search_api, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_google_flights_location_search(self, client: Structify) -> None:
        search_api = client.external.search_api.google_flights_location_search(
            q="q",
        )
        assert_matches_type(SearchAPIGoogleFlightsLocationSearchResponse, search_api, path=["response"])

    @parametrize
    def test_method_google_flights_location_search_with_all_params(self, client: Structify) -> None:
        search_api = client.external.search_api.google_flights_location_search(
            q="q",
            hl="hl",
        )
        assert_matches_type(SearchAPIGoogleFlightsLocationSearchResponse, search_api, path=["response"])

    @parametrize
    def test_raw_response_google_flights_location_search(self, client: Structify) -> None:
        response = client.external.search_api.with_raw_response.google_flights_location_search(
            q="q",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        search_api = response.parse()
        assert_matches_type(SearchAPIGoogleFlightsLocationSearchResponse, search_api, path=["response"])

    @parametrize
    def test_streaming_response_google_flights_location_search(self, client: Structify) -> None:
        with client.external.search_api.with_streaming_response.google_flights_location_search(
            q="q",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            search_api = response.parse()
            assert_matches_type(SearchAPIGoogleFlightsLocationSearchResponse, search_api, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_google_flights_search(self, client: Structify) -> None:
        search_api = client.external.search_api.google_flights_search(
            arrival_id="arrival_id",
            departure_id="departure_id",
            outbound_date="outbound_date",
        )
        assert_matches_type(SearchAPIGoogleFlightsSearchResponse, search_api, path=["response"])

    @parametrize
    def test_method_google_flights_search_with_all_params(self, client: Structify) -> None:
        search_api = client.external.search_api.google_flights_search(
            arrival_id="arrival_id",
            departure_id="departure_id",
            outbound_date="outbound_date",
            adults=0,
            children=0,
            currency="currency",
            hl="hl",
            infants_in_seat=0,
            infants_on_lap=0,
            return_date="return_date",
            travel_class="travel_class",
        )
        assert_matches_type(SearchAPIGoogleFlightsSearchResponse, search_api, path=["response"])

    @parametrize
    def test_raw_response_google_flights_search(self, client: Structify) -> None:
        response = client.external.search_api.with_raw_response.google_flights_search(
            arrival_id="arrival_id",
            departure_id="departure_id",
            outbound_date="outbound_date",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        search_api = response.parse()
        assert_matches_type(SearchAPIGoogleFlightsSearchResponse, search_api, path=["response"])

    @parametrize
    def test_streaming_response_google_flights_search(self, client: Structify) -> None:
        with client.external.search_api.with_streaming_response.google_flights_search(
            arrival_id="arrival_id",
            departure_id="departure_id",
            outbound_date="outbound_date",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            search_api = response.parse()
            assert_matches_type(SearchAPIGoogleFlightsSearchResponse, search_api, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_google_maps_place_details(self, client: Structify) -> None:
        search_api = client.external.search_api.google_maps_place_details(
            place_id="place_id",
        )
        assert_matches_type(SearchAPIGoogleMapsPlaceDetailsResponse, search_api, path=["response"])

    @parametrize
    def test_method_google_maps_place_details_with_all_params(self, client: Structify) -> None:
        search_api = client.external.search_api.google_maps_place_details(
            place_id="place_id",
            hl="hl",
        )
        assert_matches_type(SearchAPIGoogleMapsPlaceDetailsResponse, search_api, path=["response"])

    @parametrize
    def test_raw_response_google_maps_place_details(self, client: Structify) -> None:
        response = client.external.search_api.with_raw_response.google_maps_place_details(
            place_id="place_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        search_api = response.parse()
        assert_matches_type(SearchAPIGoogleMapsPlaceDetailsResponse, search_api, path=["response"])

    @parametrize
    def test_streaming_response_google_maps_place_details(self, client: Structify) -> None:
        with client.external.search_api.with_streaming_response.google_maps_place_details(
            place_id="place_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            search_api = response.parse()
            assert_matches_type(SearchAPIGoogleMapsPlaceDetailsResponse, search_api, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_google_maps_place_photos(self, client: Structify) -> None:
        search_api = client.external.search_api.google_maps_place_photos(
            place_id="place_id",
        )
        assert_matches_type(SearchAPIGoogleMapsPlacePhotosResponse, search_api, path=["response"])

    @parametrize
    def test_method_google_maps_place_photos_with_all_params(self, client: Structify) -> None:
        search_api = client.external.search_api.google_maps_place_photos(
            place_id="place_id",
            num=0,
        )
        assert_matches_type(SearchAPIGoogleMapsPlacePhotosResponse, search_api, path=["response"])

    @parametrize
    def test_raw_response_google_maps_place_photos(self, client: Structify) -> None:
        response = client.external.search_api.with_raw_response.google_maps_place_photos(
            place_id="place_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        search_api = response.parse()
        assert_matches_type(SearchAPIGoogleMapsPlacePhotosResponse, search_api, path=["response"])

    @parametrize
    def test_streaming_response_google_maps_place_photos(self, client: Structify) -> None:
        with client.external.search_api.with_streaming_response.google_maps_place_photos(
            place_id="place_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            search_api = response.parse()
            assert_matches_type(SearchAPIGoogleMapsPlacePhotosResponse, search_api, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_google_maps_place_reviews(self, client: Structify) -> None:
        search_api = client.external.search_api.google_maps_place_reviews(
            place_id="place_id",
        )
        assert_matches_type(SearchAPIGoogleMapsPlaceReviewsResponse, search_api, path=["response"])

    @parametrize
    def test_method_google_maps_place_reviews_with_all_params(self, client: Structify) -> None:
        search_api = client.external.search_api.google_maps_place_reviews(
            place_id="place_id",
            hl="hl",
            num=0,
        )
        assert_matches_type(SearchAPIGoogleMapsPlaceReviewsResponse, search_api, path=["response"])

    @parametrize
    def test_raw_response_google_maps_place_reviews(self, client: Structify) -> None:
        response = client.external.search_api.with_raw_response.google_maps_place_reviews(
            place_id="place_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        search_api = response.parse()
        assert_matches_type(SearchAPIGoogleMapsPlaceReviewsResponse, search_api, path=["response"])

    @parametrize
    def test_streaming_response_google_maps_place_reviews(self, client: Structify) -> None:
        with client.external.search_api.with_streaming_response.google_maps_place_reviews(
            place_id="place_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            search_api = response.parse()
            assert_matches_type(SearchAPIGoogleMapsPlaceReviewsResponse, search_api, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_google_maps_search(self, client: Structify) -> None:
        search_api = client.external.search_api.google_maps_search(
            q="q",
        )
        assert_matches_type(SearchAPIGoogleMapsSearchResponse, search_api, path=["response"])

    @parametrize
    def test_method_google_maps_search_with_all_params(self, client: Structify) -> None:
        search_api = client.external.search_api.google_maps_search(
            q="q",
            gl="gl",
            hl="hl",
            num=0,
        )
        assert_matches_type(SearchAPIGoogleMapsSearchResponse, search_api, path=["response"])

    @parametrize
    def test_raw_response_google_maps_search(self, client: Structify) -> None:
        response = client.external.search_api.with_raw_response.google_maps_search(
            q="q",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        search_api = response.parse()
        assert_matches_type(SearchAPIGoogleMapsSearchResponse, search_api, path=["response"])

    @parametrize
    def test_streaming_response_google_maps_search(self, client: Structify) -> None:
        with client.external.search_api.with_streaming_response.google_maps_search(
            q="q",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            search_api = response.parse()
            assert_matches_type(SearchAPIGoogleMapsSearchResponse, search_api, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_google_scholar_author_search(self, client: Structify) -> None:
        search_api = client.external.search_api.google_scholar_author_search(
            author="author",
        )
        assert_matches_type(SearchAPIGoogleScholarAuthorSearchResponse, search_api, path=["response"])

    @parametrize
    def test_method_google_scholar_author_search_with_all_params(self, client: Structify) -> None:
        search_api = client.external.search_api.google_scholar_author_search(
            author="author",
            hl="hl",
            num=0,
            start=0,
        )
        assert_matches_type(SearchAPIGoogleScholarAuthorSearchResponse, search_api, path=["response"])

    @parametrize
    def test_raw_response_google_scholar_author_search(self, client: Structify) -> None:
        response = client.external.search_api.with_raw_response.google_scholar_author_search(
            author="author",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        search_api = response.parse()
        assert_matches_type(SearchAPIGoogleScholarAuthorSearchResponse, search_api, path=["response"])

    @parametrize
    def test_streaming_response_google_scholar_author_search(self, client: Structify) -> None:
        with client.external.search_api.with_streaming_response.google_scholar_author_search(
            author="author",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            search_api = response.parse()
            assert_matches_type(SearchAPIGoogleScholarAuthorSearchResponse, search_api, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_google_scholar_citations(self, client: Structify) -> None:
        search_api = client.external.search_api.google_scholar_citations(
            q="q",
        )
        assert_matches_type(SearchAPIGoogleScholarCitationsResponse, search_api, path=["response"])

    @parametrize
    def test_method_google_scholar_citations_with_all_params(self, client: Structify) -> None:
        search_api = client.external.search_api.google_scholar_citations(
            q="q",
            hl="hl",
            num=0,
            start=0,
        )
        assert_matches_type(SearchAPIGoogleScholarCitationsResponse, search_api, path=["response"])

    @parametrize
    def test_raw_response_google_scholar_citations(self, client: Structify) -> None:
        response = client.external.search_api.with_raw_response.google_scholar_citations(
            q="q",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        search_api = response.parse()
        assert_matches_type(SearchAPIGoogleScholarCitationsResponse, search_api, path=["response"])

    @parametrize
    def test_streaming_response_google_scholar_citations(self, client: Structify) -> None:
        with client.external.search_api.with_streaming_response.google_scholar_citations(
            q="q",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            search_api = response.parse()
            assert_matches_type(SearchAPIGoogleScholarCitationsResponse, search_api, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_google_scholar_search(self, client: Structify) -> None:
        search_api = client.external.search_api.google_scholar_search(
            q="q",
        )
        assert_matches_type(SearchAPIGoogleScholarSearchResponse, search_api, path=["response"])

    @parametrize
    def test_method_google_scholar_search_with_all_params(self, client: Structify) -> None:
        search_api = client.external.search_api.google_scholar_search(
            q="q",
            as_yhi=0,
            as_ylo=0,
            hl="hl",
            num=0,
            start=0,
        )
        assert_matches_type(SearchAPIGoogleScholarSearchResponse, search_api, path=["response"])

    @parametrize
    def test_raw_response_google_scholar_search(self, client: Structify) -> None:
        response = client.external.search_api.with_raw_response.google_scholar_search(
            q="q",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        search_api = response.parse()
        assert_matches_type(SearchAPIGoogleScholarSearchResponse, search_api, path=["response"])

    @parametrize
    def test_streaming_response_google_scholar_search(self, client: Structify) -> None:
        with client.external.search_api.with_streaming_response.google_scholar_search(
            q="q",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            search_api = response.parse()
            assert_matches_type(SearchAPIGoogleScholarSearchResponse, search_api, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_google_search(self, client: Structify) -> None:
        search_api = client.external.search_api.google_search(
            q="q",
        )
        assert_matches_type(GoogleSearchResponse, search_api, path=["response"])

    @parametrize
    def test_method_google_search_with_all_params(self, client: Structify) -> None:
        search_api = client.external.search_api.google_search(
            q="q",
            gl="gl",
            hl="hl",
            num=0,
            start=0,
        )
        assert_matches_type(GoogleSearchResponse, search_api, path=["response"])

    @parametrize
    def test_raw_response_google_search(self, client: Structify) -> None:
        response = client.external.search_api.with_raw_response.google_search(
            q="q",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        search_api = response.parse()
        assert_matches_type(GoogleSearchResponse, search_api, path=["response"])

    @parametrize
    def test_streaming_response_google_search(self, client: Structify) -> None:
        with client.external.search_api.with_streaming_response.google_search(
            q="q",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            search_api = response.parse()
            assert_matches_type(GoogleSearchResponse, search_api, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_location_search(self, client: Structify) -> None:
        search_api = client.external.search_api.location_search(
            q="q",
        )
        assert_matches_type(LocationResponse, search_api, path=["response"])

    @parametrize
    def test_method_location_search_with_all_params(self, client: Structify) -> None:
        search_api = client.external.search_api.location_search(
            q="q",
            gl="gl",
            hl="hl",
            num=0,
        )
        assert_matches_type(LocationResponse, search_api, path=["response"])

    @parametrize
    def test_raw_response_location_search(self, client: Structify) -> None:
        response = client.external.search_api.with_raw_response.location_search(
            q="q",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        search_api = response.parse()
        assert_matches_type(LocationResponse, search_api, path=["response"])

    @parametrize
    def test_streaming_response_location_search(self, client: Structify) -> None:
        with client.external.search_api.with_streaming_response.location_search(
            q="q",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            search_api = response.parse()
            assert_matches_type(LocationResponse, search_api, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncSearchAPI:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_google_flights_calendar(self, async_client: AsyncStructify) -> None:
        search_api = await async_client.external.search_api.google_flights_calendar(
            arrival_id="arrival_id",
            departure_id="departure_id",
            outbound_date="outbound_date",
        )
        assert_matches_type(SearchAPIGoogleFlightsCalendarResponse, search_api, path=["response"])

    @parametrize
    async def test_method_google_flights_calendar_with_all_params(self, async_client: AsyncStructify) -> None:
        search_api = await async_client.external.search_api.google_flights_calendar(
            arrival_id="arrival_id",
            departure_id="departure_id",
            outbound_date="outbound_date",
            currency="currency",
            hl="hl",
            return_date="return_date",
        )
        assert_matches_type(SearchAPIGoogleFlightsCalendarResponse, search_api, path=["response"])

    @parametrize
    async def test_raw_response_google_flights_calendar(self, async_client: AsyncStructify) -> None:
        response = await async_client.external.search_api.with_raw_response.google_flights_calendar(
            arrival_id="arrival_id",
            departure_id="departure_id",
            outbound_date="outbound_date",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        search_api = await response.parse()
        assert_matches_type(SearchAPIGoogleFlightsCalendarResponse, search_api, path=["response"])

    @parametrize
    async def test_streaming_response_google_flights_calendar(self, async_client: AsyncStructify) -> None:
        async with async_client.external.search_api.with_streaming_response.google_flights_calendar(
            arrival_id="arrival_id",
            departure_id="departure_id",
            outbound_date="outbound_date",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            search_api = await response.parse()
            assert_matches_type(SearchAPIGoogleFlightsCalendarResponse, search_api, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_google_flights_location_search(self, async_client: AsyncStructify) -> None:
        search_api = await async_client.external.search_api.google_flights_location_search(
            q="q",
        )
        assert_matches_type(SearchAPIGoogleFlightsLocationSearchResponse, search_api, path=["response"])

    @parametrize
    async def test_method_google_flights_location_search_with_all_params(self, async_client: AsyncStructify) -> None:
        search_api = await async_client.external.search_api.google_flights_location_search(
            q="q",
            hl="hl",
        )
        assert_matches_type(SearchAPIGoogleFlightsLocationSearchResponse, search_api, path=["response"])

    @parametrize
    async def test_raw_response_google_flights_location_search(self, async_client: AsyncStructify) -> None:
        response = await async_client.external.search_api.with_raw_response.google_flights_location_search(
            q="q",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        search_api = await response.parse()
        assert_matches_type(SearchAPIGoogleFlightsLocationSearchResponse, search_api, path=["response"])

    @parametrize
    async def test_streaming_response_google_flights_location_search(self, async_client: AsyncStructify) -> None:
        async with async_client.external.search_api.with_streaming_response.google_flights_location_search(
            q="q",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            search_api = await response.parse()
            assert_matches_type(SearchAPIGoogleFlightsLocationSearchResponse, search_api, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_google_flights_search(self, async_client: AsyncStructify) -> None:
        search_api = await async_client.external.search_api.google_flights_search(
            arrival_id="arrival_id",
            departure_id="departure_id",
            outbound_date="outbound_date",
        )
        assert_matches_type(SearchAPIGoogleFlightsSearchResponse, search_api, path=["response"])

    @parametrize
    async def test_method_google_flights_search_with_all_params(self, async_client: AsyncStructify) -> None:
        search_api = await async_client.external.search_api.google_flights_search(
            arrival_id="arrival_id",
            departure_id="departure_id",
            outbound_date="outbound_date",
            adults=0,
            children=0,
            currency="currency",
            hl="hl",
            infants_in_seat=0,
            infants_on_lap=0,
            return_date="return_date",
            travel_class="travel_class",
        )
        assert_matches_type(SearchAPIGoogleFlightsSearchResponse, search_api, path=["response"])

    @parametrize
    async def test_raw_response_google_flights_search(self, async_client: AsyncStructify) -> None:
        response = await async_client.external.search_api.with_raw_response.google_flights_search(
            arrival_id="arrival_id",
            departure_id="departure_id",
            outbound_date="outbound_date",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        search_api = await response.parse()
        assert_matches_type(SearchAPIGoogleFlightsSearchResponse, search_api, path=["response"])

    @parametrize
    async def test_streaming_response_google_flights_search(self, async_client: AsyncStructify) -> None:
        async with async_client.external.search_api.with_streaming_response.google_flights_search(
            arrival_id="arrival_id",
            departure_id="departure_id",
            outbound_date="outbound_date",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            search_api = await response.parse()
            assert_matches_type(SearchAPIGoogleFlightsSearchResponse, search_api, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_google_maps_place_details(self, async_client: AsyncStructify) -> None:
        search_api = await async_client.external.search_api.google_maps_place_details(
            place_id="place_id",
        )
        assert_matches_type(SearchAPIGoogleMapsPlaceDetailsResponse, search_api, path=["response"])

    @parametrize
    async def test_method_google_maps_place_details_with_all_params(self, async_client: AsyncStructify) -> None:
        search_api = await async_client.external.search_api.google_maps_place_details(
            place_id="place_id",
            hl="hl",
        )
        assert_matches_type(SearchAPIGoogleMapsPlaceDetailsResponse, search_api, path=["response"])

    @parametrize
    async def test_raw_response_google_maps_place_details(self, async_client: AsyncStructify) -> None:
        response = await async_client.external.search_api.with_raw_response.google_maps_place_details(
            place_id="place_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        search_api = await response.parse()
        assert_matches_type(SearchAPIGoogleMapsPlaceDetailsResponse, search_api, path=["response"])

    @parametrize
    async def test_streaming_response_google_maps_place_details(self, async_client: AsyncStructify) -> None:
        async with async_client.external.search_api.with_streaming_response.google_maps_place_details(
            place_id="place_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            search_api = await response.parse()
            assert_matches_type(SearchAPIGoogleMapsPlaceDetailsResponse, search_api, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_google_maps_place_photos(self, async_client: AsyncStructify) -> None:
        search_api = await async_client.external.search_api.google_maps_place_photos(
            place_id="place_id",
        )
        assert_matches_type(SearchAPIGoogleMapsPlacePhotosResponse, search_api, path=["response"])

    @parametrize
    async def test_method_google_maps_place_photos_with_all_params(self, async_client: AsyncStructify) -> None:
        search_api = await async_client.external.search_api.google_maps_place_photos(
            place_id="place_id",
            num=0,
        )
        assert_matches_type(SearchAPIGoogleMapsPlacePhotosResponse, search_api, path=["response"])

    @parametrize
    async def test_raw_response_google_maps_place_photos(self, async_client: AsyncStructify) -> None:
        response = await async_client.external.search_api.with_raw_response.google_maps_place_photos(
            place_id="place_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        search_api = await response.parse()
        assert_matches_type(SearchAPIGoogleMapsPlacePhotosResponse, search_api, path=["response"])

    @parametrize
    async def test_streaming_response_google_maps_place_photos(self, async_client: AsyncStructify) -> None:
        async with async_client.external.search_api.with_streaming_response.google_maps_place_photos(
            place_id="place_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            search_api = await response.parse()
            assert_matches_type(SearchAPIGoogleMapsPlacePhotosResponse, search_api, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_google_maps_place_reviews(self, async_client: AsyncStructify) -> None:
        search_api = await async_client.external.search_api.google_maps_place_reviews(
            place_id="place_id",
        )
        assert_matches_type(SearchAPIGoogleMapsPlaceReviewsResponse, search_api, path=["response"])

    @parametrize
    async def test_method_google_maps_place_reviews_with_all_params(self, async_client: AsyncStructify) -> None:
        search_api = await async_client.external.search_api.google_maps_place_reviews(
            place_id="place_id",
            hl="hl",
            num=0,
        )
        assert_matches_type(SearchAPIGoogleMapsPlaceReviewsResponse, search_api, path=["response"])

    @parametrize
    async def test_raw_response_google_maps_place_reviews(self, async_client: AsyncStructify) -> None:
        response = await async_client.external.search_api.with_raw_response.google_maps_place_reviews(
            place_id="place_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        search_api = await response.parse()
        assert_matches_type(SearchAPIGoogleMapsPlaceReviewsResponse, search_api, path=["response"])

    @parametrize
    async def test_streaming_response_google_maps_place_reviews(self, async_client: AsyncStructify) -> None:
        async with async_client.external.search_api.with_streaming_response.google_maps_place_reviews(
            place_id="place_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            search_api = await response.parse()
            assert_matches_type(SearchAPIGoogleMapsPlaceReviewsResponse, search_api, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_google_maps_search(self, async_client: AsyncStructify) -> None:
        search_api = await async_client.external.search_api.google_maps_search(
            q="q",
        )
        assert_matches_type(SearchAPIGoogleMapsSearchResponse, search_api, path=["response"])

    @parametrize
    async def test_method_google_maps_search_with_all_params(self, async_client: AsyncStructify) -> None:
        search_api = await async_client.external.search_api.google_maps_search(
            q="q",
            gl="gl",
            hl="hl",
            num=0,
        )
        assert_matches_type(SearchAPIGoogleMapsSearchResponse, search_api, path=["response"])

    @parametrize
    async def test_raw_response_google_maps_search(self, async_client: AsyncStructify) -> None:
        response = await async_client.external.search_api.with_raw_response.google_maps_search(
            q="q",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        search_api = await response.parse()
        assert_matches_type(SearchAPIGoogleMapsSearchResponse, search_api, path=["response"])

    @parametrize
    async def test_streaming_response_google_maps_search(self, async_client: AsyncStructify) -> None:
        async with async_client.external.search_api.with_streaming_response.google_maps_search(
            q="q",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            search_api = await response.parse()
            assert_matches_type(SearchAPIGoogleMapsSearchResponse, search_api, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_google_scholar_author_search(self, async_client: AsyncStructify) -> None:
        search_api = await async_client.external.search_api.google_scholar_author_search(
            author="author",
        )
        assert_matches_type(SearchAPIGoogleScholarAuthorSearchResponse, search_api, path=["response"])

    @parametrize
    async def test_method_google_scholar_author_search_with_all_params(self, async_client: AsyncStructify) -> None:
        search_api = await async_client.external.search_api.google_scholar_author_search(
            author="author",
            hl="hl",
            num=0,
            start=0,
        )
        assert_matches_type(SearchAPIGoogleScholarAuthorSearchResponse, search_api, path=["response"])

    @parametrize
    async def test_raw_response_google_scholar_author_search(self, async_client: AsyncStructify) -> None:
        response = await async_client.external.search_api.with_raw_response.google_scholar_author_search(
            author="author",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        search_api = await response.parse()
        assert_matches_type(SearchAPIGoogleScholarAuthorSearchResponse, search_api, path=["response"])

    @parametrize
    async def test_streaming_response_google_scholar_author_search(self, async_client: AsyncStructify) -> None:
        async with async_client.external.search_api.with_streaming_response.google_scholar_author_search(
            author="author",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            search_api = await response.parse()
            assert_matches_type(SearchAPIGoogleScholarAuthorSearchResponse, search_api, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_google_scholar_citations(self, async_client: AsyncStructify) -> None:
        search_api = await async_client.external.search_api.google_scholar_citations(
            q="q",
        )
        assert_matches_type(SearchAPIGoogleScholarCitationsResponse, search_api, path=["response"])

    @parametrize
    async def test_method_google_scholar_citations_with_all_params(self, async_client: AsyncStructify) -> None:
        search_api = await async_client.external.search_api.google_scholar_citations(
            q="q",
            hl="hl",
            num=0,
            start=0,
        )
        assert_matches_type(SearchAPIGoogleScholarCitationsResponse, search_api, path=["response"])

    @parametrize
    async def test_raw_response_google_scholar_citations(self, async_client: AsyncStructify) -> None:
        response = await async_client.external.search_api.with_raw_response.google_scholar_citations(
            q="q",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        search_api = await response.parse()
        assert_matches_type(SearchAPIGoogleScholarCitationsResponse, search_api, path=["response"])

    @parametrize
    async def test_streaming_response_google_scholar_citations(self, async_client: AsyncStructify) -> None:
        async with async_client.external.search_api.with_streaming_response.google_scholar_citations(
            q="q",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            search_api = await response.parse()
            assert_matches_type(SearchAPIGoogleScholarCitationsResponse, search_api, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_google_scholar_search(self, async_client: AsyncStructify) -> None:
        search_api = await async_client.external.search_api.google_scholar_search(
            q="q",
        )
        assert_matches_type(SearchAPIGoogleScholarSearchResponse, search_api, path=["response"])

    @parametrize
    async def test_method_google_scholar_search_with_all_params(self, async_client: AsyncStructify) -> None:
        search_api = await async_client.external.search_api.google_scholar_search(
            q="q",
            as_yhi=0,
            as_ylo=0,
            hl="hl",
            num=0,
            start=0,
        )
        assert_matches_type(SearchAPIGoogleScholarSearchResponse, search_api, path=["response"])

    @parametrize
    async def test_raw_response_google_scholar_search(self, async_client: AsyncStructify) -> None:
        response = await async_client.external.search_api.with_raw_response.google_scholar_search(
            q="q",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        search_api = await response.parse()
        assert_matches_type(SearchAPIGoogleScholarSearchResponse, search_api, path=["response"])

    @parametrize
    async def test_streaming_response_google_scholar_search(self, async_client: AsyncStructify) -> None:
        async with async_client.external.search_api.with_streaming_response.google_scholar_search(
            q="q",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            search_api = await response.parse()
            assert_matches_type(SearchAPIGoogleScholarSearchResponse, search_api, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_google_search(self, async_client: AsyncStructify) -> None:
        search_api = await async_client.external.search_api.google_search(
            q="q",
        )
        assert_matches_type(GoogleSearchResponse, search_api, path=["response"])

    @parametrize
    async def test_method_google_search_with_all_params(self, async_client: AsyncStructify) -> None:
        search_api = await async_client.external.search_api.google_search(
            q="q",
            gl="gl",
            hl="hl",
            num=0,
            start=0,
        )
        assert_matches_type(GoogleSearchResponse, search_api, path=["response"])

    @parametrize
    async def test_raw_response_google_search(self, async_client: AsyncStructify) -> None:
        response = await async_client.external.search_api.with_raw_response.google_search(
            q="q",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        search_api = await response.parse()
        assert_matches_type(GoogleSearchResponse, search_api, path=["response"])

    @parametrize
    async def test_streaming_response_google_search(self, async_client: AsyncStructify) -> None:
        async with async_client.external.search_api.with_streaming_response.google_search(
            q="q",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            search_api = await response.parse()
            assert_matches_type(GoogleSearchResponse, search_api, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_location_search(self, async_client: AsyncStructify) -> None:
        search_api = await async_client.external.search_api.location_search(
            q="q",
        )
        assert_matches_type(LocationResponse, search_api, path=["response"])

    @parametrize
    async def test_method_location_search_with_all_params(self, async_client: AsyncStructify) -> None:
        search_api = await async_client.external.search_api.location_search(
            q="q",
            gl="gl",
            hl="hl",
            num=0,
        )
        assert_matches_type(LocationResponse, search_api, path=["response"])

    @parametrize
    async def test_raw_response_location_search(self, async_client: AsyncStructify) -> None:
        response = await async_client.external.search_api.with_raw_response.location_search(
            q="q",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        search_api = await response.parse()
        assert_matches_type(LocationResponse, search_api, path=["response"])

    @parametrize
    async def test_streaming_response_location_search(self, async_client: AsyncStructify) -> None:
        async with async_client.external.search_api.with_streaming_response.location_search(
            q="q",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            search_api = await response.parse()
            assert_matches_type(LocationResponse, search_api, path=["response"])

        assert cast(Any, response.is_closed) is True
