# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from structify import Structify, AsyncStructify
from tests.utils import assert_matches_type
from structify.types import (
    GetTeamResponse,
    AddMemberResponse,
    ListTeamsResponse,
    CreateTeamResponse,
    DeleteTeamResponse,
    UpdateTeamResponse,
    ListMembersResponse,
    ListProjectsResponse,
    RemoveMemberResponse,
    CreateProjectResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTeams:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Structify) -> None:
        team = client.teams.create(
            name="name",
        )
        assert_matches_type(CreateTeamResponse, team, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Structify) -> None:
        team = client.teams.create(
            name="name",
            description="description",
        )
        assert_matches_type(CreateTeamResponse, team, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Structify) -> None:
        response = client.teams.with_raw_response.create(
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        team = response.parse()
        assert_matches_type(CreateTeamResponse, team, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Structify) -> None:
        with client.teams.with_streaming_response.create(
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            team = response.parse()
            assert_matches_type(CreateTeamResponse, team, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_update(self, client: Structify) -> None:
        team = client.teams.update(
            team_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(UpdateTeamResponse, team, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Structify) -> None:
        team = client.teams.update(
            team_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            description="description",
            name="name",
        )
        assert_matches_type(UpdateTeamResponse, team, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Structify) -> None:
        response = client.teams.with_raw_response.update(
            team_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        team = response.parse()
        assert_matches_type(UpdateTeamResponse, team, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Structify) -> None:
        with client.teams.with_streaming_response.update(
            team_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            team = response.parse()
            assert_matches_type(UpdateTeamResponse, team, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Structify) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `team_id` but received ''"):
            client.teams.with_raw_response.update(
                team_id="",
            )

    @parametrize
    def test_method_list(self, client: Structify) -> None:
        team = client.teams.list()
        assert_matches_type(ListTeamsResponse, team, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Structify) -> None:
        response = client.teams.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        team = response.parse()
        assert_matches_type(ListTeamsResponse, team, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Structify) -> None:
        with client.teams.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            team = response.parse()
            assert_matches_type(ListTeamsResponse, team, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Structify) -> None:
        team = client.teams.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(DeleteTeamResponse, team, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Structify) -> None:
        response = client.teams.with_raw_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        team = response.parse()
        assert_matches_type(DeleteTeamResponse, team, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Structify) -> None:
        with client.teams.with_streaming_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            team = response.parse()
            assert_matches_type(DeleteTeamResponse, team, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Structify) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `team_id` but received ''"):
            client.teams.with_raw_response.delete(
                "",
            )

    @parametrize
    def test_method_add_member(self, client: Structify) -> None:
        team = client.teams.add_member(
            team_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            role="member",
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(AddMemberResponse, team, path=["response"])

    @parametrize
    def test_raw_response_add_member(self, client: Structify) -> None:
        response = client.teams.with_raw_response.add_member(
            team_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            role="member",
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        team = response.parse()
        assert_matches_type(AddMemberResponse, team, path=["response"])

    @parametrize
    def test_streaming_response_add_member(self, client: Structify) -> None:
        with client.teams.with_streaming_response.add_member(
            team_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            role="member",
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            team = response.parse()
            assert_matches_type(AddMemberResponse, team, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_add_member(self, client: Structify) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `team_id` but received ''"):
            client.teams.with_raw_response.add_member(
                team_id="",
                role="member",
                user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @parametrize
    def test_method_create_project(self, client: Structify) -> None:
        team = client.teams.create_project(
            team_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            name="name",
        )
        assert_matches_type(CreateProjectResponse, team, path=["response"])

    @parametrize
    def test_method_create_project_with_all_params(self, client: Structify) -> None:
        team = client.teams.create_project(
            team_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            name="name",
            description="description",
        )
        assert_matches_type(CreateProjectResponse, team, path=["response"])

    @parametrize
    def test_raw_response_create_project(self, client: Structify) -> None:
        response = client.teams.with_raw_response.create_project(
            team_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        team = response.parse()
        assert_matches_type(CreateProjectResponse, team, path=["response"])

    @parametrize
    def test_streaming_response_create_project(self, client: Structify) -> None:
        with client.teams.with_streaming_response.create_project(
            team_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            team = response.parse()
            assert_matches_type(CreateProjectResponse, team, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create_project(self, client: Structify) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `team_id` but received ''"):
            client.teams.with_raw_response.create_project(
                team_id="",
                name="name",
            )

    @parametrize
    def test_method_get(self, client: Structify) -> None:
        team = client.teams.get(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(GetTeamResponse, team, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Structify) -> None:
        response = client.teams.with_raw_response.get(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        team = response.parse()
        assert_matches_type(GetTeamResponse, team, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Structify) -> None:
        with client.teams.with_streaming_response.get(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            team = response.parse()
            assert_matches_type(GetTeamResponse, team, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Structify) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `team_id` but received ''"):
            client.teams.with_raw_response.get(
                "",
            )

    @parametrize
    def test_method_list_members(self, client: Structify) -> None:
        team = client.teams.list_members(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ListMembersResponse, team, path=["response"])

    @parametrize
    def test_raw_response_list_members(self, client: Structify) -> None:
        response = client.teams.with_raw_response.list_members(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        team = response.parse()
        assert_matches_type(ListMembersResponse, team, path=["response"])

    @parametrize
    def test_streaming_response_list_members(self, client: Structify) -> None:
        with client.teams.with_streaming_response.list_members(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            team = response.parse()
            assert_matches_type(ListMembersResponse, team, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list_members(self, client: Structify) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `team_id` but received ''"):
            client.teams.with_raw_response.list_members(
                "",
            )

    @parametrize
    def test_method_list_projects(self, client: Structify) -> None:
        team = client.teams.list_projects(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ListProjectsResponse, team, path=["response"])

    @parametrize
    def test_raw_response_list_projects(self, client: Structify) -> None:
        response = client.teams.with_raw_response.list_projects(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        team = response.parse()
        assert_matches_type(ListProjectsResponse, team, path=["response"])

    @parametrize
    def test_streaming_response_list_projects(self, client: Structify) -> None:
        with client.teams.with_streaming_response.list_projects(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            team = response.parse()
            assert_matches_type(ListProjectsResponse, team, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list_projects(self, client: Structify) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `team_id` but received ''"):
            client.teams.with_raw_response.list_projects(
                "",
            )

    @parametrize
    def test_method_remove_member(self, client: Structify) -> None:
        team = client.teams.remove_member(
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            team_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(RemoveMemberResponse, team, path=["response"])

    @parametrize
    def test_raw_response_remove_member(self, client: Structify) -> None:
        response = client.teams.with_raw_response.remove_member(
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            team_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        team = response.parse()
        assert_matches_type(RemoveMemberResponse, team, path=["response"])

    @parametrize
    def test_streaming_response_remove_member(self, client: Structify) -> None:
        with client.teams.with_streaming_response.remove_member(
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            team_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            team = response.parse()
            assert_matches_type(RemoveMemberResponse, team, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_remove_member(self, client: Structify) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `team_id` but received ''"):
            client.teams.with_raw_response.remove_member(
                user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                team_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            client.teams.with_raw_response.remove_member(
                user_id="",
                team_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )


class TestAsyncTeams:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncStructify) -> None:
        team = await async_client.teams.create(
            name="name",
        )
        assert_matches_type(CreateTeamResponse, team, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncStructify) -> None:
        team = await async_client.teams.create(
            name="name",
            description="description",
        )
        assert_matches_type(CreateTeamResponse, team, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncStructify) -> None:
        response = await async_client.teams.with_raw_response.create(
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        team = await response.parse()
        assert_matches_type(CreateTeamResponse, team, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncStructify) -> None:
        async with async_client.teams.with_streaming_response.create(
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            team = await response.parse()
            assert_matches_type(CreateTeamResponse, team, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_update(self, async_client: AsyncStructify) -> None:
        team = await async_client.teams.update(
            team_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(UpdateTeamResponse, team, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncStructify) -> None:
        team = await async_client.teams.update(
            team_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            description="description",
            name="name",
        )
        assert_matches_type(UpdateTeamResponse, team, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncStructify) -> None:
        response = await async_client.teams.with_raw_response.update(
            team_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        team = await response.parse()
        assert_matches_type(UpdateTeamResponse, team, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncStructify) -> None:
        async with async_client.teams.with_streaming_response.update(
            team_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            team = await response.parse()
            assert_matches_type(UpdateTeamResponse, team, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncStructify) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `team_id` but received ''"):
            await async_client.teams.with_raw_response.update(
                team_id="",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncStructify) -> None:
        team = await async_client.teams.list()
        assert_matches_type(ListTeamsResponse, team, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncStructify) -> None:
        response = await async_client.teams.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        team = await response.parse()
        assert_matches_type(ListTeamsResponse, team, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncStructify) -> None:
        async with async_client.teams.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            team = await response.parse()
            assert_matches_type(ListTeamsResponse, team, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncStructify) -> None:
        team = await async_client.teams.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(DeleteTeamResponse, team, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncStructify) -> None:
        response = await async_client.teams.with_raw_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        team = await response.parse()
        assert_matches_type(DeleteTeamResponse, team, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncStructify) -> None:
        async with async_client.teams.with_streaming_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            team = await response.parse()
            assert_matches_type(DeleteTeamResponse, team, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncStructify) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `team_id` but received ''"):
            await async_client.teams.with_raw_response.delete(
                "",
            )

    @parametrize
    async def test_method_add_member(self, async_client: AsyncStructify) -> None:
        team = await async_client.teams.add_member(
            team_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            role="member",
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(AddMemberResponse, team, path=["response"])

    @parametrize
    async def test_raw_response_add_member(self, async_client: AsyncStructify) -> None:
        response = await async_client.teams.with_raw_response.add_member(
            team_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            role="member",
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        team = await response.parse()
        assert_matches_type(AddMemberResponse, team, path=["response"])

    @parametrize
    async def test_streaming_response_add_member(self, async_client: AsyncStructify) -> None:
        async with async_client.teams.with_streaming_response.add_member(
            team_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            role="member",
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            team = await response.parse()
            assert_matches_type(AddMemberResponse, team, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_add_member(self, async_client: AsyncStructify) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `team_id` but received ''"):
            await async_client.teams.with_raw_response.add_member(
                team_id="",
                role="member",
                user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @parametrize
    async def test_method_create_project(self, async_client: AsyncStructify) -> None:
        team = await async_client.teams.create_project(
            team_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            name="name",
        )
        assert_matches_type(CreateProjectResponse, team, path=["response"])

    @parametrize
    async def test_method_create_project_with_all_params(self, async_client: AsyncStructify) -> None:
        team = await async_client.teams.create_project(
            team_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            name="name",
            description="description",
        )
        assert_matches_type(CreateProjectResponse, team, path=["response"])

    @parametrize
    async def test_raw_response_create_project(self, async_client: AsyncStructify) -> None:
        response = await async_client.teams.with_raw_response.create_project(
            team_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        team = await response.parse()
        assert_matches_type(CreateProjectResponse, team, path=["response"])

    @parametrize
    async def test_streaming_response_create_project(self, async_client: AsyncStructify) -> None:
        async with async_client.teams.with_streaming_response.create_project(
            team_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            team = await response.parse()
            assert_matches_type(CreateProjectResponse, team, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create_project(self, async_client: AsyncStructify) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `team_id` but received ''"):
            await async_client.teams.with_raw_response.create_project(
                team_id="",
                name="name",
            )

    @parametrize
    async def test_method_get(self, async_client: AsyncStructify) -> None:
        team = await async_client.teams.get(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(GetTeamResponse, team, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncStructify) -> None:
        response = await async_client.teams.with_raw_response.get(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        team = await response.parse()
        assert_matches_type(GetTeamResponse, team, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncStructify) -> None:
        async with async_client.teams.with_streaming_response.get(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            team = await response.parse()
            assert_matches_type(GetTeamResponse, team, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncStructify) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `team_id` but received ''"):
            await async_client.teams.with_raw_response.get(
                "",
            )

    @parametrize
    async def test_method_list_members(self, async_client: AsyncStructify) -> None:
        team = await async_client.teams.list_members(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ListMembersResponse, team, path=["response"])

    @parametrize
    async def test_raw_response_list_members(self, async_client: AsyncStructify) -> None:
        response = await async_client.teams.with_raw_response.list_members(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        team = await response.parse()
        assert_matches_type(ListMembersResponse, team, path=["response"])

    @parametrize
    async def test_streaming_response_list_members(self, async_client: AsyncStructify) -> None:
        async with async_client.teams.with_streaming_response.list_members(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            team = await response.parse()
            assert_matches_type(ListMembersResponse, team, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list_members(self, async_client: AsyncStructify) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `team_id` but received ''"):
            await async_client.teams.with_raw_response.list_members(
                "",
            )

    @parametrize
    async def test_method_list_projects(self, async_client: AsyncStructify) -> None:
        team = await async_client.teams.list_projects(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ListProjectsResponse, team, path=["response"])

    @parametrize
    async def test_raw_response_list_projects(self, async_client: AsyncStructify) -> None:
        response = await async_client.teams.with_raw_response.list_projects(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        team = await response.parse()
        assert_matches_type(ListProjectsResponse, team, path=["response"])

    @parametrize
    async def test_streaming_response_list_projects(self, async_client: AsyncStructify) -> None:
        async with async_client.teams.with_streaming_response.list_projects(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            team = await response.parse()
            assert_matches_type(ListProjectsResponse, team, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list_projects(self, async_client: AsyncStructify) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `team_id` but received ''"):
            await async_client.teams.with_raw_response.list_projects(
                "",
            )

    @parametrize
    async def test_method_remove_member(self, async_client: AsyncStructify) -> None:
        team = await async_client.teams.remove_member(
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            team_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(RemoveMemberResponse, team, path=["response"])

    @parametrize
    async def test_raw_response_remove_member(self, async_client: AsyncStructify) -> None:
        response = await async_client.teams.with_raw_response.remove_member(
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            team_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        team = await response.parse()
        assert_matches_type(RemoveMemberResponse, team, path=["response"])

    @parametrize
    async def test_streaming_response_remove_member(self, async_client: AsyncStructify) -> None:
        async with async_client.teams.with_streaming_response.remove_member(
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            team_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            team = await response.parse()
            assert_matches_type(RemoveMemberResponse, team, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_remove_member(self, async_client: AsyncStructify) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `team_id` but received ''"):
            await async_client.teams.with_raw_response.remove_member(
                user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                team_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            await async_client.teams.with_raw_response.remove_member(
                user_id="",
                team_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )
