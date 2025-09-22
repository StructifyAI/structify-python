# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from structify import Structify, AsyncStructify
from tests.utils import assert_matches_type
from structify.types.external import (
    OrganizationDetail,
    JobPostingsResponse,
    PeopleMatchResponse,
    EnrichedOrganization,
    PeopleSearchResponse,
    CompaniesSearchResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPeople:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_companies_search(self, client: Structify) -> None:
        person = client.external.people.companies_search()
        assert_matches_type(CompaniesSearchResponse, person, path=["response"])

    @parametrize
    def test_method_companies_search_with_all_params(self, client: Structify) -> None:
        person = client.external.people.companies_search(
            organization_department_headcount_ranges=["string"],
            organization_founded_year_max=0,
            organization_founded_year_min=0,
            organization_locations=["string"],
            organization_naics_codes=["string"],
            organization_not_ids=["string"],
            organization_num_employees_ranges=["string"],
            organization_revenue_ranges=["string"],
            organization_sic_codes=["string"],
            organization_technologies=["string"],
            page=0,
            per_page=0,
            q_keywords="q_keywords",
            q_organization_industry_tag_ids=["string"],
            q_organization_keyword_tags=["string"],
            sort_ascending=True,
            sort_by_field="sort_by_field",
        )
        assert_matches_type(CompaniesSearchResponse, person, path=["response"])

    @parametrize
    def test_raw_response_companies_search(self, client: Structify) -> None:
        response = client.external.people.with_raw_response.companies_search()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        person = response.parse()
        assert_matches_type(CompaniesSearchResponse, person, path=["response"])

    @parametrize
    def test_streaming_response_companies_search(self, client: Structify) -> None:
        with client.external.people.with_streaming_response.companies_search() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            person = response.parse()
            assert_matches_type(CompaniesSearchResponse, person, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_organization_detail(self, client: Structify) -> None:
        person = client.external.people.organization_detail(
            "id",
        )
        assert_matches_type(OrganizationDetail, person, path=["response"])

    @parametrize
    def test_raw_response_organization_detail(self, client: Structify) -> None:
        response = client.external.people.with_raw_response.organization_detail(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        person = response.parse()
        assert_matches_type(OrganizationDetail, person, path=["response"])

    @parametrize
    def test_streaming_response_organization_detail(self, client: Structify) -> None:
        with client.external.people.with_streaming_response.organization_detail(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            person = response.parse()
            assert_matches_type(OrganizationDetail, person, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_organization_detail(self, client: Structify) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.external.people.with_raw_response.organization_detail(
                "",
            )

    @parametrize
    def test_method_organization_job_postings(self, client: Structify) -> None:
        person = client.external.people.organization_job_postings(
            organization_id="organization_id",
        )
        assert_matches_type(JobPostingsResponse, person, path=["response"])

    @parametrize
    def test_method_organization_job_postings_with_all_params(self, client: Structify) -> None:
        person = client.external.people.organization_job_postings(
            organization_id="organization_id",
            page=0,
            per_page=0,
        )
        assert_matches_type(JobPostingsResponse, person, path=["response"])

    @parametrize
    def test_raw_response_organization_job_postings(self, client: Structify) -> None:
        response = client.external.people.with_raw_response.organization_job_postings(
            organization_id="organization_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        person = response.parse()
        assert_matches_type(JobPostingsResponse, person, path=["response"])

    @parametrize
    def test_streaming_response_organization_job_postings(self, client: Structify) -> None:
        with client.external.people.with_streaming_response.organization_job_postings(
            organization_id="organization_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            person = response.parse()
            assert_matches_type(JobPostingsResponse, person, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_organization_job_postings(self, client: Structify) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `organization_id` but received ''"):
            client.external.people.with_raw_response.organization_job_postings(
                organization_id="",
            )

    @parametrize
    def test_method_organizations_enrich(self, client: Structify) -> None:
        person = client.external.people.organizations_enrich()
        assert_matches_type(EnrichedOrganization, person, path=["response"])

    @parametrize
    def test_method_organizations_enrich_with_all_params(self, client: Structify) -> None:
        person = client.external.people.organizations_enrich(
            domain="domain",
            organization_name="organization_name",
        )
        assert_matches_type(EnrichedOrganization, person, path=["response"])

    @parametrize
    def test_raw_response_organizations_enrich(self, client: Structify) -> None:
        response = client.external.people.with_raw_response.organizations_enrich()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        person = response.parse()
        assert_matches_type(EnrichedOrganization, person, path=["response"])

    @parametrize
    def test_streaming_response_organizations_enrich(self, client: Structify) -> None:
        with client.external.people.with_streaming_response.organizations_enrich() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            person = response.parse()
            assert_matches_type(EnrichedOrganization, person, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_people_match(self, client: Structify) -> None:
        person = client.external.people.people_match()
        assert_matches_type(PeopleMatchResponse, person, path=["response"])

    @parametrize
    def test_method_people_match_with_all_params(self, client: Structify) -> None:
        person = client.external.people.people_match(
            company_domain="company_domain",
            company_name="company_name",
            email="email",
            first_name="first_name",
            last_name="last_name",
            linkedin_url="linkedin_url",
            location="location",
            name="name",
            phone="phone",
            reveal_personal_emails=True,
            reveal_phone_number=True,
            reveal_professional_emails=True,
            title="title",
        )
        assert_matches_type(PeopleMatchResponse, person, path=["response"])

    @parametrize
    def test_raw_response_people_match(self, client: Structify) -> None:
        response = client.external.people.with_raw_response.people_match()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        person = response.parse()
        assert_matches_type(PeopleMatchResponse, person, path=["response"])

    @parametrize
    def test_streaming_response_people_match(self, client: Structify) -> None:
        with client.external.people.with_streaming_response.people_match() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            person = response.parse()
            assert_matches_type(PeopleMatchResponse, person, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_people_search(self, client: Structify) -> None:
        person = client.external.people.people_search()
        assert_matches_type(PeopleSearchResponse, person, path=["response"])

    @parametrize
    def test_method_people_search_with_all_params(self, client: Structify) -> None:
        person = client.external.people.people_search(
            contact_email_status=["string"],
            organization_ids=["string"],
            organization_locations=["string"],
            organization_num_employees_ranges=["string"],
            page=0,
            per_page=0,
            person_departments=["string"],
            person_locations=["string"],
            person_seniorities=["string"],
            person_titles=["string"],
            q_keywords="q_keywords",
            q_organization_industry_tag_ids=["string"],
            reveal_personal_emails=True,
            reveal_phone_number=True,
            reveal_professional_emails=True,
        )
        assert_matches_type(PeopleSearchResponse, person, path=["response"])

    @parametrize
    def test_raw_response_people_search(self, client: Structify) -> None:
        response = client.external.people.with_raw_response.people_search()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        person = response.parse()
        assert_matches_type(PeopleSearchResponse, person, path=["response"])

    @parametrize
    def test_streaming_response_people_search(self, client: Structify) -> None:
        with client.external.people.with_streaming_response.people_search() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            person = response.parse()
            assert_matches_type(PeopleSearchResponse, person, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncPeople:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_companies_search(self, async_client: AsyncStructify) -> None:
        person = await async_client.external.people.companies_search()
        assert_matches_type(CompaniesSearchResponse, person, path=["response"])

    @parametrize
    async def test_method_companies_search_with_all_params(self, async_client: AsyncStructify) -> None:
        person = await async_client.external.people.companies_search(
            organization_department_headcount_ranges=["string"],
            organization_founded_year_max=0,
            organization_founded_year_min=0,
            organization_locations=["string"],
            organization_naics_codes=["string"],
            organization_not_ids=["string"],
            organization_num_employees_ranges=["string"],
            organization_revenue_ranges=["string"],
            organization_sic_codes=["string"],
            organization_technologies=["string"],
            page=0,
            per_page=0,
            q_keywords="q_keywords",
            q_organization_industry_tag_ids=["string"],
            q_organization_keyword_tags=["string"],
            sort_ascending=True,
            sort_by_field="sort_by_field",
        )
        assert_matches_type(CompaniesSearchResponse, person, path=["response"])

    @parametrize
    async def test_raw_response_companies_search(self, async_client: AsyncStructify) -> None:
        response = await async_client.external.people.with_raw_response.companies_search()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        person = await response.parse()
        assert_matches_type(CompaniesSearchResponse, person, path=["response"])

    @parametrize
    async def test_streaming_response_companies_search(self, async_client: AsyncStructify) -> None:
        async with async_client.external.people.with_streaming_response.companies_search() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            person = await response.parse()
            assert_matches_type(CompaniesSearchResponse, person, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_organization_detail(self, async_client: AsyncStructify) -> None:
        person = await async_client.external.people.organization_detail(
            "id",
        )
        assert_matches_type(OrganizationDetail, person, path=["response"])

    @parametrize
    async def test_raw_response_organization_detail(self, async_client: AsyncStructify) -> None:
        response = await async_client.external.people.with_raw_response.organization_detail(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        person = await response.parse()
        assert_matches_type(OrganizationDetail, person, path=["response"])

    @parametrize
    async def test_streaming_response_organization_detail(self, async_client: AsyncStructify) -> None:
        async with async_client.external.people.with_streaming_response.organization_detail(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            person = await response.parse()
            assert_matches_type(OrganizationDetail, person, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_organization_detail(self, async_client: AsyncStructify) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.external.people.with_raw_response.organization_detail(
                "",
            )

    @parametrize
    async def test_method_organization_job_postings(self, async_client: AsyncStructify) -> None:
        person = await async_client.external.people.organization_job_postings(
            organization_id="organization_id",
        )
        assert_matches_type(JobPostingsResponse, person, path=["response"])

    @parametrize
    async def test_method_organization_job_postings_with_all_params(self, async_client: AsyncStructify) -> None:
        person = await async_client.external.people.organization_job_postings(
            organization_id="organization_id",
            page=0,
            per_page=0,
        )
        assert_matches_type(JobPostingsResponse, person, path=["response"])

    @parametrize
    async def test_raw_response_organization_job_postings(self, async_client: AsyncStructify) -> None:
        response = await async_client.external.people.with_raw_response.organization_job_postings(
            organization_id="organization_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        person = await response.parse()
        assert_matches_type(JobPostingsResponse, person, path=["response"])

    @parametrize
    async def test_streaming_response_organization_job_postings(self, async_client: AsyncStructify) -> None:
        async with async_client.external.people.with_streaming_response.organization_job_postings(
            organization_id="organization_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            person = await response.parse()
            assert_matches_type(JobPostingsResponse, person, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_organization_job_postings(self, async_client: AsyncStructify) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `organization_id` but received ''"):
            await async_client.external.people.with_raw_response.organization_job_postings(
                organization_id="",
            )

    @parametrize
    async def test_method_organizations_enrich(self, async_client: AsyncStructify) -> None:
        person = await async_client.external.people.organizations_enrich()
        assert_matches_type(EnrichedOrganization, person, path=["response"])

    @parametrize
    async def test_method_organizations_enrich_with_all_params(self, async_client: AsyncStructify) -> None:
        person = await async_client.external.people.organizations_enrich(
            domain="domain",
            organization_name="organization_name",
        )
        assert_matches_type(EnrichedOrganization, person, path=["response"])

    @parametrize
    async def test_raw_response_organizations_enrich(self, async_client: AsyncStructify) -> None:
        response = await async_client.external.people.with_raw_response.organizations_enrich()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        person = await response.parse()
        assert_matches_type(EnrichedOrganization, person, path=["response"])

    @parametrize
    async def test_streaming_response_organizations_enrich(self, async_client: AsyncStructify) -> None:
        async with async_client.external.people.with_streaming_response.organizations_enrich() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            person = await response.parse()
            assert_matches_type(EnrichedOrganization, person, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_people_match(self, async_client: AsyncStructify) -> None:
        person = await async_client.external.people.people_match()
        assert_matches_type(PeopleMatchResponse, person, path=["response"])

    @parametrize
    async def test_method_people_match_with_all_params(self, async_client: AsyncStructify) -> None:
        person = await async_client.external.people.people_match(
            company_domain="company_domain",
            company_name="company_name",
            email="email",
            first_name="first_name",
            last_name="last_name",
            linkedin_url="linkedin_url",
            location="location",
            name="name",
            phone="phone",
            reveal_personal_emails=True,
            reveal_phone_number=True,
            reveal_professional_emails=True,
            title="title",
        )
        assert_matches_type(PeopleMatchResponse, person, path=["response"])

    @parametrize
    async def test_raw_response_people_match(self, async_client: AsyncStructify) -> None:
        response = await async_client.external.people.with_raw_response.people_match()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        person = await response.parse()
        assert_matches_type(PeopleMatchResponse, person, path=["response"])

    @parametrize
    async def test_streaming_response_people_match(self, async_client: AsyncStructify) -> None:
        async with async_client.external.people.with_streaming_response.people_match() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            person = await response.parse()
            assert_matches_type(PeopleMatchResponse, person, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_people_search(self, async_client: AsyncStructify) -> None:
        person = await async_client.external.people.people_search()
        assert_matches_type(PeopleSearchResponse, person, path=["response"])

    @parametrize
    async def test_method_people_search_with_all_params(self, async_client: AsyncStructify) -> None:
        person = await async_client.external.people.people_search(
            contact_email_status=["string"],
            organization_ids=["string"],
            organization_locations=["string"],
            organization_num_employees_ranges=["string"],
            page=0,
            per_page=0,
            person_departments=["string"],
            person_locations=["string"],
            person_seniorities=["string"],
            person_titles=["string"],
            q_keywords="q_keywords",
            q_organization_industry_tag_ids=["string"],
            reveal_personal_emails=True,
            reveal_phone_number=True,
            reveal_professional_emails=True,
        )
        assert_matches_type(PeopleSearchResponse, person, path=["response"])

    @parametrize
    async def test_raw_response_people_search(self, async_client: AsyncStructify) -> None:
        response = await async_client.external.people.with_raw_response.people_search()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        person = await response.parse()
        assert_matches_type(PeopleSearchResponse, person, path=["response"])

    @parametrize
    async def test_streaming_response_people_search(self, async_client: AsyncStructify) -> None:
        async with async_client.external.people.with_streaming_response.people_search() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            person = await response.parse()
            assert_matches_type(PeopleSearchResponse, person, path=["response"])

        assert cast(Any, response.is_closed) is True
