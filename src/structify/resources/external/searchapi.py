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
from ...types.external import (
    searchapi_google_search_params,
    searchapi_location_search_params,
    searchapi_google_maps_search_params,
    searchapi_google_flights_search_params,
    searchapi_google_scholar_search_params,
    searchapi_google_flights_calendar_params,
    searchapi_google_maps_place_photos_params,
    searchapi_google_scholar_citations_params,
    searchapi_google_maps_place_details_params,
    searchapi_google_maps_place_reviews_params,
    searchapi_google_scholar_author_search_params,
    searchapi_google_flights_location_search_params,
)
from ...types.external.location_response import LocationResponse
from ...types.external.google_search_response import GoogleSearchResponse
from ...types.external.searchapi_google_maps_search_response import SearchapiGoogleMapsSearchResponse
from ...types.external.searchapi_google_flights_search_response import SearchapiGoogleFlightsSearchResponse
from ...types.external.searchapi_google_scholar_search_response import SearchapiGoogleScholarSearchResponse
from ...types.external.searchapi_google_flights_calendar_response import SearchapiGoogleFlightsCalendarResponse
from ...types.external.searchapi_google_maps_place_photos_response import SearchapiGoogleMapsPlacePhotosResponse
from ...types.external.searchapi_google_scholar_citations_response import SearchapiGoogleScholarCitationsResponse
from ...types.external.searchapi_google_maps_place_details_response import SearchapiGoogleMapsPlaceDetailsResponse
from ...types.external.searchapi_google_maps_place_reviews_response import SearchapiGoogleMapsPlaceReviewsResponse
from ...types.external.searchapi_google_scholar_author_search_response import SearchapiGoogleScholarAuthorSearchResponse
from ...types.external.searchapi_google_flights_location_search_response import (
    SearchapiGoogleFlightsLocationSearchResponse,
)

__all__ = ["SearchapiResource", "AsyncSearchapiResource"]


class SearchapiResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SearchapiResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/StructifyAI/structify-python#accessing-raw-response-data-eg-headers
        """
        return SearchapiResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SearchapiResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/StructifyAI/structify-python#with_streaming_response
        """
        return SearchapiResourceWithStreamingResponse(self)

    def google_flights_calendar(
        self,
        *,
        arrival_id: str,
        departure_id: str,
        outbound_date: str,
        currency: Optional[str] | Omit = omit,
        hl: Optional[str] | Omit = omit,
        return_date: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SearchapiGoogleFlightsCalendarResponse:
        """
        Get flight prices across different dates (calendar view)

        Args:
          arrival_id: Arrival airport code

          departure_id: Departure airport code

          outbound_date: Outbound date (YYYY-MM-DD format)

          currency: Currency (optional, e.g. "USD")

          hl: Language (optional, e.g. "en")

          return_date: Return date (YYYY-MM-DD format, optional)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/external/searchapi/flights/calendar",
            body=maybe_transform(
                {
                    "arrival_id": arrival_id,
                    "departure_id": departure_id,
                    "outbound_date": outbound_date,
                    "currency": currency,
                    "hl": hl,
                    "return_date": return_date,
                },
                searchapi_google_flights_calendar_params.SearchapiGoogleFlightsCalendarParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SearchapiGoogleFlightsCalendarResponse,
        )

    def google_flights_location_search(
        self,
        *,
        q: str,
        hl: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SearchapiGoogleFlightsLocationSearchResponse:
        """
        Search for airports and locations for flight booking

        Args:
          q: Search query for airport/location

          hl: Language (optional, e.g. "en")

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/external/searchapi/flights/location_search",
            body=maybe_transform(
                {
                    "q": q,
                    "hl": hl,
                },
                searchapi_google_flights_location_search_params.SearchapiGoogleFlightsLocationSearchParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SearchapiGoogleFlightsLocationSearchResponse,
        )

    def google_flights_search(
        self,
        *,
        arrival_id: str,
        departure_id: str,
        outbound_date: str,
        adults: Optional[int] | Omit = omit,
        children: Optional[int] | Omit = omit,
        currency: Optional[str] | Omit = omit,
        hl: Optional[str] | Omit = omit,
        infants_in_seat: Optional[int] | Omit = omit,
        infants_on_lap: Optional[int] | Omit = omit,
        return_date: Optional[str] | Omit = omit,
        travel_class: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SearchapiGoogleFlightsSearchResponse:
        """
        Search for flight options between airports

        Args:
          arrival_id: Arrival airport code (e.g., "JFK", "LAX")

          departure_id: Departure airport code (e.g., "JFK", "LAX")

          outbound_date: Outbound date (YYYY-MM-DD format)

          adults: Number of adults (optional, default 1)

          children: Number of children (optional, default 0)

          currency: Currency (optional, e.g. "USD")

          hl: Language (optional, e.g. "en")

          infants_in_seat: Number of infants on lap (optional, default 0)

          infants_on_lap: Number of infants in seat (optional, default 0)

          return_date: Return date (YYYY-MM-DD format, optional for one-way)

          travel_class: Travel class (optional: "economy", "premium_economy", "business", "first")

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/external/searchapi/flights/search",
            body=maybe_transform(
                {
                    "arrival_id": arrival_id,
                    "departure_id": departure_id,
                    "outbound_date": outbound_date,
                    "adults": adults,
                    "children": children,
                    "currency": currency,
                    "hl": hl,
                    "infants_in_seat": infants_in_seat,
                    "infants_on_lap": infants_on_lap,
                    "return_date": return_date,
                    "travel_class": travel_class,
                },
                searchapi_google_flights_search_params.SearchapiGoogleFlightsSearchParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SearchapiGoogleFlightsSearchResponse,
        )

    def google_maps_place_details(
        self,
        *,
        place_id: str,
        hl: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SearchapiGoogleMapsPlaceDetailsResponse:
        """
        Get detailed information about a specific place

        Args:
          place_id: Place ID from Google Maps

          hl: Language (optional, e.g. "en", "es")

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/external/searchapi/maps/place",
            body=maybe_transform(
                {
                    "place_id": place_id,
                    "hl": hl,
                },
                searchapi_google_maps_place_details_params.SearchapiGoogleMapsPlaceDetailsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SearchapiGoogleMapsPlaceDetailsResponse,
        )

    def google_maps_place_photos(
        self,
        *,
        place_id: str,
        num: Optional[int] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SearchapiGoogleMapsPlacePhotosResponse:
        """
        Get photos for a specific place

        Args:
          place_id: Place ID from Google Maps

          num: Number of photos to return (optional)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/external/searchapi/maps/photos",
            body=maybe_transform(
                {
                    "place_id": place_id,
                    "num": num,
                },
                searchapi_google_maps_place_photos_params.SearchapiGoogleMapsPlacePhotosParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SearchapiGoogleMapsPlacePhotosResponse,
        )

    def google_maps_place_reviews(
        self,
        *,
        place_id: str,
        hl: Optional[str] | Omit = omit,
        num: Optional[int] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SearchapiGoogleMapsPlaceReviewsResponse:
        """
        Get reviews for a specific place

        Args:
          place_id: Place ID from Google Maps

          hl: Language (optional, e.g. "en", "es")

          num: Number of reviews to return (optional)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/external/searchapi/maps/reviews",
            body=maybe_transform(
                {
                    "place_id": place_id,
                    "hl": hl,
                    "num": num,
                },
                searchapi_google_maps_place_reviews_params.SearchapiGoogleMapsPlaceReviewsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SearchapiGoogleMapsPlaceReviewsResponse,
        )

    def google_maps_search(
        self,
        *,
        q: str,
        gl: Optional[str] | Omit = omit,
        hl: Optional[str] | Omit = omit,
        num: Optional[int] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SearchapiGoogleMapsSearchResponse:
        """
        Search for places on Google Maps

        Args:
          q: The search query (e.g., "restaurants near me")

          gl: Geographic location (optional, e.g. "us", "uk")

          hl: Language (optional, e.g. "en", "es")

          num: Number of results to return (optional)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/external/searchapi/maps/search",
            body=maybe_transform(
                {
                    "q": q,
                    "gl": gl,
                    "hl": hl,
                    "num": num,
                },
                searchapi_google_maps_search_params.SearchapiGoogleMapsSearchParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SearchapiGoogleMapsSearchResponse,
        )

    def google_scholar_author_search(
        self,
        *,
        author: str,
        hl: Optional[str] | Omit = omit,
        num: Optional[int] | Omit = omit,
        start: Optional[int] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SearchapiGoogleScholarAuthorSearchResponse:
        """
        Search for academic authors and their publications

        Args:
          author: Author name to search for

          hl: Language (optional, e.g. "en")

          num: Number of results to return (optional)

          start: Starting result index (optional)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/external/searchapi/scholar/author",
            body=maybe_transform(
                {
                    "author": author,
                    "hl": hl,
                    "num": num,
                    "start": start,
                },
                searchapi_google_scholar_author_search_params.SearchapiGoogleScholarAuthorSearchParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SearchapiGoogleScholarAuthorSearchResponse,
        )

    def google_scholar_citations(
        self,
        *,
        q: str,
        hl: Optional[str] | Omit = omit,
        num: Optional[int] | Omit = omit,
        start: Optional[int] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SearchapiGoogleScholarCitationsResponse:
        """
        Get citations for a specific academic publication

        Args:
          q: The publication ID to get citations for

          hl: Language (optional, e.g. "en")

          num: Number of citations to return (optional)

          start: Starting result index (optional)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/external/searchapi/scholar/cite",
            body=maybe_transform(
                {
                    "q": q,
                    "hl": hl,
                    "num": num,
                    "start": start,
                },
                searchapi_google_scholar_citations_params.SearchapiGoogleScholarCitationsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SearchapiGoogleScholarCitationsResponse,
        )

    def google_scholar_search(
        self,
        *,
        q: str,
        as_yhi: Optional[int] | Omit = omit,
        as_ylo: Optional[int] | Omit = omit,
        hl: Optional[str] | Omit = omit,
        num: Optional[int] | Omit = omit,
        start: Optional[int] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SearchapiGoogleScholarSearchResponse:
        """
        Search academic papers and publications on Google Scholar

        Args:
          q: The search query

          as_yhi: Year range end (optional, e.g. 2023)

          as_ylo: Year range start (optional, e.g. 2020)

          hl: Language (optional, e.g. "en")

          num: Number of results to return (optional)

          start: Starting result index (optional)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/external/searchapi/scholar/search",
            body=maybe_transform(
                {
                    "q": q,
                    "as_yhi": as_yhi,
                    "as_ylo": as_ylo,
                    "hl": hl,
                    "num": num,
                    "start": start,
                },
                searchapi_google_scholar_search_params.SearchapiGoogleScholarSearchParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SearchapiGoogleScholarSearchResponse,
        )

    def google_search(
        self,
        *,
        q: str,
        gl: Optional[str] | Omit = omit,
        hl: Optional[str] | Omit = omit,
        num: Optional[int] | Omit = omit,
        start: Optional[int] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> GoogleSearchResponse:
        """
        Performs a Google web search using the SearchAPI service

        Args:
          q: The search query

          gl: Geographic location (optional, e.g. "us", "uk")

          hl: Language (optional, e.g. "en", "es")

          num: Number of results to return (optional, max 100)

          start: Starting result index (optional)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/external/searchapi/search",
            body=maybe_transform(
                {
                    "q": q,
                    "gl": gl,
                    "hl": hl,
                    "num": num,
                    "start": start,
                },
                searchapi_google_search_params.SearchapiGoogleSearchParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GoogleSearchResponse,
        )

    def location_search(
        self,
        *,
        q: str,
        gl: Optional[str] | Omit = omit,
        hl: Optional[str] | Omit = omit,
        num: Optional[int] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LocationResponse:
        """
        Search for geographic locations, addresses, and places

        Args:
          q: The location query to search for

          gl: Geographic location bias (optional, e.g. "us", "uk")

          hl: Language (optional, e.g. "en")

          num: Number of results to return (optional)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/external/searchapi/locations",
            body=maybe_transform(
                {
                    "q": q,
                    "gl": gl,
                    "hl": hl,
                    "num": num,
                },
                searchapi_location_search_params.SearchapiLocationSearchParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LocationResponse,
        )


class AsyncSearchapiResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSearchapiResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/StructifyAI/structify-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSearchapiResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSearchapiResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/StructifyAI/structify-python#with_streaming_response
        """
        return AsyncSearchapiResourceWithStreamingResponse(self)

    async def google_flights_calendar(
        self,
        *,
        arrival_id: str,
        departure_id: str,
        outbound_date: str,
        currency: Optional[str] | Omit = omit,
        hl: Optional[str] | Omit = omit,
        return_date: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SearchapiGoogleFlightsCalendarResponse:
        """
        Get flight prices across different dates (calendar view)

        Args:
          arrival_id: Arrival airport code

          departure_id: Departure airport code

          outbound_date: Outbound date (YYYY-MM-DD format)

          currency: Currency (optional, e.g. "USD")

          hl: Language (optional, e.g. "en")

          return_date: Return date (YYYY-MM-DD format, optional)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/external/searchapi/flights/calendar",
            body=await async_maybe_transform(
                {
                    "arrival_id": arrival_id,
                    "departure_id": departure_id,
                    "outbound_date": outbound_date,
                    "currency": currency,
                    "hl": hl,
                    "return_date": return_date,
                },
                searchapi_google_flights_calendar_params.SearchapiGoogleFlightsCalendarParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SearchapiGoogleFlightsCalendarResponse,
        )

    async def google_flights_location_search(
        self,
        *,
        q: str,
        hl: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SearchapiGoogleFlightsLocationSearchResponse:
        """
        Search for airports and locations for flight booking

        Args:
          q: Search query for airport/location

          hl: Language (optional, e.g. "en")

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/external/searchapi/flights/location_search",
            body=await async_maybe_transform(
                {
                    "q": q,
                    "hl": hl,
                },
                searchapi_google_flights_location_search_params.SearchapiGoogleFlightsLocationSearchParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SearchapiGoogleFlightsLocationSearchResponse,
        )

    async def google_flights_search(
        self,
        *,
        arrival_id: str,
        departure_id: str,
        outbound_date: str,
        adults: Optional[int] | Omit = omit,
        children: Optional[int] | Omit = omit,
        currency: Optional[str] | Omit = omit,
        hl: Optional[str] | Omit = omit,
        infants_in_seat: Optional[int] | Omit = omit,
        infants_on_lap: Optional[int] | Omit = omit,
        return_date: Optional[str] | Omit = omit,
        travel_class: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SearchapiGoogleFlightsSearchResponse:
        """
        Search for flight options between airports

        Args:
          arrival_id: Arrival airport code (e.g., "JFK", "LAX")

          departure_id: Departure airport code (e.g., "JFK", "LAX")

          outbound_date: Outbound date (YYYY-MM-DD format)

          adults: Number of adults (optional, default 1)

          children: Number of children (optional, default 0)

          currency: Currency (optional, e.g. "USD")

          hl: Language (optional, e.g. "en")

          infants_in_seat: Number of infants on lap (optional, default 0)

          infants_on_lap: Number of infants in seat (optional, default 0)

          return_date: Return date (YYYY-MM-DD format, optional for one-way)

          travel_class: Travel class (optional: "economy", "premium_economy", "business", "first")

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/external/searchapi/flights/search",
            body=await async_maybe_transform(
                {
                    "arrival_id": arrival_id,
                    "departure_id": departure_id,
                    "outbound_date": outbound_date,
                    "adults": adults,
                    "children": children,
                    "currency": currency,
                    "hl": hl,
                    "infants_in_seat": infants_in_seat,
                    "infants_on_lap": infants_on_lap,
                    "return_date": return_date,
                    "travel_class": travel_class,
                },
                searchapi_google_flights_search_params.SearchapiGoogleFlightsSearchParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SearchapiGoogleFlightsSearchResponse,
        )

    async def google_maps_place_details(
        self,
        *,
        place_id: str,
        hl: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SearchapiGoogleMapsPlaceDetailsResponse:
        """
        Get detailed information about a specific place

        Args:
          place_id: Place ID from Google Maps

          hl: Language (optional, e.g. "en", "es")

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/external/searchapi/maps/place",
            body=await async_maybe_transform(
                {
                    "place_id": place_id,
                    "hl": hl,
                },
                searchapi_google_maps_place_details_params.SearchapiGoogleMapsPlaceDetailsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SearchapiGoogleMapsPlaceDetailsResponse,
        )

    async def google_maps_place_photos(
        self,
        *,
        place_id: str,
        num: Optional[int] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SearchapiGoogleMapsPlacePhotosResponse:
        """
        Get photos for a specific place

        Args:
          place_id: Place ID from Google Maps

          num: Number of photos to return (optional)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/external/searchapi/maps/photos",
            body=await async_maybe_transform(
                {
                    "place_id": place_id,
                    "num": num,
                },
                searchapi_google_maps_place_photos_params.SearchapiGoogleMapsPlacePhotosParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SearchapiGoogleMapsPlacePhotosResponse,
        )

    async def google_maps_place_reviews(
        self,
        *,
        place_id: str,
        hl: Optional[str] | Omit = omit,
        num: Optional[int] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SearchapiGoogleMapsPlaceReviewsResponse:
        """
        Get reviews for a specific place

        Args:
          place_id: Place ID from Google Maps

          hl: Language (optional, e.g. "en", "es")

          num: Number of reviews to return (optional)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/external/searchapi/maps/reviews",
            body=await async_maybe_transform(
                {
                    "place_id": place_id,
                    "hl": hl,
                    "num": num,
                },
                searchapi_google_maps_place_reviews_params.SearchapiGoogleMapsPlaceReviewsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SearchapiGoogleMapsPlaceReviewsResponse,
        )

    async def google_maps_search(
        self,
        *,
        q: str,
        gl: Optional[str] | Omit = omit,
        hl: Optional[str] | Omit = omit,
        num: Optional[int] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SearchapiGoogleMapsSearchResponse:
        """
        Search for places on Google Maps

        Args:
          q: The search query (e.g., "restaurants near me")

          gl: Geographic location (optional, e.g. "us", "uk")

          hl: Language (optional, e.g. "en", "es")

          num: Number of results to return (optional)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/external/searchapi/maps/search",
            body=await async_maybe_transform(
                {
                    "q": q,
                    "gl": gl,
                    "hl": hl,
                    "num": num,
                },
                searchapi_google_maps_search_params.SearchapiGoogleMapsSearchParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SearchapiGoogleMapsSearchResponse,
        )

    async def google_scholar_author_search(
        self,
        *,
        author: str,
        hl: Optional[str] | Omit = omit,
        num: Optional[int] | Omit = omit,
        start: Optional[int] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SearchapiGoogleScholarAuthorSearchResponse:
        """
        Search for academic authors and their publications

        Args:
          author: Author name to search for

          hl: Language (optional, e.g. "en")

          num: Number of results to return (optional)

          start: Starting result index (optional)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/external/searchapi/scholar/author",
            body=await async_maybe_transform(
                {
                    "author": author,
                    "hl": hl,
                    "num": num,
                    "start": start,
                },
                searchapi_google_scholar_author_search_params.SearchapiGoogleScholarAuthorSearchParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SearchapiGoogleScholarAuthorSearchResponse,
        )

    async def google_scholar_citations(
        self,
        *,
        q: str,
        hl: Optional[str] | Omit = omit,
        num: Optional[int] | Omit = omit,
        start: Optional[int] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SearchapiGoogleScholarCitationsResponse:
        """
        Get citations for a specific academic publication

        Args:
          q: The publication ID to get citations for

          hl: Language (optional, e.g. "en")

          num: Number of citations to return (optional)

          start: Starting result index (optional)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/external/searchapi/scholar/cite",
            body=await async_maybe_transform(
                {
                    "q": q,
                    "hl": hl,
                    "num": num,
                    "start": start,
                },
                searchapi_google_scholar_citations_params.SearchapiGoogleScholarCitationsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SearchapiGoogleScholarCitationsResponse,
        )

    async def google_scholar_search(
        self,
        *,
        q: str,
        as_yhi: Optional[int] | Omit = omit,
        as_ylo: Optional[int] | Omit = omit,
        hl: Optional[str] | Omit = omit,
        num: Optional[int] | Omit = omit,
        start: Optional[int] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SearchapiGoogleScholarSearchResponse:
        """
        Search academic papers and publications on Google Scholar

        Args:
          q: The search query

          as_yhi: Year range end (optional, e.g. 2023)

          as_ylo: Year range start (optional, e.g. 2020)

          hl: Language (optional, e.g. "en")

          num: Number of results to return (optional)

          start: Starting result index (optional)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/external/searchapi/scholar/search",
            body=await async_maybe_transform(
                {
                    "q": q,
                    "as_yhi": as_yhi,
                    "as_ylo": as_ylo,
                    "hl": hl,
                    "num": num,
                    "start": start,
                },
                searchapi_google_scholar_search_params.SearchapiGoogleScholarSearchParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SearchapiGoogleScholarSearchResponse,
        )

    async def google_search(
        self,
        *,
        q: str,
        gl: Optional[str] | Omit = omit,
        hl: Optional[str] | Omit = omit,
        num: Optional[int] | Omit = omit,
        start: Optional[int] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> GoogleSearchResponse:
        """
        Performs a Google web search using the SearchAPI service

        Args:
          q: The search query

          gl: Geographic location (optional, e.g. "us", "uk")

          hl: Language (optional, e.g. "en", "es")

          num: Number of results to return (optional, max 100)

          start: Starting result index (optional)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/external/searchapi/search",
            body=await async_maybe_transform(
                {
                    "q": q,
                    "gl": gl,
                    "hl": hl,
                    "num": num,
                    "start": start,
                },
                searchapi_google_search_params.SearchapiGoogleSearchParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GoogleSearchResponse,
        )

    async def location_search(
        self,
        *,
        q: str,
        gl: Optional[str] | Omit = omit,
        hl: Optional[str] | Omit = omit,
        num: Optional[int] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LocationResponse:
        """
        Search for geographic locations, addresses, and places

        Args:
          q: The location query to search for

          gl: Geographic location bias (optional, e.g. "us", "uk")

          hl: Language (optional, e.g. "en")

          num: Number of results to return (optional)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/external/searchapi/locations",
            body=await async_maybe_transform(
                {
                    "q": q,
                    "gl": gl,
                    "hl": hl,
                    "num": num,
                },
                searchapi_location_search_params.SearchapiLocationSearchParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LocationResponse,
        )


class SearchapiResourceWithRawResponse:
    def __init__(self, searchapi: SearchapiResource) -> None:
        self._searchapi = searchapi

        self.google_flights_calendar = to_raw_response_wrapper(
            searchapi.google_flights_calendar,
        )
        self.google_flights_location_search = to_raw_response_wrapper(
            searchapi.google_flights_location_search,
        )
        self.google_flights_search = to_raw_response_wrapper(
            searchapi.google_flights_search,
        )
        self.google_maps_place_details = to_raw_response_wrapper(
            searchapi.google_maps_place_details,
        )
        self.google_maps_place_photos = to_raw_response_wrapper(
            searchapi.google_maps_place_photos,
        )
        self.google_maps_place_reviews = to_raw_response_wrapper(
            searchapi.google_maps_place_reviews,
        )
        self.google_maps_search = to_raw_response_wrapper(
            searchapi.google_maps_search,
        )
        self.google_scholar_author_search = to_raw_response_wrapper(
            searchapi.google_scholar_author_search,
        )
        self.google_scholar_citations = to_raw_response_wrapper(
            searchapi.google_scholar_citations,
        )
        self.google_scholar_search = to_raw_response_wrapper(
            searchapi.google_scholar_search,
        )
        self.google_search = to_raw_response_wrapper(
            searchapi.google_search,
        )
        self.location_search = to_raw_response_wrapper(
            searchapi.location_search,
        )


class AsyncSearchapiResourceWithRawResponse:
    def __init__(self, searchapi: AsyncSearchapiResource) -> None:
        self._searchapi = searchapi

        self.google_flights_calendar = async_to_raw_response_wrapper(
            searchapi.google_flights_calendar,
        )
        self.google_flights_location_search = async_to_raw_response_wrapper(
            searchapi.google_flights_location_search,
        )
        self.google_flights_search = async_to_raw_response_wrapper(
            searchapi.google_flights_search,
        )
        self.google_maps_place_details = async_to_raw_response_wrapper(
            searchapi.google_maps_place_details,
        )
        self.google_maps_place_photos = async_to_raw_response_wrapper(
            searchapi.google_maps_place_photos,
        )
        self.google_maps_place_reviews = async_to_raw_response_wrapper(
            searchapi.google_maps_place_reviews,
        )
        self.google_maps_search = async_to_raw_response_wrapper(
            searchapi.google_maps_search,
        )
        self.google_scholar_author_search = async_to_raw_response_wrapper(
            searchapi.google_scholar_author_search,
        )
        self.google_scholar_citations = async_to_raw_response_wrapper(
            searchapi.google_scholar_citations,
        )
        self.google_scholar_search = async_to_raw_response_wrapper(
            searchapi.google_scholar_search,
        )
        self.google_search = async_to_raw_response_wrapper(
            searchapi.google_search,
        )
        self.location_search = async_to_raw_response_wrapper(
            searchapi.location_search,
        )


class SearchapiResourceWithStreamingResponse:
    def __init__(self, searchapi: SearchapiResource) -> None:
        self._searchapi = searchapi

        self.google_flights_calendar = to_streamed_response_wrapper(
            searchapi.google_flights_calendar,
        )
        self.google_flights_location_search = to_streamed_response_wrapper(
            searchapi.google_flights_location_search,
        )
        self.google_flights_search = to_streamed_response_wrapper(
            searchapi.google_flights_search,
        )
        self.google_maps_place_details = to_streamed_response_wrapper(
            searchapi.google_maps_place_details,
        )
        self.google_maps_place_photos = to_streamed_response_wrapper(
            searchapi.google_maps_place_photos,
        )
        self.google_maps_place_reviews = to_streamed_response_wrapper(
            searchapi.google_maps_place_reviews,
        )
        self.google_maps_search = to_streamed_response_wrapper(
            searchapi.google_maps_search,
        )
        self.google_scholar_author_search = to_streamed_response_wrapper(
            searchapi.google_scholar_author_search,
        )
        self.google_scholar_citations = to_streamed_response_wrapper(
            searchapi.google_scholar_citations,
        )
        self.google_scholar_search = to_streamed_response_wrapper(
            searchapi.google_scholar_search,
        )
        self.google_search = to_streamed_response_wrapper(
            searchapi.google_search,
        )
        self.location_search = to_streamed_response_wrapper(
            searchapi.location_search,
        )


class AsyncSearchapiResourceWithStreamingResponse:
    def __init__(self, searchapi: AsyncSearchapiResource) -> None:
        self._searchapi = searchapi

        self.google_flights_calendar = async_to_streamed_response_wrapper(
            searchapi.google_flights_calendar,
        )
        self.google_flights_location_search = async_to_streamed_response_wrapper(
            searchapi.google_flights_location_search,
        )
        self.google_flights_search = async_to_streamed_response_wrapper(
            searchapi.google_flights_search,
        )
        self.google_maps_place_details = async_to_streamed_response_wrapper(
            searchapi.google_maps_place_details,
        )
        self.google_maps_place_photos = async_to_streamed_response_wrapper(
            searchapi.google_maps_place_photos,
        )
        self.google_maps_place_reviews = async_to_streamed_response_wrapper(
            searchapi.google_maps_place_reviews,
        )
        self.google_maps_search = async_to_streamed_response_wrapper(
            searchapi.google_maps_search,
        )
        self.google_scholar_author_search = async_to_streamed_response_wrapper(
            searchapi.google_scholar_author_search,
        )
        self.google_scholar_citations = async_to_streamed_response_wrapper(
            searchapi.google_scholar_citations,
        )
        self.google_scholar_search = async_to_streamed_response_wrapper(
            searchapi.google_scholar_search,
        )
        self.google_search = async_to_streamed_response_wrapper(
            searchapi.google_search,
        )
        self.location_search = async_to_streamed_response_wrapper(
            searchapi.location_search,
        )
