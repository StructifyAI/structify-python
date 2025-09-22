# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
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
    person_people_match_params,
    person_people_search_params,
    person_companies_search_params,
    person_organizations_enrich_params,
    person_organization_job_postings_params,
)
from ...types.external.organization_detail import OrganizationDetail
from ...types.external.enriched_organization import EnrichedOrganization
from ...types.external.job_postings_response import JobPostingsResponse
from ...types.external.people_match_response import PeopleMatchResponse
from ...types.external.people_search_response import PeopleSearchResponse
from ...types.external.companies_search_response import CompaniesSearchResponse

__all__ = ["PeopleResource", "AsyncPeopleResource"]


class PeopleResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PeopleResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/StructifyAI/structify-python#accessing-raw-response-data-eg-headers
        """
        return PeopleResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PeopleResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/StructifyAI/structify-python#with_streaming_response
        """
        return PeopleResourceWithStreamingResponse(self)

    def companies_search(
        self,
        *,
        organization_department_headcount_ranges: Optional[SequenceNotStr[str]] | Omit = omit,
        organization_founded_year_max: Optional[int] | Omit = omit,
        organization_founded_year_min: Optional[int] | Omit = omit,
        organization_locations: Optional[SequenceNotStr[str]] | Omit = omit,
        organization_naics_codes: Optional[SequenceNotStr[str]] | Omit = omit,
        organization_not_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        organization_num_employees_ranges: Optional[SequenceNotStr[str]] | Omit = omit,
        organization_revenue_ranges: Optional[SequenceNotStr[str]] | Omit = omit,
        organization_sic_codes: Optional[SequenceNotStr[str]] | Omit = omit,
        organization_technologies: Optional[SequenceNotStr[str]] | Omit = omit,
        page: Optional[int] | Omit = omit,
        per_page: Optional[int] | Omit = omit,
        q_keywords: Optional[str] | Omit = omit,
        q_organization_industry_tag_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        q_organization_keyword_tags: Optional[SequenceNotStr[str]] | Omit = omit,
        sort_ascending: Optional[bool] | Omit = omit,
        sort_by_field: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CompaniesSearchResponse:
        """
        Search for companies using various filters and criteria

        Args:
          organization_department_headcount_ranges: Organization department headcount ranges

          organization_founded_year_max: Organization founded year maximum

          organization_founded_year_min: Organization founded year minimum

          organization_locations: Organization locations

          organization_naics_codes: Organization NAICS codes

          organization_not_ids: Organization ids to exclude

          organization_num_employees_ranges: Organization num employees ranges

          organization_revenue_ranges: Organization revenue ranges

          organization_sic_codes: Organization SIC codes

          organization_technologies: Organization technologies

          page: Page number (default: 1)

          per_page: Number of results per page (max 200)

          q_keywords: Keywords to search for

          q_organization_industry_tag_ids: Organization industries

          q_organization_keyword_tags: Organization keyword tags

          sort_ascending: Sort ascending

          sort_by_field: Sort by field

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/external/people/mixed_companies/search",
            body=maybe_transform(
                {
                    "organization_department_headcount_ranges": organization_department_headcount_ranges,
                    "organization_founded_year_max": organization_founded_year_max,
                    "organization_founded_year_min": organization_founded_year_min,
                    "organization_locations": organization_locations,
                    "organization_naics_codes": organization_naics_codes,
                    "organization_not_ids": organization_not_ids,
                    "organization_num_employees_ranges": organization_num_employees_ranges,
                    "organization_revenue_ranges": organization_revenue_ranges,
                    "organization_sic_codes": organization_sic_codes,
                    "organization_technologies": organization_technologies,
                    "page": page,
                    "per_page": per_page,
                    "q_keywords": q_keywords,
                    "q_organization_industry_tag_ids": q_organization_industry_tag_ids,
                    "q_organization_keyword_tags": q_organization_keyword_tags,
                    "sort_ascending": sort_ascending,
                    "sort_by_field": sort_by_field,
                },
                person_companies_search_params.PersonCompaniesSearchParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CompaniesSearchResponse,
        )

    def organization_detail(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OrganizationDetail:
        """
        Retrieve detailed information about a specific organization

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/external/people/organizations/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OrganizationDetail,
        )

    def organization_job_postings(
        self,
        organization_id: str,
        *,
        page: Optional[int] | Omit = omit,
        per_page: Optional[int] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> JobPostingsResponse:
        """
        Retrieve job postings for a specific organization

        Args:
          page: Page number

          per_page: Results per page

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not organization_id:
            raise ValueError(f"Expected a non-empty value for `organization_id` but received {organization_id!r}")
        return self._get(
            f"/external/people/organizations/{organization_id}/job_postings",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "page": page,
                        "per_page": per_page,
                    },
                    person_organization_job_postings_params.PersonOrganizationJobPostingsParams,
                ),
            ),
            cast_to=JobPostingsResponse,
        )

    def organizations_enrich(
        self,
        *,
        domain: Optional[str] | Omit = omit,
        organization_name: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EnrichedOrganization:
        """
        Enrich organization data using Apollo.io's organization enrichment

        Args:
          domain: Organization domain

          organization_name: Organization name

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/external/people/organizations/enrich",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "domain": domain,
                        "organization_name": organization_name,
                    },
                    person_organizations_enrich_params.PersonOrganizationsEnrichParams,
                ),
            ),
            cast_to=EnrichedOrganization,
        )

    def people_match(
        self,
        *,
        company_domain: Optional[str] | Omit = omit,
        company_name: Optional[str] | Omit = omit,
        email: Optional[str] | Omit = omit,
        first_name: Optional[str] | Omit = omit,
        last_name: Optional[str] | Omit = omit,
        linkedin_url: Optional[str] | Omit = omit,
        location: Optional[str] | Omit = omit,
        name: Optional[str] | Omit = omit,
        phone: Optional[str] | Omit = omit,
        reveal_personal_emails: Optional[bool] | Omit = omit,
        reveal_phone_number: Optional[bool] | Omit = omit,
        reveal_professional_emails: Optional[bool] | Omit = omit,
        title: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PeopleMatchResponse:
        """
        Enrich a single person's profile data using Apollo.io's person matching

        Args:
          company_domain: Company domain

          company_name: Company name

          email: Email address

          first_name: First name

          last_name: Last name

          linkedin_url: LinkedIn URL

          location: Location (city, state, country)

          name: Full name (alternative to first/last)

          phone: Phone number

          reveal_personal_emails: Whether to reveal personal email

          reveal_phone_number: Whether to reveal phone numbers

          reveal_professional_emails: Whether to reveal work email

          title: Job title

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/external/people/people/match",
            body=maybe_transform(
                {
                    "company_domain": company_domain,
                    "company_name": company_name,
                    "email": email,
                    "first_name": first_name,
                    "last_name": last_name,
                    "linkedin_url": linkedin_url,
                    "location": location,
                    "name": name,
                    "phone": phone,
                    "reveal_personal_emails": reveal_personal_emails,
                    "reveal_phone_number": reveal_phone_number,
                    "reveal_professional_emails": reveal_professional_emails,
                    "title": title,
                },
                person_people_match_params.PersonPeopleMatchParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PeopleMatchResponse,
        )

    def people_search(
        self,
        *,
        contact_email_status: Optional[SequenceNotStr[str]] | Omit = omit,
        organization_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        organization_locations: Optional[SequenceNotStr[str]] | Omit = omit,
        organization_num_employees_ranges: Optional[SequenceNotStr[str]] | Omit = omit,
        page: Optional[int] | Omit = omit,
        per_page: Optional[int] | Omit = omit,
        person_departments: Optional[SequenceNotStr[str]] | Omit = omit,
        person_locations: Optional[SequenceNotStr[str]] | Omit = omit,
        person_seniorities: Optional[SequenceNotStr[str]] | Omit = omit,
        person_titles: Optional[SequenceNotStr[str]] | Omit = omit,
        q_keywords: Optional[str] | Omit = omit,
        q_organization_industry_tag_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        reveal_personal_emails: Optional[bool] | Omit = omit,
        reveal_phone_number: Optional[bool] | Omit = omit,
        reveal_professional_emails: Optional[bool] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PeopleSearchResponse:
        """
        Search for people using various filters and criteria

        Args:
          contact_email_status: Contact email status

          organization_ids: Organization ids

          organization_locations: Organization locations

          organization_num_employees_ranges: Organization num employees ranges

          page: Page number (default: 1)

          per_page: Number of results per page (max 200)

          person_departments: Person departments

          person_locations: Person locations

          person_seniorities: Person seniorities

          person_titles: Person titles to include

          q_keywords: Keywords

          q_organization_industry_tag_ids: Organization industries

          reveal_personal_emails: Reveal personal emails

          reveal_phone_number: Reveal phone numbers

          reveal_professional_emails: Reveal work emails

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/external/people/mixed_people/search",
            body=maybe_transform(
                {
                    "contact_email_status": contact_email_status,
                    "organization_ids": organization_ids,
                    "organization_locations": organization_locations,
                    "organization_num_employees_ranges": organization_num_employees_ranges,
                    "page": page,
                    "per_page": per_page,
                    "person_departments": person_departments,
                    "person_locations": person_locations,
                    "person_seniorities": person_seniorities,
                    "person_titles": person_titles,
                    "q_keywords": q_keywords,
                    "q_organization_industry_tag_ids": q_organization_industry_tag_ids,
                    "reveal_personal_emails": reveal_personal_emails,
                    "reveal_phone_number": reveal_phone_number,
                    "reveal_professional_emails": reveal_professional_emails,
                },
                person_people_search_params.PersonPeopleSearchParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PeopleSearchResponse,
        )


class AsyncPeopleResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPeopleResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/StructifyAI/structify-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPeopleResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPeopleResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/StructifyAI/structify-python#with_streaming_response
        """
        return AsyncPeopleResourceWithStreamingResponse(self)

    async def companies_search(
        self,
        *,
        organization_department_headcount_ranges: Optional[SequenceNotStr[str]] | Omit = omit,
        organization_founded_year_max: Optional[int] | Omit = omit,
        organization_founded_year_min: Optional[int] | Omit = omit,
        organization_locations: Optional[SequenceNotStr[str]] | Omit = omit,
        organization_naics_codes: Optional[SequenceNotStr[str]] | Omit = omit,
        organization_not_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        organization_num_employees_ranges: Optional[SequenceNotStr[str]] | Omit = omit,
        organization_revenue_ranges: Optional[SequenceNotStr[str]] | Omit = omit,
        organization_sic_codes: Optional[SequenceNotStr[str]] | Omit = omit,
        organization_technologies: Optional[SequenceNotStr[str]] | Omit = omit,
        page: Optional[int] | Omit = omit,
        per_page: Optional[int] | Omit = omit,
        q_keywords: Optional[str] | Omit = omit,
        q_organization_industry_tag_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        q_organization_keyword_tags: Optional[SequenceNotStr[str]] | Omit = omit,
        sort_ascending: Optional[bool] | Omit = omit,
        sort_by_field: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CompaniesSearchResponse:
        """
        Search for companies using various filters and criteria

        Args:
          organization_department_headcount_ranges: Organization department headcount ranges

          organization_founded_year_max: Organization founded year maximum

          organization_founded_year_min: Organization founded year minimum

          organization_locations: Organization locations

          organization_naics_codes: Organization NAICS codes

          organization_not_ids: Organization ids to exclude

          organization_num_employees_ranges: Organization num employees ranges

          organization_revenue_ranges: Organization revenue ranges

          organization_sic_codes: Organization SIC codes

          organization_technologies: Organization technologies

          page: Page number (default: 1)

          per_page: Number of results per page (max 200)

          q_keywords: Keywords to search for

          q_organization_industry_tag_ids: Organization industries

          q_organization_keyword_tags: Organization keyword tags

          sort_ascending: Sort ascending

          sort_by_field: Sort by field

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/external/people/mixed_companies/search",
            body=await async_maybe_transform(
                {
                    "organization_department_headcount_ranges": organization_department_headcount_ranges,
                    "organization_founded_year_max": organization_founded_year_max,
                    "organization_founded_year_min": organization_founded_year_min,
                    "organization_locations": organization_locations,
                    "organization_naics_codes": organization_naics_codes,
                    "organization_not_ids": organization_not_ids,
                    "organization_num_employees_ranges": organization_num_employees_ranges,
                    "organization_revenue_ranges": organization_revenue_ranges,
                    "organization_sic_codes": organization_sic_codes,
                    "organization_technologies": organization_technologies,
                    "page": page,
                    "per_page": per_page,
                    "q_keywords": q_keywords,
                    "q_organization_industry_tag_ids": q_organization_industry_tag_ids,
                    "q_organization_keyword_tags": q_organization_keyword_tags,
                    "sort_ascending": sort_ascending,
                    "sort_by_field": sort_by_field,
                },
                person_companies_search_params.PersonCompaniesSearchParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CompaniesSearchResponse,
        )

    async def organization_detail(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OrganizationDetail:
        """
        Retrieve detailed information about a specific organization

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/external/people/organizations/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OrganizationDetail,
        )

    async def organization_job_postings(
        self,
        organization_id: str,
        *,
        page: Optional[int] | Omit = omit,
        per_page: Optional[int] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> JobPostingsResponse:
        """
        Retrieve job postings for a specific organization

        Args:
          page: Page number

          per_page: Results per page

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not organization_id:
            raise ValueError(f"Expected a non-empty value for `organization_id` but received {organization_id!r}")
        return await self._get(
            f"/external/people/organizations/{organization_id}/job_postings",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "page": page,
                        "per_page": per_page,
                    },
                    person_organization_job_postings_params.PersonOrganizationJobPostingsParams,
                ),
            ),
            cast_to=JobPostingsResponse,
        )

    async def organizations_enrich(
        self,
        *,
        domain: Optional[str] | Omit = omit,
        organization_name: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EnrichedOrganization:
        """
        Enrich organization data using Apollo.io's organization enrichment

        Args:
          domain: Organization domain

          organization_name: Organization name

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/external/people/organizations/enrich",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "domain": domain,
                        "organization_name": organization_name,
                    },
                    person_organizations_enrich_params.PersonOrganizationsEnrichParams,
                ),
            ),
            cast_to=EnrichedOrganization,
        )

    async def people_match(
        self,
        *,
        company_domain: Optional[str] | Omit = omit,
        company_name: Optional[str] | Omit = omit,
        email: Optional[str] | Omit = omit,
        first_name: Optional[str] | Omit = omit,
        last_name: Optional[str] | Omit = omit,
        linkedin_url: Optional[str] | Omit = omit,
        location: Optional[str] | Omit = omit,
        name: Optional[str] | Omit = omit,
        phone: Optional[str] | Omit = omit,
        reveal_personal_emails: Optional[bool] | Omit = omit,
        reveal_phone_number: Optional[bool] | Omit = omit,
        reveal_professional_emails: Optional[bool] | Omit = omit,
        title: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PeopleMatchResponse:
        """
        Enrich a single person's profile data using Apollo.io's person matching

        Args:
          company_domain: Company domain

          company_name: Company name

          email: Email address

          first_name: First name

          last_name: Last name

          linkedin_url: LinkedIn URL

          location: Location (city, state, country)

          name: Full name (alternative to first/last)

          phone: Phone number

          reveal_personal_emails: Whether to reveal personal email

          reveal_phone_number: Whether to reveal phone numbers

          reveal_professional_emails: Whether to reveal work email

          title: Job title

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/external/people/people/match",
            body=await async_maybe_transform(
                {
                    "company_domain": company_domain,
                    "company_name": company_name,
                    "email": email,
                    "first_name": first_name,
                    "last_name": last_name,
                    "linkedin_url": linkedin_url,
                    "location": location,
                    "name": name,
                    "phone": phone,
                    "reveal_personal_emails": reveal_personal_emails,
                    "reveal_phone_number": reveal_phone_number,
                    "reveal_professional_emails": reveal_professional_emails,
                    "title": title,
                },
                person_people_match_params.PersonPeopleMatchParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PeopleMatchResponse,
        )

    async def people_search(
        self,
        *,
        contact_email_status: Optional[SequenceNotStr[str]] | Omit = omit,
        organization_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        organization_locations: Optional[SequenceNotStr[str]] | Omit = omit,
        organization_num_employees_ranges: Optional[SequenceNotStr[str]] | Omit = omit,
        page: Optional[int] | Omit = omit,
        per_page: Optional[int] | Omit = omit,
        person_departments: Optional[SequenceNotStr[str]] | Omit = omit,
        person_locations: Optional[SequenceNotStr[str]] | Omit = omit,
        person_seniorities: Optional[SequenceNotStr[str]] | Omit = omit,
        person_titles: Optional[SequenceNotStr[str]] | Omit = omit,
        q_keywords: Optional[str] | Omit = omit,
        q_organization_industry_tag_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        reveal_personal_emails: Optional[bool] | Omit = omit,
        reveal_phone_number: Optional[bool] | Omit = omit,
        reveal_professional_emails: Optional[bool] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PeopleSearchResponse:
        """
        Search for people using various filters and criteria

        Args:
          contact_email_status: Contact email status

          organization_ids: Organization ids

          organization_locations: Organization locations

          organization_num_employees_ranges: Organization num employees ranges

          page: Page number (default: 1)

          per_page: Number of results per page (max 200)

          person_departments: Person departments

          person_locations: Person locations

          person_seniorities: Person seniorities

          person_titles: Person titles to include

          q_keywords: Keywords

          q_organization_industry_tag_ids: Organization industries

          reveal_personal_emails: Reveal personal emails

          reveal_phone_number: Reveal phone numbers

          reveal_professional_emails: Reveal work emails

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/external/people/mixed_people/search",
            body=await async_maybe_transform(
                {
                    "contact_email_status": contact_email_status,
                    "organization_ids": organization_ids,
                    "organization_locations": organization_locations,
                    "organization_num_employees_ranges": organization_num_employees_ranges,
                    "page": page,
                    "per_page": per_page,
                    "person_departments": person_departments,
                    "person_locations": person_locations,
                    "person_seniorities": person_seniorities,
                    "person_titles": person_titles,
                    "q_keywords": q_keywords,
                    "q_organization_industry_tag_ids": q_organization_industry_tag_ids,
                    "reveal_personal_emails": reveal_personal_emails,
                    "reveal_phone_number": reveal_phone_number,
                    "reveal_professional_emails": reveal_professional_emails,
                },
                person_people_search_params.PersonPeopleSearchParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PeopleSearchResponse,
        )


class PeopleResourceWithRawResponse:
    def __init__(self, people: PeopleResource) -> None:
        self._people = people

        self.companies_search = to_raw_response_wrapper(
            people.companies_search,
        )
        self.organization_detail = to_raw_response_wrapper(
            people.organization_detail,
        )
        self.organization_job_postings = to_raw_response_wrapper(
            people.organization_job_postings,
        )
        self.organizations_enrich = to_raw_response_wrapper(
            people.organizations_enrich,
        )
        self.people_match = to_raw_response_wrapper(
            people.people_match,
        )
        self.people_search = to_raw_response_wrapper(
            people.people_search,
        )


class AsyncPeopleResourceWithRawResponse:
    def __init__(self, people: AsyncPeopleResource) -> None:
        self._people = people

        self.companies_search = async_to_raw_response_wrapper(
            people.companies_search,
        )
        self.organization_detail = async_to_raw_response_wrapper(
            people.organization_detail,
        )
        self.organization_job_postings = async_to_raw_response_wrapper(
            people.organization_job_postings,
        )
        self.organizations_enrich = async_to_raw_response_wrapper(
            people.organizations_enrich,
        )
        self.people_match = async_to_raw_response_wrapper(
            people.people_match,
        )
        self.people_search = async_to_raw_response_wrapper(
            people.people_search,
        )


class PeopleResourceWithStreamingResponse:
    def __init__(self, people: PeopleResource) -> None:
        self._people = people

        self.companies_search = to_streamed_response_wrapper(
            people.companies_search,
        )
        self.organization_detail = to_streamed_response_wrapper(
            people.organization_detail,
        )
        self.organization_job_postings = to_streamed_response_wrapper(
            people.organization_job_postings,
        )
        self.organizations_enrich = to_streamed_response_wrapper(
            people.organizations_enrich,
        )
        self.people_match = to_streamed_response_wrapper(
            people.people_match,
        )
        self.people_search = to_streamed_response_wrapper(
            people.people_search,
        )


class AsyncPeopleResourceWithStreamingResponse:
    def __init__(self, people: AsyncPeopleResource) -> None:
        self._people = people

        self.companies_search = async_to_streamed_response_wrapper(
            people.companies_search,
        )
        self.organization_detail = async_to_streamed_response_wrapper(
            people.organization_detail,
        )
        self.organization_job_postings = async_to_streamed_response_wrapper(
            people.organization_job_postings,
        )
        self.organizations_enrich = async_to_streamed_response_wrapper(
            people.organizations_enrich,
        )
        self.people_match = async_to_streamed_response_wrapper(
            people.people_match,
        )
        self.people_search = async_to_streamed_response_wrapper(
            people.people_search,
        )
