# User

Types:

```python
from structify.types import (
    SurveySubmissionRequest,
    SurveySubmissionResponse,
    TokenResponse,
    UpdateUserParams,
    UserInfo,
    UserTransactionsResponse,
    UserUsageResponse,
)
```

Methods:

- <code title="put /user/update">client.user.<a href="./src/structify/resources/user/user.py">update</a>(\*\*<a href="src/structify/types/user_update_params.py">params</a>) -> <a href="./src/structify/types/admin/user.py">User</a></code>
- <code title="get /user/info">client.user.<a href="./src/structify/resources/user/user.py">info</a>() -> <a href="./src/structify/types/user_info.py">UserInfo</a></code>
- <code title="post /user/survey/submit">client.user.<a href="./src/structify/resources/user/user.py">survey_submit</a>(\*\*<a href="src/structify/types/user_survey_submit_params.py">params</a>) -> <a href="./src/structify/types/survey_submission_response.py">SurveySubmissionResponse</a></code>
- <code title="get /user/transactions/list">client.user.<a href="./src/structify/resources/user/user.py">transactions</a>() -> <a href="./src/structify/types/user_transactions_response.py">UserTransactionsResponse</a></code>
- <code title="get /user/usage">client.user.<a href="./src/structify/resources/user/user.py">usage</a>(\*\*<a href="src/structify/types/user_usage_params.py">params</a>) -> <a href="./src/structify/types/user_usage_response.py">UserUsageResponse</a></code>

## Stripe

Types:

```python
from structify.types.user import (
    CreatePortalRequest,
    CreateSessionRequest,
    CreateSessionResponse,
    CreateSubscriptionRequest,
    SubscriptionPlan,
)
```

Methods:

- <code title="post /user/transactions/stripe/create_portal_session">client.user.stripe.<a href="./src/structify/resources/user/stripe.py">create_portal_session</a>(\*\*<a href="src/structify/types/user/stripe_create_portal_session_params.py">params</a>) -> <a href="./src/structify/types/user/create_session_response.py">CreateSessionResponse</a></code>
- <code title="post /user/transactions/stripe/create_session">client.user.stripe.<a href="./src/structify/resources/user/stripe.py">create_session</a>(\*\*<a href="src/structify/types/user/stripe_create_session_params.py">params</a>) -> <a href="./src/structify/types/user/create_session_response.py">CreateSessionResponse</a></code>
- <code title="post /user/transactions/stripe/create_subscription">client.user.stripe.<a href="./src/structify/resources/user/stripe.py">create_subscription</a>(\*\*<a href="src/structify/types/user/stripe_create_subscription_params.py">params</a>) -> <a href="./src/structify/types/user/create_session_response.py">CreateSessionResponse</a></code>

# Chat

Types:

```python
from structify.types import (
    AddChatMessageRequest,
    AddChatMessageResponse,
    AddCollaboratorRequest,
    ChatEvent,
    ChatSession,
    ChatSessionRole,
    ChatSessionUser,
    ChatSessionWithMessages,
    CopyChatSessionRequest,
    CreateChatSessionRequest,
    CreateChatSessionResponse,
    DeleteChatSessionResponse,
    ErrorResponse,
    GetChatSessionResponse,
    ListChatSessionsResponse,
    ListCollaboratorsResponse,
    Message,
    TogglePublicRequest,
    TogglePublicResponse,
    ChatAddGitCommitResponse,
    ChatCopyNodeOutputByCodeHashResponse,
    ChatDeleteFilesResponse,
    ChatGetGitCommitResponse,
    ChatGetSessionTimelineResponse,
    ChatLoadFilesResponse,
    ChatRevertToCommitResponse,
)
```

Methods:

- <code title="post /chat/sessions/{chat_id}/collaborators">client.chat.<a href="./src/structify/resources/chat.py">add_collaborator</a>(chat_id, \*\*<a href="src/structify/types/chat_add_collaborator_params.py">params</a>) -> None</code>
- <code title="post /chat/sessions/{session_id}/commits">client.chat.<a href="./src/structify/resources/chat.py">add_git_commit</a>(session_id, \*\*<a href="src/structify/types/chat_add_git_commit_params.py">params</a>) -> <a href="./src/structify/types/chat_add_git_commit_response.py">ChatAddGitCommitResponse</a></code>
- <code title="post /chat/sessions/{session_id}/messages">client.chat.<a href="./src/structify/resources/chat.py">add_message</a>(session_id, \*\*<a href="src/structify/types/chat_add_message_params.py">params</a>) -> <a href="./src/structify/types/add_chat_message_response.py">AddChatMessageResponse</a></code>
- <code title="post /chat/copy">client.chat.<a href="./src/structify/resources/chat.py">copy</a>(\*\*<a href="src/structify/types/chat_copy_params.py">params</a>) -> <a href="./src/structify/types/chat_session_with_messages.py">ChatSessionWithMessages</a></code>
- <code title="post /chat/sessions/{session_id}/nodes/by_code_hash">client.chat.<a href="./src/structify/resources/chat.py">copy_node_output_by_code_hash</a>(session_id, \*\*<a href="src/structify/types/chat_copy_node_output_by_code_hash_params.py">params</a>) -> str</code>
- <code title="post /chat/sessions">client.chat.<a href="./src/structify/resources/chat.py">create_session</a>(\*\*<a href="src/structify/types/chat_create_session_params.py">params</a>) -> <a href="./src/structify/types/create_chat_session_response.py">CreateChatSessionResponse</a></code>
- <code title="post /chat/files/delete/{chat_id}">client.chat.<a href="./src/structify/resources/chat.py">delete_files</a>(chat_id, \*\*<a href="src/structify/types/chat_delete_files_params.py">params</a>) -> <a href="./src/structify/types/chat_delete_files_response.py">ChatDeleteFilesResponse</a></code>
- <code title="delete /chat/sessions/{session_id}">client.chat.<a href="./src/structify/resources/chat.py">delete_session</a>(session_id) -> <a href="./src/structify/types/delete_chat_session_response.py">DeleteChatSessionResponse</a></code>
- <code title="get /chat/sessions/{chat_id}/commits/{commit_hash}">client.chat.<a href="./src/structify/resources/chat.py">get_git_commit</a>(commit_hash, \*, chat_id) -> <a href="./src/structify/types/chat_get_git_commit_response.py">ChatGetGitCommitResponse</a></code>
- <code title="get /chat/sessions/{session_id}">client.chat.<a href="./src/structify/resources/chat.py">get_session</a>(session_id) -> <a href="./src/structify/types/get_chat_session_response.py">GetChatSessionResponse</a></code>
- <code title="get /chat/sessions/{session_id}/timeline">client.chat.<a href="./src/structify/resources/chat.py">get_session_timeline</a>(session_id) -> <a href="./src/structify/types/chat_get_session_timeline_response.py">ChatGetSessionTimelineResponse</a></code>
- <code title="get /chat/sessions/{chat_id}/collaborators">client.chat.<a href="./src/structify/resources/chat.py">list_collaborators</a>(chat_id) -> <a href="./src/structify/types/list_collaborators_response.py">ListCollaboratorsResponse</a></code>
- <code title="get /chat/sessions">client.chat.<a href="./src/structify/resources/chat.py">list_sessions</a>(\*\*<a href="src/structify/types/chat_list_sessions_params.py">params</a>) -> <a href="./src/structify/types/list_chat_sessions_response.py">ListChatSessionsResponse</a></code>
- <code title="post /chat/files/load">client.chat.<a href="./src/structify/resources/chat.py">load_files</a>(\*\*<a href="src/structify/types/chat_load_files_params.py">params</a>) -> <a href="./src/structify/types/chat_load_files_response.py">ChatLoadFilesResponse</a></code>
- <code title="patch /chat/sessions/{session_id}/make-permanent">client.chat.<a href="./src/structify/resources/chat.py">make_permanent</a>(session_id) -> None</code>
- <code title="delete /chat/sessions/{chat_id}/collaborators/{user_id}">client.chat.<a href="./src/structify/resources/chat.py">remove_collaborator</a>(user_id, \*, chat_id) -> None</code>
- <code title="post /chat/sessions/{session_id}/revert">client.chat.<a href="./src/structify/resources/chat.py">revert_to_commit</a>(session_id, \*\*<a href="src/structify/types/chat_revert_to_commit_params.py">params</a>) -> <a href="./src/structify/types/chat_revert_to_commit_response.py">ChatRevertToCommitResponse</a></code>
- <code title="put /chat/sessions/{session_id}/public">client.chat.<a href="./src/structify/resources/chat.py">toggle_public</a>(session_id, \*\*<a href="src/structify/types/chat_toggle_public_params.py">params</a>) -> <a href="./src/structify/types/toggle_public_response.py">TogglePublicResponse</a></code>
- <code title="patch /chat/sessions/{session_id}">client.chat.<a href="./src/structify/resources/chat.py">update_session</a>(session_id, \*\*<a href="src/structify/types/chat_update_session_params.py">params</a>) -> <a href="./src/structify/types/chat_session.py">ChatSession</a></code>

# Teams

Types:

```python
from structify.types import (
    AcceptInvitationRequest,
    AcceptInvitationResponse,
    AddMemberRequest,
    AddMemberResponse,
    CreateProjectRequest,
    CreateProjectResponse,
    CreateTeamRequest,
    CreateTeamResponse,
    CreditsUsageRequest,
    CreditsUsageResponse,
    CreditsUsageTimeseriesPoint,
    DeleteTeamResponse,
    GetTeamResponse,
    Granularity,
    ListMembersResponse,
    ListProjectsResponse,
    ListTeamsResponse,
    RemoveMemberResponse,
    Team,
    TeamRole,
    TeamSubscriptionStatus,
    TeamWithRole,
    UpdateTeamRequest,
    UpdateTeamResponse,
    UsageGroupKey,
    UserTeam,
)
```

Methods:

- <code title="post /team/create">client.teams.<a href="./src/structify/resources/teams.py">create</a>(\*\*<a href="src/structify/types/team_create_params.py">params</a>) -> <a href="./src/structify/types/create_team_response.py">CreateTeamResponse</a></code>
- <code title="put /team/{team_id}">client.teams.<a href="./src/structify/resources/teams.py">update</a>(team_id, \*\*<a href="src/structify/types/team_update_params.py">params</a>) -> <a href="./src/structify/types/update_team_response.py">UpdateTeamResponse</a></code>
- <code title="get /team/list">client.teams.<a href="./src/structify/resources/teams.py">list</a>() -> <a href="./src/structify/types/list_teams_response.py">ListTeamsResponse</a></code>
- <code title="delete /team/{team_id}">client.teams.<a href="./src/structify/resources/teams.py">delete</a>(team_id) -> <a href="./src/structify/types/delete_team_response.py">DeleteTeamResponse</a></code>
- <code title="post /team/invitations/accept">client.teams.<a href="./src/structify/resources/teams.py">accept_invitation</a>(\*\*<a href="src/structify/types/team_accept_invitation_params.py">params</a>) -> <a href="./src/structify/types/accept_invitation_response.py">AcceptInvitationResponse</a></code>
- <code title="post /team/{team_id}/members">client.teams.<a href="./src/structify/resources/teams.py">add_member</a>(team_id, \*\*<a href="src/structify/types/team_add_member_params.py">params</a>) -> <a href="./src/structify/types/add_member_response.py">AddMemberResponse</a></code>
- <code title="post /team/{team_id}/projects">client.teams.<a href="./src/structify/resources/teams.py">create_project</a>(team_id, \*\*<a href="src/structify/types/team_create_project_params.py">params</a>) -> <a href="./src/structify/types/create_project_response.py">CreateProjectResponse</a></code>
- <code title="get /team/{team_id}/credits/usage">client.teams.<a href="./src/structify/resources/teams.py">credits_usage</a>(team_id, \*\*<a href="src/structify/types/team_credits_usage_params.py">params</a>) -> <a href="./src/structify/types/credits_usage_response.py">CreditsUsageResponse</a></code>
- <code title="get /team/{team_id}">client.teams.<a href="./src/structify/resources/teams.py">get</a>(team_id) -> <a href="./src/structify/types/get_team_response.py">GetTeamResponse</a></code>
- <code title="get /team/{team_id}/members">client.teams.<a href="./src/structify/resources/teams.py">list_members</a>(team_id) -> <a href="./src/structify/types/list_members_response.py">ListMembersResponse</a></code>
- <code title="get /team/{team_id}/projects">client.teams.<a href="./src/structify/resources/teams.py">list_projects</a>(team_id) -> <a href="./src/structify/types/list_projects_response.py">ListProjectsResponse</a></code>
- <code title="delete /team/{team_id}/members/{user_id}">client.teams.<a href="./src/structify/resources/teams.py">remove_member</a>(user_id, \*, team_id) -> <a href="./src/structify/types/remove_member_response.py">RemoveMemberResponse</a></code>

# Projects

Types:

```python
from structify.types import DeleteProjectResponse, GetProjectResponse, Project
```

Methods:

- <code title="delete /team/{team_id}/project/{project_id}">client.projects.<a href="./src/structify/resources/projects.py">delete</a>(project_id, \*, team_id) -> <a href="./src/structify/types/delete_project_response.py">DeleteProjectResponse</a></code>
- <code title="get /team/{team_id}/project/{project_id}">client.projects.<a href="./src/structify/resources/projects.py">get</a>(project_id, \*, team_id) -> <a href="./src/structify/types/get_project_response.py">GetProjectResponse</a></code>

# Admin

## Teams

Types:

```python
from structify.types.admin import AdminTeamsListResponse, TeamListResponse
```

Methods:

- <code title="get /admin/teams/list">client.admin.teams.<a href="./src/structify/resources/admin/teams.py">list</a>() -> <a href="./src/structify/types/admin/team_list_response.py">TeamListResponse</a></code>

## Dataset

Types:

```python
from structify.types.admin import AdminDatasetReturn
```

Methods:

- <code title="get /admin/dataset/get_by_id">client.admin.dataset.<a href="./src/structify/resources/admin/dataset.py">get_by_id</a>(\*\*<a href="src/structify/types/admin/dataset_get_by_id_params.py">params</a>) -> <a href="./src/structify/types/admin/admin_dataset_return.py">AdminDatasetReturn</a></code>

## Jobs

Types:

```python
from structify.types.admin import AdminListJobsRequestParams, AdminListJobsResponse
```

Methods:

- <code title="get /admin/jobs/list">client.admin.jobs.<a href="./src/structify/resources/admin/jobs.py">list</a>(\*\*<a href="src/structify/types/admin/job_list_params.py">params</a>) -> <a href="./src/structify/types/admin/admin_list_jobs_response.py">SyncJobsList[AdminListJobsResponse]</a></code>

## HumanLlm

Types:

```python
from structify.types.admin import (
    HumanLlmJob,
    StepChoices,
    HumanLlmGetJobsResponse,
    HumanLlmGetNextStepResponse,
    HumanLlmPrelabelStepResponse,
)
```

Methods:

- <code title="post /admin/human_llm/add_search_for_job">client.admin.human_llm.<a href="./src/structify/resources/admin/human_llm.py">add_search_for_job</a>(\*\*<a href="src/structify/types/admin/human_llm_add_search_for_job_params.py">params</a>) -> <a href="./src/structify/types/admin/step_choices.py">StepChoices</a></code>
- <code title="post /admin/human_llm/add_to_dataset">client.admin.human_llm.<a href="./src/structify/resources/admin/human_llm.py">add_to_dataset</a>(\*\*<a href="src/structify/types/admin/human_llm_add_to_dataset_params.py">params</a>) -> object</code>
- <code title="post /admin/human_llm/finish_job">client.admin.human_llm.<a href="./src/structify/resources/admin/human_llm.py">finish_job</a>(\*\*<a href="src/structify/types/admin/human_llm_finish_job_params.py">params</a>) -> object</code>
- <code title="post /admin/human_llm/get_jobs">client.admin.human_llm.<a href="./src/structify/resources/admin/human_llm.py">get_jobs</a>(\*\*<a href="src/structify/types/admin/human_llm_get_jobs_params.py">params</a>) -> <a href="./src/structify/types/admin/human_llm_get_jobs_response.py">HumanLlmGetJobsResponse</a></code>
- <code title="post /admin/human_llm/get_next_step">client.admin.human_llm.<a href="./src/structify/resources/admin/human_llm.py">get_next_step</a>(\*\*<a href="src/structify/types/admin/human_llm_get_next_step_params.py">params</a>) -> <a href="./src/structify/types/admin/human_llm_get_next_step_response.py">HumanLlmGetNextStepResponse</a></code>
- <code title="post /admin/human_llm/prelabel_step/{step_id}">client.admin.human_llm.<a href="./src/structify/resources/admin/human_llm.py">prelabel_step</a>(step_id) -> <a href="./src/structify/types/admin/human_llm_prelabel_step_response.py">HumanLlmPrelabelStepResponse</a></code>
- <code title="post /admin/human_llm/start_next_job">client.admin.human_llm.<a href="./src/structify/resources/admin/human_llm.py">start_next_job</a>(\*\*<a href="src/structify/types/admin/human_llm_start_next_job_params.py">params</a>) -> <a href="./src/structify/types/admin/step_choices.py">StepChoices</a></code>
- <code title="post /admin/human_llm/update_step">client.admin.human_llm.<a href="./src/structify/resources/admin/human_llm.py">update_step</a>(\*\*<a href="src/structify/types/admin/human_llm_update_step_params.py">params</a>) -> <a href="./src/structify/types/admin/step_choices.py">StepChoices</a></code>

## NextAction

Types:

```python
from structify.types.admin import (
    ActionTrainingDataEntry,
    ActionTrainingDataResponse,
    AddActionTrainingDatumRequest,
    DeleteActionTrainingDataParams,
    DeleteActionTrainingDataResponse,
    GetActionTrainingDataParams,
    GetBatchedActionTrainingDataRequest,
    LabelActionTrainingDatumRequest,
)
```

Methods:

- <code title="post /admin/next_action/add_action_training_datum">client.admin.next_action.<a href="./src/structify/resources/admin/next_action.py">add_training_datum</a>(\*\*<a href="src/structify/types/admin/next_action_add_training_datum_params.py">params</a>) -> None</code>
- <code title="delete /admin/next_action/delete_action_training_data">client.admin.next_action.<a href="./src/structify/resources/admin/next_action.py">delete_training_data</a>(\*\*<a href="src/structify/types/admin/next_action_delete_training_data_params.py">params</a>) -> <a href="./src/structify/types/admin/delete_action_training_data_response.py">DeleteActionTrainingDataResponse</a></code>
- <code title="post /admin/next_action/get_batched_action_training_data">client.admin.next_action.<a href="./src/structify/resources/admin/next_action.py">get_batched_training_data</a>(\*\*<a href="src/structify/types/admin/next_action_get_batched_training_data_params.py">params</a>) -> <a href="./src/structify/types/admin/action_training_data_response.py">ActionTrainingDataResponse</a></code>
- <code title="get /admin/next_action/get_action_training_data">client.admin.next_action.<a href="./src/structify/resources/admin/next_action.py">get_training_data</a>(\*\*<a href="src/structify/types/admin/next_action_get_training_data_params.py">params</a>) -> <a href="./src/structify/types/admin/action_training_data_response.py">ActionTrainingDataResponse</a></code>
- <code title="get /admin/next_action/get_action_training_datum">client.admin.next_action.<a href="./src/structify/resources/admin/next_action.py">get_training_datum</a>(\*\*<a href="src/structify/types/admin/next_action_get_training_datum_params.py">params</a>) -> <a href="./src/structify/types/admin/action_training_data_entry.py">ActionTrainingDataEntry</a></code>
- <code title="put /admin/next_action/label_action_training_datum">client.admin.next_action.<a href="./src/structify/resources/admin/next_action.py">label_training_datum</a>(\*\*<a href="src/structify/types/admin/next_action_label_training_datum_params.py">params</a>) -> None</code>

## Users

Types:

```python
from structify.types.admin import (
    User,
    UserListResponse,
    UserGetCreditsResponse,
    UserGetStatsResponse,
    UserSetCreditsResponse,
)
```

Methods:

- <code title="post /admin/users/create">client.admin.users.<a href="./src/structify/resources/admin/users.py">create</a>(\*\*<a href="src/structify/types/admin/user_create_params.py">params</a>) -> <a href="./src/structify/types/token_response.py">TokenResponse</a></code>
- <code title="get /admin/users/list">client.admin.users.<a href="./src/structify/resources/admin/users.py">list</a>() -> <a href="./src/structify/types/admin/user_list_response.py">UserListResponse</a></code>
- <code title="post /admin/users/get_credits">client.admin.users.<a href="./src/structify/resources/admin/users.py">get_credits</a>(\*\*<a href="src/structify/types/admin/user_get_credits_params.py">params</a>) -> <a href="./src/structify/types/admin/user_get_credits_response.py">UserGetCreditsResponse</a></code>
- <code title="post /admin/users/get_stats">client.admin.users.<a href="./src/structify/resources/admin/users.py">get_stats</a>(\*\*<a href="src/structify/types/admin/user_get_stats_params.py">params</a>) -> <a href="./src/structify/types/admin/user_get_stats_response.py">UserGetStatsResponse</a></code>
- <code title="post /admin/users/set_credits">client.admin.users.<a href="./src/structify/resources/admin/users.py">set_credits</a>(\*\*<a href="src/structify/types/admin/user_set_credits_params.py">params</a>) -> <a href="./src/structify/types/admin/user_set_credits_response.py">UserSetCreditsResponse</a></code>

## TrainingDatasets

Types:

```python
from structify.types.admin import (
    AddDatumRequest,
    DatumStatus,
    LabelingStats,
    TrainingDatumResponse,
    UpdateDatumStatusRequest,
    TrainingDatasetListResponse,
    TrainingDatasetGetLabellerStatsResponse,
    TrainingDatasetListDatumsResponse,
    TrainingDatasetSizeResponse,
    TrainingDatasetSuspiciousCountResponse,
)
```

Methods:

- <code title="get /admin/training_datasets/list">client.admin.training_datasets.<a href="./src/structify/resources/admin/training_datasets.py">list</a>() -> <a href="./src/structify/types/admin/training_dataset_list_response.py">TrainingDatasetListResponse</a></code>
- <code title="delete /admin/training_datasets/delete_dataset">client.admin.training_datasets.<a href="./src/structify/resources/admin/training_datasets.py">delete</a>(\*\*<a href="src/structify/types/admin/training_dataset_delete_params.py">params</a>) -> None</code>
- <code title="post /admin/training_datasets/add_dataset">client.admin.training_datasets.<a href="./src/structify/resources/admin/training_datasets.py">add</a>(\*\*<a href="src/structify/types/admin/training_dataset_add_params.py">params</a>) -> None</code>
- <code title="post /admin/training_datasets/add_datum">client.admin.training_datasets.<a href="./src/structify/resources/admin/training_datasets.py">add_datum</a>(\*\*<a href="src/structify/types/admin/training_dataset_add_datum_params.py">params</a>) -> None</code>
- <code title="get /admin/training_datasets/download_datum_step">client.admin.training_datasets.<a href="./src/structify/resources/admin/training_datasets.py">download_datum</a>(\*\*<a href="src/structify/types/admin/training_dataset_download_datum_params.py">params</a>) -> BinaryAPIResponse</code>
- <code title="get /admin/training_datasets/get_datum_info">client.admin.training_datasets.<a href="./src/structify/resources/admin/training_datasets.py">get_datum_info</a>(\*\*<a href="src/structify/types/admin/training_dataset_get_datum_info_params.py">params</a>) -> <a href="./src/structify/types/admin/training_datum_response.py">TrainingDatumResponse</a></code>
- <code title="get /admin/training_datasets/labeller_stats">client.admin.training_datasets.<a href="./src/structify/resources/admin/training_datasets.py">get_labeller_stats</a>(\*\*<a href="src/structify/types/admin/training_dataset_get_labeller_stats_params.py">params</a>) -> <a href="./src/structify/types/admin/training_dataset_get_labeller_stats_response.py">TrainingDatasetGetLabellerStatsResponse</a></code>
- <code title="get /admin/training_datasets/get_next_for_labeling">client.admin.training_datasets.<a href="./src/structify/resources/admin/training_datasets.py">get_next_for_labeling</a>(\*\*<a href="src/structify/types/admin/training_dataset_get_next_for_labeling_params.py">params</a>) -> <a href="./src/structify/types/admin/training_datum_response.py">Optional[TrainingDatumResponse]</a></code>
- <code title="get /admin/training_datasets/get_next_for_qa">client.admin.training_datasets.<a href="./src/structify/resources/admin/training_datasets.py">get_next_for_qa</a>(\*\*<a href="src/structify/types/admin/training_dataset_get_next_for_qa_params.py">params</a>) -> <a href="./src/structify/types/admin/training_datum_response.py">Optional[TrainingDatumResponse]</a></code>
- <code title="get /admin/training_datasets/get_next_suspicious">client.admin.training_datasets.<a href="./src/structify/resources/admin/training_datasets.py">get_next_suspicious</a>(\*\*<a href="src/structify/types/admin/training_dataset_get_next_suspicious_params.py">params</a>) -> <a href="./src/structify/types/admin/training_datum_response.py">Optional[TrainingDatumResponse]</a></code>
- <code title="put /admin/training_datasets/label_datum">client.admin.training_datasets.<a href="./src/structify/resources/admin/training_datasets.py">label_datum</a>(\*\*<a href="src/structify/types/admin/training_dataset_label_datum_params.py">params</a>) -> None</code>
- <code title="get /admin/training_datasets/list_datums">client.admin.training_datasets.<a href="./src/structify/resources/admin/training_datasets.py">list_datums</a>(\*\*<a href="src/structify/types/admin/training_dataset_list_datums_params.py">params</a>) -> <a href="./src/structify/types/admin/training_dataset_list_datums_response.py">TrainingDatasetListDatumsResponse</a></code>
- <code title="put /admin/training_datasets/mark_datum_suspicious">client.admin.training_datasets.<a href="./src/structify/resources/admin/training_datasets.py">mark_datum_suspicious</a>(\*\*<a href="src/structify/types/admin/training_dataset_mark_datum_suspicious_params.py">params</a>) -> None</code>
- <code title="delete /admin/training_datasets/remove_from_dataset">client.admin.training_datasets.<a href="./src/structify/resources/admin/training_datasets.py">remove_datum</a>(\*\*<a href="src/structify/types/admin/training_dataset_remove_datum_params.py">params</a>) -> None</code>
- <code title="post /admin/training_datasets/size">client.admin.training_datasets.<a href="./src/structify/resources/admin/training_datasets.py">size</a>(\*\*<a href="src/structify/types/admin/training_dataset_size_params.py">params</a>) -> <a href="./src/structify/types/admin/training_dataset_size_response.py">TrainingDatasetSizeResponse</a></code>
- <code title="get /admin/training_datasets/suspicious_count">client.admin.training_datasets.<a href="./src/structify/resources/admin/training_datasets.py">suspicious_count</a>(\*\*<a href="src/structify/types/admin/training_dataset_suspicious_count_params.py">params</a>) -> <a href="./src/structify/types/admin/training_dataset_suspicious_count_response.py">TrainingDatasetSuspiciousCountResponse</a></code>
- <code title="post /admin/training_datasets/switch_dataset">client.admin.training_datasets.<a href="./src/structify/resources/admin/training_datasets.py">switch_dataset</a>(\*\*<a href="src/structify/types/admin/training_dataset_switch_dataset_params.py">params</a>) -> None</code>
- <code title="post /admin/training_datasets/update_datum_status">client.admin.training_datasets.<a href="./src/structify/resources/admin/training_datasets.py">update_datum_status</a>(\*\*<a href="src/structify/types/admin/training_dataset_update_datum_status_params.py">params</a>) -> None</code>
- <code title="post /admin/training_datasets/upload_labeled_step">client.admin.training_datasets.<a href="./src/structify/resources/admin/training_datasets.py">upload_labeled_step</a>(\*\*<a href="src/structify/types/admin/training_dataset_upload_labeled_step_params.py">params</a>) -> None</code>
- <code title="put /admin/training_datasets/verify_datum">client.admin.training_datasets.<a href="./src/structify/resources/admin/training_datasets.py">verify_datum</a>(\*\*<a href="src/structify/types/admin/training_dataset_verify_datum_params.py">params</a>) -> None</code>

# Datasets

Types:

```python
from structify.types import (
    MergeConfig,
    RelationshipMergeStrategy,
    Strategy,
    DatasetCreateResponse,
    DatasetListResponse,
    DatasetEnrichmentProgressResponse,
    DatasetGetResponse,
    DatasetMatchResponse,
    DatasetViewRelationshipsResponse,
    DatasetViewTableResponse,
    DatasetViewTablesWithRelationshipsResponse,
)
```

Methods:

- <code title="post /dataset/create">client.datasets.<a href="./src/structify/resources/datasets/datasets.py">create</a>(\*\*<a href="src/structify/types/dataset_create_params.py">params</a>) -> str</code>
- <code title="get /dataset/list">client.datasets.<a href="./src/structify/resources/datasets/datasets.py">list</a>() -> <a href="./src/structify/types/dataset_list_response.py">DatasetListResponse</a></code>
- <code title="delete /dataset/delete">client.datasets.<a href="./src/structify/resources/datasets/datasets.py">delete</a>(\*\*<a href="src/structify/types/dataset_delete_params.py">params</a>) -> None</code>
- <code title="post /dataset/add_property">client.datasets.<a href="./src/structify/resources/datasets/datasets.py">add_property</a>(\*\*<a href="src/structify/types/dataset_add_property_params.py">params</a>) -> None</code>
- <code title="get /dataset/enrichment_progress">client.datasets.<a href="./src/structify/resources/datasets/datasets.py">enrichment_progress</a>(\*\*<a href="src/structify/types/dataset_enrichment_progress_params.py">params</a>) -> <a href="./src/structify/types/dataset_enrichment_progress_response.py">DatasetEnrichmentProgressResponse</a></code>
- <code title="get /dataset/export_to_csv">client.datasets.<a href="./src/structify/resources/datasets/datasets.py">export_to_csv</a>(\*\*<a href="src/structify/types/dataset_export_to_csv_params.py">params</a>) -> None</code>
- <code title="get /dataset/export_to_excel">client.datasets.<a href="./src/structify/resources/datasets/datasets.py">export_to_excel</a>(\*\*<a href="src/structify/types/dataset_export_to_excel_params.py">params</a>) -> None</code>
- <code title="get /dataset/info">client.datasets.<a href="./src/structify/resources/datasets/datasets.py">get</a>(\*\*<a href="src/structify/types/dataset_get_params.py">params</a>) -> <a href="./src/structify/types/dataset_get_response.py">DatasetGetResponse</a></code>
- <code title="post /dataset/match">client.datasets.<a href="./src/structify/resources/datasets/datasets.py">match</a>(\*\*<a href="src/structify/types/dataset_match_params.py">params</a>) -> <a href="./src/structify/types/dataset_match_response.py">DatasetMatchResponse</a></code>
- <code title="post /dataset/remove_property">client.datasets.<a href="./src/structify/resources/datasets/datasets.py">remove_property</a>(\*\*<a href="src/structify/types/dataset_remove_property_params.py">params</a>) -> None</code>
- <code title="post /dataset/reorder_properties">client.datasets.<a href="./src/structify/resources/datasets/datasets.py">reorder_properties</a>(\*\*<a href="src/structify/types/dataset_reorder_properties_params.py">params</a>) -> None</code>
- <code title="post /dataset/set_primary_column">client.datasets.<a href="./src/structify/resources/datasets/datasets.py">set_primary_column</a>(\*\*<a href="src/structify/types/dataset_set_primary_column_params.py">params</a>) -> None</code>
- <code title="post /dataset/update_property">client.datasets.<a href="./src/structify/resources/datasets/datasets.py">update_property</a>(\*\*<a href="src/structify/types/dataset_update_property_params.py">params</a>) -> None</code>
- <code title="post /dataset/update_relationship">client.datasets.<a href="./src/structify/resources/datasets/datasets.py">update_relationship</a>(\*\*<a href="src/structify/types/dataset_update_relationship_params.py">params</a>) -> None</code>
- <code title="get /dataset/view_relationships">client.datasets.<a href="./src/structify/resources/datasets/datasets.py">view_relationships</a>(\*\*<a href="src/structify/types/dataset_view_relationships_params.py">params</a>) -> <a href="./src/structify/types/dataset_view_relationships_response.py">SyncJobsList[DatasetViewRelationshipsResponse]</a></code>
- <code title="get /dataset/view_table">client.datasets.<a href="./src/structify/resources/datasets/datasets.py">view_table</a>(\*\*<a href="src/structify/types/dataset_view_table_params.py">params</a>) -> <a href="./src/structify/types/dataset_view_table_response.py">SyncJobsList[DatasetViewTableResponse]</a></code>
- <code title="get /dataset/view_tables_with_relationships">client.datasets.<a href="./src/structify/resources/datasets/datasets.py">view_tables_with_relationships</a>(\*\*<a href="src/structify/types/dataset_view_tables_with_relationships_params.py">params</a>) -> <a href="./src/structify/types/dataset_view_tables_with_relationships_response.py">DatasetViewTablesWithRelationshipsResponse</a></code>

## Evaluate

Types:

```python
from structify.types.datasets import (
    EvaluateListResponse,
    EvaluateGetResponse,
    EvaluateRunResponse,
    EvaluateStatusResponse,
)
```

Methods:

- <code title="get /dataset/evaluate/list">client.datasets.evaluate.<a href="./src/structify/resources/datasets/evaluate.py">list</a>(\*\*<a href="src/structify/types/datasets/evaluate_list_params.py">params</a>) -> <a href="./src/structify/types/datasets/evaluate_list_response.py">SyncJobsList[EvaluateListResponse]</a></code>
- <code title="delete /dataset/evaluate/delete">client.datasets.evaluate.<a href="./src/structify/resources/datasets/evaluate.py">delete</a>(\*\*<a href="src/structify/types/datasets/evaluate_delete_params.py">params</a>) -> None</code>
- <code title="get /dataset/evaluate/get">client.datasets.evaluate.<a href="./src/structify/resources/datasets/evaluate.py">get</a>(\*\*<a href="src/structify/types/datasets/evaluate_get_params.py">params</a>) -> <a href="./src/structify/types/datasets/evaluate_get_response.py">EvaluateGetResponse</a></code>
- <code title="post /dataset/evaluate/run">client.datasets.evaluate.<a href="./src/structify/resources/datasets/evaluate.py">run</a>(\*\*<a href="src/structify/types/datasets/evaluate_run_params.py">params</a>) -> str</code>
- <code title="get /dataset/evaluate/status">client.datasets.evaluate.<a href="./src/structify/resources/datasets/evaluate.py">status</a>(\*\*<a href="src/structify/types/datasets/evaluate_status_params.py">params</a>) -> <a href="./src/structify/types/datasets/evaluate_status_response.py">EvaluateStatusResponse</a></code>

# Documents

Types:

```python
from structify.types import (
    DocumentListResponse,
    DocumentDownloadResponse,
    DocumentStructureResponse,
)
```

Methods:

- <code title="get /documents/list">client.documents.<a href="./src/structify/resources/documents.py">list</a>(\*\*<a href="src/structify/types/document_list_params.py">params</a>) -> <a href="./src/structify/types/document_list_response.py">DocumentListResponse</a></code>
- <code title="delete /documents/delete">client.documents.<a href="./src/structify/resources/documents.py">delete</a>(\*\*<a href="src/structify/types/document_delete_params.py">params</a>) -> None</code>
- <code title="post /documents/download">client.documents.<a href="./src/structify/resources/documents.py">download</a>(\*\*<a href="src/structify/types/document_download_params.py">params</a>) -> <a href="./src/structify/types/document_download_response.py">DocumentDownloadResponse</a></code>
- <code title="post /documents/structure">client.documents.<a href="./src/structify/resources/documents.py">structure</a>(\*\*<a href="src/structify/types/document_structure_params.py">params</a>) -> <a href="./src/structify/types/document_structure_response.py">DocumentStructureResponse</a></code>
- <code title="post /documents/upload">client.documents.<a href="./src/structify/resources/documents.py">upload</a>(\*\*<a href="src/structify/types/document_upload_params.py">params</a>) -> None</code>

# Jobs

Types:

```python
from structify.types import (
    JobListResponse,
    JobDeleteResponse,
    JobCancelResponse,
    JobGetResponse,
    JobGetScrapersResponse,
    JobGetSourceEntitiesResponse,
    JobGetStepResponse,
    JobGetStepGraphResponse,
    JobGetStepsResponse,
    JobStatusResponse,
)
```

Methods:

- <code title="get /jobs/list">client.jobs.<a href="./src/structify/resources/jobs.py">list</a>(\*\*<a href="src/structify/types/job_list_params.py">params</a>) -> <a href="./src/structify/types/job_list_response.py">SyncJobsList[JobListResponse]</a></code>
- <code title="post /jobs/delete/{job_id}">client.jobs.<a href="./src/structify/resources/jobs.py">delete</a>(job_id) -> str</code>
- <code title="post /jobs/cancel/{uuid}">client.jobs.<a href="./src/structify/resources/jobs.py">cancel</a>(uuid) -> <a href="./src/structify/types/job_cancel_response.py">JobCancelResponse</a></code>
- <code title="get /jobs/get/{job_id}">client.jobs.<a href="./src/structify/resources/jobs.py">get</a>(job_id) -> <a href="./src/structify/types/job_get_response.py">JobGetResponse</a></code>
- <code title="get /jobs/get_scrapers/{job_id}">client.jobs.<a href="./src/structify/resources/jobs.py">get_scrapers</a>(job_id) -> <a href="./src/structify/types/job_get_scrapers_response.py">JobGetScrapersResponse</a></code>
- <code title="get /jobs/get_source_entities/{job_id}">client.jobs.<a href="./src/structify/resources/jobs.py">get_source_entities</a>(job_id) -> <a href="./src/structify/types/job_get_source_entities_response.py">JobGetSourceEntitiesResponse</a></code>
- <code title="get /jobs/get_step/{step_id}">client.jobs.<a href="./src/structify/resources/jobs.py">get_step</a>(step_id) -> <a href="./src/structify/types/job_get_step_response.py">JobGetStepResponse</a></code>
- <code title="get /jobs/get_step_graph/{job_id}">client.jobs.<a href="./src/structify/resources/jobs.py">get_step_graph</a>(job_id) -> <a href="./src/structify/types/job_get_step_graph_response.py">JobGetStepGraphResponse</a></code>
- <code title="get /jobs/get_steps/{job_id}">client.jobs.<a href="./src/structify/resources/jobs.py">get_steps</a>(job_id) -> <a href="./src/structify/types/job_get_steps_response.py">JobGetStepsResponse</a></code>
- <code title="post /jobs/schedule">client.jobs.<a href="./src/structify/resources/jobs.py">schedule</a>() -> None</code>
- <code title="post /jobs/status_aggregated">client.jobs.<a href="./src/structify/resources/jobs.py">status</a>(\*\*<a href="src/structify/types/job_status_params.py">params</a>) -> <a href="./src/structify/types/job_status_response.py">JobStatusResponse</a></code>

# Sessions

Types:

```python
from structify.types import (
    CreateWorkflowEdgeRequest,
    CreateWorkflowNodeRequest,
    CreateWorkflowSessionRequest,
    GetNodeLogsResponse,
    JobEventBody,
    MarkWorkflowSessionErroredRequest,
    UpdateWorkflowNodeProgressRequest,
    UpdateWorkflowNodeRequest,
    UploadNodeVisualizationOutputRequest,
    WorkflowDag,
    WorkflowNodeExecutionStatus,
    WorkflowNodeLog,
    WorkflowSession,
    WorkflowSessionEdge,
    WorkflowSessionNode,
    SessionGetEventsResponse,
    SessionGetNodeProgressResponse,
    SessionKillJobsResponse,
)
```

Methods:

- <code title="post /sessions/{session_id}/edges">client.sessions.<a href="./src/structify/resources/sessions.py">create_edge</a>(session_id, \*\*<a href="src/structify/types/session_create_edge_params.py">params</a>) -> <a href="./src/structify/types/workflow_session_edge.py">WorkflowSessionEdge</a></code>
- <code title="post /sessions/{session_id}/nodes">client.sessions.<a href="./src/structify/resources/sessions.py">create_node</a>(session_id, \*\*<a href="src/structify/types/session_create_node_params.py">params</a>) -> <a href="./src/structify/types/workflow_session_node.py">WorkflowSessionNode</a></code>
- <code title="post /sessions">client.sessions.<a href="./src/structify/resources/sessions.py">create_session</a>(\*\*<a href="src/structify/types/session_create_session_params.py">params</a>) -> <a href="./src/structify/types/workflow_session.py">WorkflowSession</a></code>
- <code title="post /sessions/{session_id}/dag_ready">client.sessions.<a href="./src/structify/resources/sessions.py">finalize_dag</a>(session_id) -> None</code>
- <code title="get /sessions/{session_id}/dag">client.sessions.<a href="./src/structify/resources/sessions.py">get_dag</a>(session_id) -> <a href="./src/structify/types/workflow_dag.py">WorkflowDag</a></code>
- <code title="get /sessions/nodes/{node_id}/events">client.sessions.<a href="./src/structify/resources/sessions.py">get_events</a>(node_id, \*\*<a href="src/structify/types/session_get_events_params.py">params</a>) -> <a href="./src/structify/types/session_get_events_response.py">SessionGetEventsResponse</a></code>
- <code title="get /sessions/node/{node_id}/logs">client.sessions.<a href="./src/structify/resources/sessions.py">get_node_logs</a>(node_id) -> <a href="./src/structify/types/get_node_logs_response.py">GetNodeLogsResponse</a></code>
- <code title="get /sessions/nodes/{node_id}/output_data">client.sessions.<a href="./src/structify/resources/sessions.py">get_node_output_data</a>(node_id) -> BinaryAPIResponse</code>
- <code title="get /sessions/nodes/{node_id}/progress">client.sessions.<a href="./src/structify/resources/sessions.py">get_node_progress</a>(node_id) -> <a href="./src/structify/types/session_get_node_progress_response.py">SessionGetNodeProgressResponse</a></code>
- <code title="post /sessions/{session_id}/kill_jobs">client.sessions.<a href="./src/structify/resources/sessions.py">kill_jobs</a>(session_id, \*\*<a href="src/structify/types/session_kill_jobs_params.py">params</a>) -> <a href="./src/structify/types/session_kill_jobs_response.py">SessionKillJobsResponse</a></code>
- <code title="patch /sessions/{session_id}/error">client.sessions.<a href="./src/structify/resources/sessions.py">mark_errored</a>(session_id, \*\*<a href="src/structify/types/session_mark_errored_params.py">params</a>) -> <a href="./src/structify/types/workflow_session.py">WorkflowSession</a></code>
- <code title="patch /sessions/nodes/{node_id}">client.sessions.<a href="./src/structify/resources/sessions.py">update_node</a>(node_id, \*\*<a href="src/structify/types/session_update_node_params.py">params</a>) -> <a href="./src/structify/types/workflow_session_node.py">WorkflowSessionNode</a></code>
- <code title="patch /sessions/nodes/{node_id}/progress">client.sessions.<a href="./src/structify/resources/sessions.py">update_node_progress</a>(node_id, \*\*<a href="src/structify/types/session_update_node_progress_params.py">params</a>) -> <a href="./src/structify/types/workflow_session_node.py">WorkflowSessionNode</a></code>
- <code title="post /sessions/nodes/{node_id}/output_data">client.sessions.<a href="./src/structify/resources/sessions.py">upload_node_output_data</a>(node_id, \*\*<a href="src/structify/types/session_upload_node_output_data_params.py">params</a>) -> <a href="./src/structify/types/workflow_session_node.py">WorkflowSessionNode</a></code>
- <code title="post /sessions/nodes/{node_id}/visualization_output">client.sessions.<a href="./src/structify/resources/sessions.py">upload_node_visualization_output</a>(node_id, \*\*<a href="src/structify/types/session_upload_node_visualization_output_params.py">params</a>) -> <a href="./src/structify/types/workflow_session_node.py">WorkflowSessionNode</a></code>

# WorkflowSchedule

Types:

```python
from structify.types import (
    CreateWorkflowScheduleRequest,
    GetWorkflowScheduleSessionsRequest,
    GetWorkflowScheduleSessionsResponse,
    UpdateWorkflowScheduleRequest,
    WorkflowScheduleInfo,
    WorkflowScheduleGetResponse,
    WorkflowScheduleGetAllResponse,
)
```

Methods:

- <code title="post /workflow-schedule/{chat_session_id}">client.workflow_schedule.<a href="./src/structify/resources/workflow_schedule.py">create</a>(chat_session_id, \*\*<a href="src/structify/types/workflow_schedule_create_params.py">params</a>) -> <a href="./src/structify/types/workflow_schedule_info.py">WorkflowScheduleInfo</a></code>
- <code title="put /workflow-schedule/{schedule_id}">client.workflow_schedule.<a href="./src/structify/resources/workflow_schedule.py">update</a>(schedule_id, \*\*<a href="src/structify/types/workflow_schedule_update_params.py">params</a>) -> <a href="./src/structify/types/workflow_schedule_info.py">WorkflowScheduleInfo</a></code>
- <code title="delete /workflow-schedule/{schedule_id}">client.workflow_schedule.<a href="./src/structify/resources/workflow_schedule.py">delete</a>(schedule_id) -> None</code>
- <code title="get /workflow-schedule/{chat_session_id}">client.workflow_schedule.<a href="./src/structify/resources/workflow_schedule.py">get</a>(chat_session_id) -> <a href="./src/structify/types/workflow_schedule_get_response.py">WorkflowScheduleGetResponse</a></code>
- <code title="get /workflow-schedule">client.workflow_schedule.<a href="./src/structify/resources/workflow_schedule.py">get_all</a>() -> <a href="./src/structify/types/workflow_schedule_get_all_response.py">WorkflowScheduleGetAllResponse</a></code>
- <code title="post /workflow-schedule/{schedule_id}/sessions">client.workflow_schedule.<a href="./src/structify/resources/workflow_schedule.py">get_sessions</a>(schedule_id, \*\*<a href="src/structify/types/workflow_schedule_get_sessions_params.py">params</a>) -> <a href="./src/structify/types/get_workflow_schedule_sessions_response.py">GetWorkflowScheduleSessionsResponse</a></code>

# Connectors

Types:

```python
from structify.types import (
    Connector,
    ConnectorWithSecrets,
    CreateConnectorRequest,
    CreateSecretRequest,
    UpdateConnectorRequest,
    ConnectorGetResponse,
)
```

Methods:

- <code title="post /connectors">client.connectors.<a href="./src/structify/resources/connectors.py">create</a>(\*\*<a href="src/structify/types/connector_create_params.py">params</a>) -> <a href="./src/structify/types/connector.py">Connector</a></code>
- <code title="patch /connectors/{connector_id}">client.connectors.<a href="./src/structify/resources/connectors.py">update</a>(connector_id, \*\*<a href="src/structify/types/connector_update_params.py">params</a>) -> None</code>
- <code title="get /connectors">client.connectors.<a href="./src/structify/resources/connectors.py">list</a>(\*\*<a href="src/structify/types/connector_list_params.py">params</a>) -> <a href="./src/structify/types/connector_with_secrets.py">SyncJobsList[ConnectorWithSecrets]</a></code>
- <code title="delete /connectors/{connector_id}">client.connectors.<a href="./src/structify/resources/connectors.py">delete</a>(connector_id) -> None</code>
- <code title="post /connectors/{connector_id}/secrets">client.connectors.<a href="./src/structify/resources/connectors.py">create_secret</a>(connector_id, \*\*<a href="src/structify/types/connector_create_secret_params.py">params</a>) -> None</code>
- <code title="delete /connectors/{connector_id}/secrets/{secret_name}">client.connectors.<a href="./src/structify/resources/connectors.py">delete_secret</a>(secret_name, \*, connector_id) -> None</code>
- <code title="get /connectors/{connector_id}">client.connectors.<a href="./src/structify/resources/connectors.py">get</a>(connector_id) -> <a href="./src/structify/types/connector_get_response.py">ConnectorGetResponse</a></code>

# Server

Types:

```python
from structify.types import ServerInformation
```

Methods:

- <code title="get /server/version">client.server.<a href="./src/structify/resources/server.py">version</a>() -> <a href="./src/structify/types/server_information.py">ServerInformation</a></code>

# Sources

Types:

```python
from structify.types import (
    DeleteSourceEntityParams,
    DeleteSourceEntityResponse,
    DeleteSourceRelationshipParams,
    DeleteSourceRelationshipResponse,
    Source,
    SourceListResponse,
)
```

Methods:

- <code title="get /source/get_sources">client.sources.<a href="./src/structify/resources/sources.py">list</a>(\*\*<a href="src/structify/types/source_list_params.py">params</a>) -> <a href="./src/structify/types/source_list_response.py">SourceListResponse</a></code>
- <code title="delete /source/entity">client.sources.<a href="./src/structify/resources/sources.py">delete_entity</a>(\*\*<a href="src/structify/types/source_delete_entity_params.py">params</a>) -> <a href="./src/structify/types/delete_source_entity_response.py">DeleteSourceEntityResponse</a></code>
- <code title="delete /source/relationship">client.sources.<a href="./src/structify/resources/sources.py">delete_relationship</a>(\*\*<a href="src/structify/types/source_delete_relationship_params.py">params</a>) -> <a href="./src/structify/types/delete_source_relationship_response.py">DeleteSourceRelationshipResponse</a></code>

# Entities

Types:

```python
from structify.types import (
    EntityDeleteResponse,
    EntityAddResponse,
    EntityAddBatchResponse,
    EntityAddRelationshipResponse,
    EntityAgentMergeResponse,
    EntityDeriveResponse,
    EntityGetResponse,
    EntityGetLocalSubgraphResponse,
    EntityGetMergesResponse,
    EntityGetSourceEntitiesResponse,
    EntityListJobsResponse,
    EntityMergeResponse,
    EntitySearchResponse,
    EntitySummarizeResponse,
    EntityTriggerMergeResponse,
    EntityUpdatePropertyResponse,
    EntityViewResponse,
)
```

Methods:

- <code title="delete /entity/delete">client.entities.<a href="./src/structify/resources/entities.py">delete</a>(\*\*<a href="src/structify/types/entity_delete_params.py">params</a>) -> <a href="./src/structify/types/entity_delete_response.py">EntityDeleteResponse</a></code>
- <code title="post /entity/add">client.entities.<a href="./src/structify/resources/entities.py">add</a>(\*\*<a href="src/structify/types/entity_add_params.py">params</a>) -> <a href="./src/structify/types/entity_add_response.py">EntityAddResponse</a></code>
- <code title="post /entity/add_batch">client.entities.<a href="./src/structify/resources/entities.py">add_batch</a>(\*\*<a href="src/structify/types/entity_add_batch_params.py">params</a>) -> <a href="./src/structify/types/entity_add_batch_response.py">EntityAddBatchResponse</a></code>
- <code title="post /entity/add_relationship">client.entities.<a href="./src/structify/resources/entities.py">add_relationship</a>(\*\*<a href="src/structify/types/entity_add_relationship_params.py">params</a>) -> <a href="./src/structify/types/entity_add_relationship_response.py">EntityAddRelationshipResponse</a></code>
- <code title="post /entity/agent_merge">client.entities.<a href="./src/structify/resources/entities.py">agent_merge</a>(\*\*<a href="src/structify/types/entity_agent_merge_params.py">params</a>) -> <a href="./src/structify/types/entity_agent_merge_response.py">EntityAgentMergeResponse</a></code>
- <code title="post /entity/delete_relationship">client.entities.<a href="./src/structify/resources/entities.py">delete_relationship</a>(\*\*<a href="src/structify/types/entity_delete_relationship_params.py">params</a>) -> object</code>
- <code title="post /entity/derive">client.entities.<a href="./src/structify/resources/entities.py">derive</a>(\*\*<a href="src/structify/types/entity_derive_params.py">params</a>) -> str</code>
- <code title="get /entity/get">client.entities.<a href="./src/structify/resources/entities.py">get</a>(\*\*<a href="src/structify/types/entity_get_params.py">params</a>) -> <a href="./src/structify/types/entity_get_response.py">EntityGetResponse</a></code>
- <code title="get /entity/get_local_subgraph">client.entities.<a href="./src/structify/resources/entities.py">get_local_subgraph</a>(\*\*<a href="src/structify/types/entity_get_local_subgraph_params.py">params</a>) -> <a href="./src/structify/types/entity_get_local_subgraph_response.py">EntityGetLocalSubgraphResponse</a></code>
- <code title="get /entity/get_merges">client.entities.<a href="./src/structify/resources/entities.py">get_merges</a>(\*\*<a href="src/structify/types/entity_get_merges_params.py">params</a>) -> <a href="./src/structify/types/entity_get_merges_response.py">EntityGetMergesResponse</a></code>
- <code title="get /entity/get_source_entities">client.entities.<a href="./src/structify/resources/entities.py">get_source_entities</a>(\*\*<a href="src/structify/types/entity_get_source_entities_params.py">params</a>) -> <a href="./src/structify/types/entity_get_source_entities_response.py">EntityGetSourceEntitiesResponse</a></code>
- <code title="get /entity/list_jobs">client.entities.<a href="./src/structify/resources/entities.py">list_jobs</a>(\*\*<a href="src/structify/types/entity_list_jobs_params.py">params</a>) -> <a href="./src/structify/types/entity_list_jobs_response.py">EntityListJobsResponse</a></code>
- <code title="post /entity/merge">client.entities.<a href="./src/structify/resources/entities.py">merge</a>(\*\*<a href="src/structify/types/entity_merge_params.py">params</a>) -> <a href="./src/structify/types/entity_merge_response.py">EntityMergeResponse</a></code>
- <code title="post /entity/search">client.entities.<a href="./src/structify/resources/entities.py">search</a>(\*\*<a href="src/structify/types/entity_search_params.py">params</a>) -> <a href="./src/structify/types/entity_search_response.py">EntitySearchResponse</a></code>
- <code title="post /entity/summarize">client.entities.<a href="./src/structify/resources/entities.py">summarize</a>(\*\*<a href="src/structify/types/entity_summarize_params.py">params</a>) -> <a href="./src/structify/types/entity_summarize_response.py">EntitySummarizeResponse</a></code>
- <code title="post /entity/trigger_merge">client.entities.<a href="./src/structify/resources/entities.py">trigger_merge</a>(\*\*<a href="src/structify/types/entity_trigger_merge_params.py">params</a>) -> <a href="./src/structify/types/entity_trigger_merge_response.py">EntityTriggerMergeResponse</a></code>
- <code title="post /entity/update">client.entities.<a href="./src/structify/resources/entities.py">update_property</a>(\*\*<a href="src/structify/types/entity_update_property_params.py">params</a>) -> <a href="./src/structify/types/entity_update_property_response.py">EntityUpdatePropertyResponse</a></code>
- <code title="post /entity/verify">client.entities.<a href="./src/structify/resources/entities.py">verify</a>(\*\*<a href="src/structify/types/entity_verify_params.py">params</a>) -> <a href="./src/structify/types/knowledge_graph.py">KnowledgeGraph</a></code>
- <code title="get /entity/view">client.entities.<a href="./src/structify/resources/entities.py">view</a>(\*\*<a href="src/structify/types/entity_view_params.py">params</a>) -> <a href="./src/structify/types/entity_view_response.py">EntityViewResponse</a></code>

# Report

Types:

```python
from structify.types import (
    ReportMissingResponse,
    ReportRelationshipResponse,
    ReportStepResponse,
    ReportWrongResponse,
)
```

Methods:

- <code title="post /report/entity/missing">client.report.<a href="./src/structify/resources/report.py">missing</a>(\*\*<a href="src/structify/types/report_missing_params.py">params</a>) -> str</code>
- <code title="post /report/relationship/missing">client.report.<a href="./src/structify/resources/report.py">relationship</a>(\*\*<a href="src/structify/types/report_relationship_params.py">params</a>) -> str</code>
- <code title="post /report/step">client.report.<a href="./src/structify/resources/report.py">step</a>(\*\*<a href="src/structify/types/report_step_params.py">params</a>) -> str</code>
- <code title="post /report/entity/wrong">client.report.<a href="./src/structify/resources/report.py">wrong</a>(\*\*<a href="src/structify/types/report_wrong_params.py">params</a>) -> str</code>

# Sandbox

Types:

```python
from structify.types import GetSandboxRequest, Sandbox, SandboxListResponse
```

Methods:

- <code title="post /sandbox/{chat_id}">client.sandbox.<a href="./src/structify/resources/sandbox.py">create</a>(chat_id, \*\*<a href="src/structify/types/sandbox_create_params.py">params</a>) -> <a href="./src/structify/types/sandbox.py">Sandbox</a></code>
- <code title="get /sandbox/list/{chat_id}">client.sandbox.<a href="./src/structify/resources/sandbox.py">list</a>(chat_id) -> <a href="./src/structify/types/sandbox_list_response.py">SandboxListResponse</a></code>
- <code title="post /sandbox/live/{chat_id}">client.sandbox.<a href="./src/structify/resources/sandbox.py">get</a>(chat_id, \*\*<a href="src/structify/types/sandbox_get_params.py">params</a>) -> <a href="./src/structify/types/sandbox.py">Sandbox</a></code>
- <code title="patch /sandbox/{sandbox_id}/status">client.sandbox.<a href="./src/structify/resources/sandbox.py">update_status</a>(sandbox_id, \*\*<a href="src/structify/types/sandbox_update_status_params.py">params</a>) -> <a href="./src/structify/types/sandbox.py">Sandbox</a></code>

# Scrape

Types:

```python
from structify.types import (
    ScrapeListRequest,
    ScrapeRequest,
    ScrapeListResponse,
    ScrapeScrapeResponse,
)
```

Methods:

- <code title="post /scrape/list">client.scrape.<a href="./src/structify/resources/scrape.py">list</a>(\*\*<a href="src/structify/types/scrape_list_params.py">params</a>) -> <a href="./src/structify/types/scrape_list_response.py">ScrapeListResponse</a></code>
- <code title="post /scrape">client.scrape.<a href="./src/structify/resources/scrape.py">scrape</a>(\*\*<a href="src/structify/types/scrape_scrape_params.py">params</a>) -> <a href="./src/structify/types/scrape_scrape_response.py">ScrapeScrapeResponse</a></code>

# Code

Types:

```python
from structify.types import GenerateCodeRequest
```

Methods:

- <code title="post /code/generate-code">client.code.<a href="./src/structify/resources/code.py">generate_code</a>(\*\*<a href="src/structify/types/code_generate_code_params.py">params</a>) -> None</code>

# Structure

Types:

```python
from structify.types import (
    ChatPrompt,
    ExecutionStep,
    SaveRequirement,
    ToolMetadata,
    StructureEnhancePropertyResponse,
    StructureEnhanceRelationshipResponse,
    StructureFindRelationshipResponse,
    StructureIsCompleteResponse,
    StructureJobStatusResponse,
    StructureRunAsyncResponse,
)
```

Methods:

- <code title="post /structure/enhance_property">client.structure.<a href="./src/structify/resources/structure.py">enhance_property</a>(\*\*<a href="src/structify/types/structure_enhance_property_params.py">params</a>) -> str</code>
- <code title="post /structure/enhance_relationship">client.structure.<a href="./src/structify/resources/structure.py">enhance_relationship</a>(\*\*<a href="src/structify/types/structure_enhance_relationship_params.py">params</a>) -> str</code>
- <code title="post /structure/find_relationship">client.structure.<a href="./src/structify/resources/structure.py">find_relationship</a>(\*\*<a href="src/structify/types/structure_find_relationship_params.py">params</a>) -> str</code>
- <code title="post /structure/is_complete">client.structure.<a href="./src/structify/resources/structure.py">is_complete</a>(\*\*<a href="src/structify/types/structure_is_complete_params.py">params</a>) -> str</code>
- <code title="post /structure/job_status">client.structure.<a href="./src/structify/resources/structure.py">job_status</a>(\*\*<a href="src/structify/types/structure_job_status_params.py">params</a>) -> <a href="./src/structify/types/structure_job_status_response.py">StructureJobStatusResponse</a></code>
- <code title="post /structure/run_async">client.structure.<a href="./src/structify/resources/structure.py">run_async</a>(\*\*<a href="src/structify/types/structure_run_async_params.py">params</a>) -> str</code>

# PublicSessions

Methods:

- <code title="get /public/chat/{chat_session_id}/latest-workflow">client.public_sessions.<a href="./src/structify/resources/public_sessions.py">get_latest_workflow</a>(chat_session_id) -> <a href="./src/structify/types/workflow_dag.py">WorkflowDag</a></code>
- <code title="get /public/nodes/{node_id}/output_data">client.public_sessions.<a href="./src/structify/resources/public_sessions.py">get_node_output_data</a>(node_id) -> BinaryAPIResponse</code>

# Shared

Types:

```python
from structify.types import (
    DatasetDescriptor,
    Entity,
    EntityMatch,
    Image,
    KnowledgeGraph,
    PropertyType,
    Relationship,
    Table,
)
```

# External

## News

Types:

```python
from structify.types.external import (
    EverythingQuery,
    EverythingResponse,
    NewsArticle,
    NewsSource,
    NewsSourceDetail,
    SourcesQuery,
    SourcesResponse,
    TopHeadlinesQuery,
    TopHeadlinesResponse,
)
```

Methods:

- <code title="get /external/news/everything">client.external.news.<a href="./src/structify/resources/external/news.py">everything</a>(\*\*<a href="src/structify/types/external/news_everything_params.py">params</a>) -> <a href="./src/structify/types/external/everything_response.py">EverythingResponse</a></code>
- <code title="get /external/news/sources">client.external.news.<a href="./src/structify/resources/external/news.py">sources</a>(\*\*<a href="src/structify/types/external/news_sources_params.py">params</a>) -> <a href="./src/structify/types/external/sources_response.py">SourcesResponse</a></code>
- <code title="get /external/news/top-headlines">client.external.news.<a href="./src/structify/resources/external/news.py">top_headlines</a>(\*\*<a href="src/structify/types/external/news_top_headlines_params.py">params</a>) -> <a href="./src/structify/types/external/top_headlines_response.py">TopHeadlinesResponse</a></code>

## SearchAPI

Types:

```python
from structify.types.external import (
    FlightCalendarRequest,
    FlightLocationSearchRequest,
    GoogleFlightsSearchRequest,
    GoogleMapsResult,
    GoogleMapsSearchRequest,
    GoogleScholarSearchRequest,
    GoogleSearchRequest,
    GoogleSearchResponse,
    GoogleSearchResult,
    LocationCoordinates,
    LocationResponse,
    LocationResult,
    LocationSearchRequest,
    PlaceDetailsRequest,
    PlacePhotosRequest,
    PlaceReviewsRequest,
    ScholarAuthorSearchRequest,
    ScholarCiteRequest,
    SearchAPIGoogleFlightsCalendarResponse,
    SearchAPIGoogleFlightsLocationSearchResponse,
    SearchAPIGoogleFlightsSearchResponse,
    SearchAPIGoogleMapsPlaceDetailsResponse,
    SearchAPIGoogleMapsPlacePhotosResponse,
    SearchAPIGoogleMapsPlaceReviewsResponse,
    SearchAPIGoogleMapsSearchResponse,
    SearchAPIGoogleScholarAuthorSearchResponse,
    SearchAPIGoogleScholarCitationsResponse,
    SearchAPIGoogleScholarSearchResponse,
)
```

Methods:

- <code title="post /external/search/flights/calendar">client.external.search_api.<a href="./src/structify/resources/external/search_api.py">google_flights_calendar</a>(\*\*<a href="src/structify/types/external/search_api_google_flights_calendar_params.py">params</a>) -> <a href="./src/structify/types/external/search_api_google_flights_calendar_response.py">SearchAPIGoogleFlightsCalendarResponse</a></code>
- <code title="post /external/search/flights/location_search">client.external.search_api.<a href="./src/structify/resources/external/search_api.py">google_flights_location_search</a>(\*\*<a href="src/structify/types/external/search_api_google_flights_location_search_params.py">params</a>) -> <a href="./src/structify/types/external/search_api_google_flights_location_search_response.py">SearchAPIGoogleFlightsLocationSearchResponse</a></code>
- <code title="post /external/search/flights/search">client.external.search_api.<a href="./src/structify/resources/external/search_api.py">google_flights_search</a>(\*\*<a href="src/structify/types/external/search_api_google_flights_search_params.py">params</a>) -> <a href="./src/structify/types/external/search_api_google_flights_search_response.py">SearchAPIGoogleFlightsSearchResponse</a></code>
- <code title="post /external/search/maps/place">client.external.search_api.<a href="./src/structify/resources/external/search_api.py">google_maps_place_details</a>(\*\*<a href="src/structify/types/external/search_api_google_maps_place_details_params.py">params</a>) -> <a href="./src/structify/types/external/search_api_google_maps_place_details_response.py">SearchAPIGoogleMapsPlaceDetailsResponse</a></code>
- <code title="post /external/search/maps/photos">client.external.search_api.<a href="./src/structify/resources/external/search_api.py">google_maps_place_photos</a>(\*\*<a href="src/structify/types/external/search_api_google_maps_place_photos_params.py">params</a>) -> <a href="./src/structify/types/external/search_api_google_maps_place_photos_response.py">SearchAPIGoogleMapsPlacePhotosResponse</a></code>
- <code title="post /external/search/maps/reviews">client.external.search_api.<a href="./src/structify/resources/external/search_api.py">google_maps_place_reviews</a>(\*\*<a href="src/structify/types/external/search_api_google_maps_place_reviews_params.py">params</a>) -> <a href="./src/structify/types/external/search_api_google_maps_place_reviews_response.py">SearchAPIGoogleMapsPlaceReviewsResponse</a></code>
- <code title="post /external/search/maps/search">client.external.search_api.<a href="./src/structify/resources/external/search_api.py">google_maps_search</a>(\*\*<a href="src/structify/types/external/search_api_google_maps_search_params.py">params</a>) -> <a href="./src/structify/types/external/search_api_google_maps_search_response.py">SearchAPIGoogleMapsSearchResponse</a></code>
- <code title="post /external/search/scholar/author">client.external.search_api.<a href="./src/structify/resources/external/search_api.py">google_scholar_author_search</a>(\*\*<a href="src/structify/types/external/search_api_google_scholar_author_search_params.py">params</a>) -> <a href="./src/structify/types/external/search_api_google_scholar_author_search_response.py">SearchAPIGoogleScholarAuthorSearchResponse</a></code>
- <code title="post /external/search/scholar/cite">client.external.search_api.<a href="./src/structify/resources/external/search_api.py">google_scholar_citations</a>(\*\*<a href="src/structify/types/external/search_api_google_scholar_citations_params.py">params</a>) -> <a href="./src/structify/types/external/search_api_google_scholar_citations_response.py">SearchAPIGoogleScholarCitationsResponse</a></code>
- <code title="post /external/search/scholar/search">client.external.search_api.<a href="./src/structify/resources/external/search_api.py">google_scholar_search</a>(\*\*<a href="src/structify/types/external/search_api_google_scholar_search_params.py">params</a>) -> <a href="./src/structify/types/external/search_api_google_scholar_search_response.py">SearchAPIGoogleScholarSearchResponse</a></code>
- <code title="post /external/search/search">client.external.search_api.<a href="./src/structify/resources/external/search_api.py">google_search</a>(\*\*<a href="src/structify/types/external/search_api_google_search_params.py">params</a>) -> <a href="./src/structify/types/external/google_search_response.py">GoogleSearchResponse</a></code>
- <code title="post /external/search/locations">client.external.search_api.<a href="./src/structify/resources/external/search_api.py">location_search</a>(\*\*<a href="src/structify/types/external/search_api_location_search_params.py">params</a>) -> <a href="./src/structify/types/external/location_response.py">LocationResponse</a></code>

## People

Types:

```python
from structify.types.external import (
    CompaniesSearchRequest,
    CompaniesSearchResponse,
    CompanySearchResult,
    EnrichedOrganization,
    JobPosting,
    JobPostingsQuery,
    JobPostingsResponse,
    OrganizationDetail,
    OrganizationEnrichQuery,
    PeopleMatchRequest,
    PeopleMatchResponse,
    PeopleSearchRequest,
    PeopleSearchResponse,
    PersonMatch,
    PersonSearchResult,
)
```

Methods:

- <code title="post /external/people/mixed_companies/search">client.external.people.<a href="./src/structify/resources/external/people.py">companies_search</a>(\*\*<a href="src/structify/types/external/person_companies_search_params.py">params</a>) -> <a href="./src/structify/types/external/companies_search_response.py">CompaniesSearchResponse</a></code>
- <code title="get /external/people/organizations/{id}">client.external.people.<a href="./src/structify/resources/external/people.py">organization_detail</a>(id) -> <a href="./src/structify/types/external/organization_detail.py">OrganizationDetail</a></code>
- <code title="get /external/people/organizations/{organization_id}/job_postings">client.external.people.<a href="./src/structify/resources/external/people.py">organization_job_postings</a>(organization_id, \*\*<a href="src/structify/types/external/person_organization_job_postings_params.py">params</a>) -> <a href="./src/structify/types/external/job_postings_response.py">JobPostingsResponse</a></code>
- <code title="get /external/people/organizations/enrich">client.external.people.<a href="./src/structify/resources/external/people.py">organizations_enrich</a>(\*\*<a href="src/structify/types/external/person_organizations_enrich_params.py">params</a>) -> <a href="./src/structify/types/external/enriched_organization.py">EnrichedOrganization</a></code>
- <code title="post /external/people/people/match">client.external.people.<a href="./src/structify/resources/external/people.py">people_match</a>(\*\*<a href="src/structify/types/external/person_people_match_params.py">params</a>) -> <a href="./src/structify/types/external/people_match_response.py">PeopleMatchResponse</a></code>
- <code title="post /external/people/mixed_people/search">client.external.people.<a href="./src/structify/resources/external/people.py">people_search</a>(\*\*<a href="src/structify/types/external/person_people_search_params.py">params</a>) -> <a href="./src/structify/types/external/people_search_response.py">PeopleSearchResponse</a></code>
