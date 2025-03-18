# User

Types:

```python
from structify.types import TokenResponse, UserInfo, UserTransactionsResponse, UserUsageResponse
```

Methods:

- <code title="get /user/info">client.user.<a href="./src/structify/resources/user.py">info</a>() -> <a href="./src/structify/types/user_info.py">UserInfo</a></code>
- <code title="get /user/transactions/list">client.user.<a href="./src/structify/resources/user.py">transactions</a>() -> <a href="./src/structify/types/user_transactions_response.py">UserTransactionsResponse</a></code>
- <code title="get /user/usage">client.user.<a href="./src/structify/resources/user.py">usage</a>(\*\*<a href="src/structify/types/user_usage_params.py">params</a>) -> <a href="./src/structify/types/user_usage_response.py">UserUsageResponse</a></code>

# Admin

## NextAction

Types:

```python
from structify.types.admin import (
    ActionTrainingDataEntry,
    NextActionDeleteTrainingDataResponse,
    NextActionGetTrainingDataResponse,
)
```

Methods:

- <code title="post /admin/next_action/add_action_training_datum">client.admin.next_action.<a href="./src/structify/resources/admin/next_action.py">add_training_datum</a>(\*\*<a href="src/structify/types/admin/next_action_add_training_datum_params.py">params</a>) -> None</code>
- <code title="delete /admin/next_action/delete_action_training_data">client.admin.next_action.<a href="./src/structify/resources/admin/next_action.py">delete_training_data</a>(\*\*<a href="src/structify/types/admin/next_action_delete_training_data_params.py">params</a>) -> <a href="./src/structify/types/admin/next_action_delete_training_data_response.py">object</a></code>
- <code title="get /admin/next_action/get_action_training_data">client.admin.next_action.<a href="./src/structify/resources/admin/next_action.py">get_training_data</a>(\*\*<a href="src/structify/types/admin/next_action_get_training_data_params.py">params</a>) -> <a href="./src/structify/types/admin/next_action_get_training_data_response.py">object</a></code>
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
- <code title="put /admin/users/update">client.admin.users.<a href="./src/structify/resources/admin/users.py">update</a>(\*\*<a href="src/structify/types/admin/user_update_params.py">params</a>) -> <a href="./src/structify/types/admin/user.py">User</a></code>
- <code title="get /admin/users/list">client.admin.users.<a href="./src/structify/resources/admin/users.py">list</a>() -> <a href="./src/structify/types/admin/user_list_response.py">UserListResponse</a></code>
- <code title="post /admin/users/get_credits">client.admin.users.<a href="./src/structify/resources/admin/users.py">get_credits</a>(\*\*<a href="src/structify/types/admin/user_get_credits_params.py">params</a>) -> <a href="./src/structify/types/admin/user_get_credits_response.py">UserGetCreditsResponse</a></code>
- <code title="post /admin/users/get_stats">client.admin.users.<a href="./src/structify/resources/admin/users.py">get_stats</a>(\*\*<a href="src/structify/types/admin/user_get_stats_params.py">params</a>) -> <a href="./src/structify/types/admin/user_get_stats_response.py">UserGetStatsResponse</a></code>
- <code title="post /admin/users/set_credits">client.admin.users.<a href="./src/structify/resources/admin/users.py">set_credits</a>(\*\*<a href="src/structify/types/admin/user_set_credits_params.py">params</a>) -> <a href="./src/structify/types/admin/user_set_credits_response.py">UserSetCreditsResponse</a></code>

## TrainingDatasets

Types:

```python
from structify.types.admin import DatumStatus, LabelingStats
```

# Datasets

Types:

```python
from structify.types import (
    MergeConfig,
    RelationshipMergeStrategy,
    Strategy,
    DatasetListResponse,
    DatasetGetResponse,
    DatasetMatchResponse,
    DatasetViewRelationshipsResponse,
    DatasetViewTableResponse,
    DatasetViewTablesWithRelationshipsResponse,
)
```

Methods:

- <code title="post /dataset/create">client.datasets.<a href="./src/structify/resources/datasets/datasets.py">create</a>(\*\*<a href="src/structify/types/dataset_create_params.py">params</a>) -> None</code>
- <code title="get /dataset/list">client.datasets.<a href="./src/structify/resources/datasets/datasets.py">list</a>() -> <a href="./src/structify/types/dataset_list_response.py">DatasetListResponse</a></code>
- <code title="delete /dataset/delete">client.datasets.<a href="./src/structify/resources/datasets/datasets.py">delete</a>(\*\*<a href="src/structify/types/dataset_delete_params.py">params</a>) -> None</code>
- <code title="get /dataset/info">client.datasets.<a href="./src/structify/resources/datasets/datasets.py">get</a>(\*\*<a href="src/structify/types/dataset_get_params.py">params</a>) -> <a href="./src/structify/types/dataset_get_response.py">DatasetGetResponse</a></code>
- <code title="post /dataset/match">client.datasets.<a href="./src/structify/resources/datasets/datasets.py">match</a>(\*\*<a href="src/structify/types/dataset_match_params.py">params</a>) -> <a href="./src/structify/types/dataset_match_response.py">DatasetMatchResponse</a></code>
- <code title="get /dataset/view_relationships">client.datasets.<a href="./src/structify/resources/datasets/datasets.py">view_relationships</a>(\*\*<a href="src/structify/types/dataset_view_relationships_params.py">params</a>) -> <a href="./src/structify/types/dataset_view_relationships_response.py">SyncJobsList[DatasetViewRelationshipsResponse]</a></code>
- <code title="get /dataset/view_table">client.datasets.<a href="./src/structify/resources/datasets/datasets.py">view_table</a>(\*\*<a href="src/structify/types/dataset_view_table_params.py">params</a>) -> <a href="./src/structify/types/dataset_view_table_response.py">SyncJobsList[DatasetViewTableResponse]</a></code>
- <code title="get /dataset/view_tables_with_relationships">client.datasets.<a href="./src/structify/resources/datasets/datasets.py">view_tables_with_relationships</a>(\*\*<a href="src/structify/types/dataset_view_tables_with_relationships_params.py">params</a>) -> <a href="./src/structify/types/dataset_view_tables_with_relationships_response.py">DatasetViewTablesWithRelationshipsResponse</a></code>

# Documents

Types:

```python
from structify.types import DocumentListResponse, DocumentDownloadResponse
```

Methods:

- <code title="get /documents/list">client.documents.<a href="./src/structify/resources/documents.py">list</a>(\*\*<a href="src/structify/types/document_list_params.py">params</a>) -> <a href="./src/structify/types/document_list_response.py">DocumentListResponse</a></code>
- <code title="delete /documents/delete">client.documents.<a href="./src/structify/resources/documents.py">delete</a>(\*\*<a href="src/structify/types/document_delete_params.py">params</a>) -> None</code>
- <code title="post /documents/download">client.documents.<a href="./src/structify/resources/documents.py">download</a>(\*\*<a href="src/structify/types/document_download_params.py">params</a>) -> <a href="./src/structify/types/document_download_response.py">DocumentDownloadResponse</a></code>
- <code title="post /documents/upload">client.documents.<a href="./src/structify/resources/documents.py">upload</a>(\*\*<a href="src/structify/types/document_upload_params.py">params</a>) -> None</code>

# Jobs

Types:

```python
from structify.types import (
    JobListResponse,
    JobDeleteResponse,
    JobCancelResponse,
    JobGetResponse,
    JobGetStepGraphResponse,
    JobGetStepsResponse,
)
```

Methods:

- <code title="get /jobs/list">client.jobs.<a href="./src/structify/resources/jobs.py">list</a>(\*\*<a href="src/structify/types/job_list_params.py">params</a>) -> <a href="./src/structify/types/job_list_response.py">SyncJobsList[JobListResponse]</a></code>
- <code title="post /jobs/delete/{job_id}">client.jobs.<a href="./src/structify/resources/jobs.py">delete</a>(job_id) -> str</code>
- <code title="post /jobs/cancel/{uuid}">client.jobs.<a href="./src/structify/resources/jobs.py">cancel</a>(uuid) -> <a href="./src/structify/types/job_cancel_response.py">JobCancelResponse</a></code>
- <code title="get /jobs/get/{job_id}">client.jobs.<a href="./src/structify/resources/jobs.py">get</a>(job_id) -> <a href="./src/structify/types/job_get_response.py">JobGetResponse</a></code>
- <code title="get /jobs/get_step/{step_id}">client.jobs.<a href="./src/structify/resources/jobs.py">get_step</a>(step_id) -> <a href="./src/structify/types/execution_step.py">ExecutionStep</a></code>
- <code title="get /jobs/get_step_graph/{job_id}">client.jobs.<a href="./src/structify/resources/jobs.py">get_step_graph</a>(job_id) -> <a href="./src/structify/types/job_get_step_graph_response.py">JobGetStepGraphResponse</a></code>
- <code title="get /jobs/get_steps/{job_id}">client.jobs.<a href="./src/structify/resources/jobs.py">get_steps</a>(job_id) -> <a href="./src/structify/types/job_get_steps_response.py">JobGetStepsResponse</a></code>
- <code title="post /jobs/schedule">client.jobs.<a href="./src/structify/resources/jobs.py">schedule</a>() -> None</code>

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
from structify.types import Source, SourceListResponse
```

Methods:

- <code title="get /source/get_sources">client.sources.<a href="./src/structify/resources/sources.py">list</a>(\*\*<a href="src/structify/types/source_list_params.py">params</a>) -> <a href="./src/structify/types/source_list_response.py">SourceListResponse</a></code>

# Entities

Types:

```python
from structify.types import (
    EntityDeleteResponse,
    EntityAddResponse,
    EntityAddBatchResponse,
    EntityGetResponse,
    EntityGetLocalSubgraphResponse,
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
- <code title="get /entity/get">client.entities.<a href="./src/structify/resources/entities.py">get</a>(\*\*<a href="src/structify/types/entity_get_params.py">params</a>) -> <a href="./src/structify/types/entity_get_response.py">EntityGetResponse</a></code>
- <code title="get /entity/get_local_subgraph">client.entities.<a href="./src/structify/resources/entities.py">get_local_subgraph</a>(\*\*<a href="src/structify/types/entity_get_local_subgraph_params.py">params</a>) -> <a href="./src/structify/types/entity_get_local_subgraph_response.py">EntityGetLocalSubgraphResponse</a></code>
- <code title="get /entity/get_source_entities">client.entities.<a href="./src/structify/resources/entities.py">get_source_entities</a>(\*\*<a href="src/structify/types/entity_get_source_entities_params.py">params</a>) -> <a href="./src/structify/types/entity_get_source_entities_response.py">EntityGetSourceEntitiesResponse</a></code>
- <code title="get /entity/list_jobs">client.entities.<a href="./src/structify/resources/entities.py">list_jobs</a>(\*\*<a href="src/structify/types/entity_list_jobs_params.py">params</a>) -> <a href="./src/structify/types/entity_list_jobs_response.py">EntityListJobsResponse</a></code>
- <code title="post /entity/merge">client.entities.<a href="./src/structify/resources/entities.py">merge</a>(\*\*<a href="src/structify/types/entity_merge_params.py">params</a>) -> <a href="./src/structify/types/entity_merge_response.py">EntityMergeResponse</a></code>
- <code title="post /entity/search">client.entities.<a href="./src/structify/resources/entities.py">search</a>(\*\*<a href="src/structify/types/entity_search_params.py">params</a>) -> <a href="./src/structify/types/entity_search_response.py">EntitySearchResponse</a></code>
- <code title="post /entity/summarize">client.entities.<a href="./src/structify/resources/entities.py">summarize</a>(\*\*<a href="src/structify/types/entity_summarize_params.py">params</a>) -> <a href="./src/structify/types/entity_summarize_response.py">EntitySummarizeResponse</a></code>
- <code title="post /entity/trigger_merge">client.entities.<a href="./src/structify/resources/entities.py">trigger_merge</a>(\*\*<a href="src/structify/types/entity_trigger_merge_params.py">params</a>) -> <a href="./src/structify/types/entity_trigger_merge_response.py">EntityTriggerMergeResponse</a></code>
- <code title="post /entity/update">client.entities.<a href="./src/structify/resources/entities.py">update_property</a>(\*\*<a href="src/structify/types/entity_update_property_params.py">params</a>) -> <a href="./src/structify/types/entity_update_property_response.py">EntityUpdatePropertyResponse</a></code>
- <code title="post /entity/verify">client.entities.<a href="./src/structify/resources/entities.py">verify</a>(\*\*<a href="src/structify/types/entity_verify_params.py">params</a>) -> <a href="./src/structify/types/knowledge_graph.py">KnowledgeGraph</a></code>
- <code title="get /entity/view">client.entities.<a href="./src/structify/resources/entities.py">view</a>(\*\*<a href="src/structify/types/entity_view_params.py">params</a>) -> <a href="./src/structify/types/entity_view_response.py">EntityViewResponse</a></code>

# Images

Types:

```python
from structify.types import ImageGetResponse
```

Methods:

- <code title="get /images/{hash}">client.images.<a href="./src/structify/resources/images.py">get</a>(hash) -> <a href="./src/structify/types/image_get_response.py">ImageGetResponse</a></code>

# Plan

Types:

```python
from structify.types import (
    EnhanceProperty,
    EnhanceRelationship,
    FindRelationship,
    Plan,
    PlanCreateResponse,
    PlanListResponse,
    PlanPauseAllResponse,
    PlanResumeAllResponse,
)
```

Methods:

- <code title="post /plan/create">client.plan.<a href="./src/structify/resources/plan.py">create</a>(\*\*<a href="src/structify/types/plan_create_params.py">params</a>) -> str</code>
- <code title="get /plan/list">client.plan.<a href="./src/structify/resources/plan.py">list</a>() -> <a href="./src/structify/types/plan_list_response.py">PlanListResponse</a></code>
- <code title="get /plan/pause_all">client.plan.<a href="./src/structify/resources/plan.py">pause_all</a>(\*\*<a href="src/structify/types/plan_pause_all_params.py">params</a>) -> <a href="./src/structify/types/plan_pause_all_response.py">PlanPauseAllResponse</a></code>
- <code title="get /plan/resume_all">client.plan.<a href="./src/structify/resources/plan.py">resume_all</a>(\*\*<a href="src/structify/types/plan_resume_all_params.py">params</a>) -> <a href="./src/structify/types/plan_resume_all_response.py">PlanResumeAllResponse</a></code>

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

# Shared

Types:

```python
from structify.types import (
    DatasetDescriptor,
    Entity,
    Image,
    KnowledgeGraph,
    MatchedEntity,
    PropertyType,
    Relationship,
    Table,
)
```
