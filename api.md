# User

Types:

```python
from structify.types import NewToken, UserInfo, UserUsageResponse
```

Methods:

- <code title="post /user/create_test_token">client.user.<a href="./src/structify/resources/user.py">create_test_token</a>() -> <a href="./src/structify/types/new_token.py">NewToken</a></code>
- <code title="get /user/info">client.user.<a href="./src/structify/resources/user.py">info</a>() -> <a href="./src/structify/types/user_info.py">UserInfo</a></code>
- <code title="get /user/usage">client.user.<a href="./src/structify/resources/user.py">usage</a>() -> <a href="./src/structify/types/user_usage_response.py">UserUsageResponse</a></code>

# Admin

## Users

Types:

```python
from structify.types.admin import User, UserListResponse
```

Methods:

- <code title="get /admin/users/list">client.admin.users.<a href="./src/structify/resources/admin/users.py">list</a>() -> <a href="./src/structify/types/admin/user_list_response.py">UserListResponse</a></code>

# Datasets

Types:

```python
from structify.types import (
    DatasetListResponse,
    DatasetViewRelationshipsResponse,
    DatasetViewTableResponse,
)
```

Methods:

- <code title="post /dataset/create">client.datasets.<a href="./src/structify/resources/datasets.py">create</a>(\*\*<a href="src/structify/types/dataset_create_params.py">params</a>) -> None</code>
- <code title="get /dataset/list">client.datasets.<a href="./src/structify/resources/datasets.py">list</a>() -> <a href="./src/structify/types/dataset_list_response.py">DatasetListResponse</a></code>
- <code title="delete /dataset/delete">client.datasets.<a href="./src/structify/resources/datasets.py">delete</a>(\*\*<a href="src/structify/types/dataset_delete_params.py">params</a>) -> None</code>
- <code title="get /dataset/info">client.datasets.<a href="./src/structify/resources/datasets.py">get</a>(\*\*<a href="src/structify/types/dataset_get_params.py">params</a>) -> <a href="./src/structify/types/dataset_descriptor.py">Optional</a></code>
- <code title="get /dataset/view_relationships">client.datasets.<a href="./src/structify/resources/datasets.py">view_relationships</a>(\*\*<a href="src/structify/types/dataset_view_relationships_params.py">params</a>) -> <a href="./src/structify/types/dataset_view_relationships_response.py">SyncJobsList[DatasetViewRelationshipsResponse]</a></code>
- <code title="get /dataset/view_table">client.datasets.<a href="./src/structify/resources/datasets.py">view_table</a>(\*\*<a href="src/structify/types/dataset_view_table_params.py">params</a>) -> <a href="./src/structify/types/dataset_view_table_response.py">SyncJobsList[DatasetViewTableResponse]</a></code>

# Documents

Types:

```python
from structify.types import DocumentListResponse
```

Methods:

- <code title="get /documents/list">client.documents.<a href="./src/structify/resources/documents.py">list</a>() -> <a href="./src/structify/types/document_list_response.py">DocumentListResponse</a></code>
- <code title="delete /documents/delete">client.documents.<a href="./src/structify/resources/documents.py">delete</a>(\*\*<a href="src/structify/types/document_delete_params.py">params</a>) -> None</code>
- <code title="get /documents/download/{path}">client.documents.<a href="./src/structify/resources/documents.py">download</a>(path) -> BinaryAPIResponse</code>
- <code title="post /documents/upload">client.documents.<a href="./src/structify/resources/documents.py">upload</a>(\*\*<a href="src/structify/types/document_upload_params.py">params</a>) -> None</code>

# Jobs

Types:

```python
from structify.types import (
    JobListResponse,
    JobDeleteResponse,
    JobCancelResponse,
    JobGetResponse,
    JobGetStepsResponse,
)
```

Methods:

- <code title="get /jobs/list">client.jobs.<a href="./src/structify/resources/jobs.py">list</a>(\*\*<a href="src/structify/types/job_list_params.py">params</a>) -> <a href="./src/structify/types/job_list_response.py">SyncJobsList[JobListResponse]</a></code>
- <code title="post /jobs/delete/{job_id}">client.jobs.<a href="./src/structify/resources/jobs.py">delete</a>(job_id) -> str</code>
- <code title="post /jobs/cancel/{uuid}">client.jobs.<a href="./src/structify/resources/jobs.py">cancel</a>(uuid) -> <a href="./src/structify/types/job_cancel_response.py">JobCancelResponse</a></code>
- <code title="get /jobs/get/{job_id}">client.jobs.<a href="./src/structify/resources/jobs.py">get</a>(job_id) -> <a href="./src/structify/types/job_get_response.py">JobGetResponse</a></code>
- <code title="get /jobs/get_step/{step_id}">client.jobs.<a href="./src/structify/resources/jobs.py">get_step</a>(step_id) -> <a href="./src/structify/types/execution_step.py">ExecutionStep</a></code>
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
from structify.types import EntityAddResponse, EntityGetResponse, EntityReportResponse
```

Methods:

- <code title="post /entity/add">client.entities.<a href="./src/structify/resources/entities.py">add</a>(\*\*<a href="src/structify/types/entity_add_params.py">params</a>) -> <a href="./src/structify/types/entity_add_response.py">EntityAddResponse</a></code>
- <code title="get /entity/get">client.entities.<a href="./src/structify/resources/entities.py">get</a>(\*\*<a href="src/structify/types/entity_get_params.py">params</a>) -> <a href="./src/structify/types/entity_get_response.py">EntityGetResponse</a></code>
- <code title="post /entity/report">client.entities.<a href="./src/structify/resources/entities.py">report</a>(\*\*<a href="src/structify/types/entity_report_params.py">params</a>) -> str</code>

# Structure

Types:

```python
from structify.types import (
    ChatPrompt,
    ExecutionStep,
    ExtractionCriteria,
    ToolMetadata,
    StructureIsCompleteResponse,
    StructureJobStatusResponse,
    StructureRunAsyncResponse,
)
```

Methods:

- <code title="post /structure/is_complete">client.structure.<a href="./src/structify/resources/structure.py">is_complete</a>(\*\*<a href="src/structify/types/structure_is_complete_params.py">params</a>) -> str</code>
- <code title="post /structure/job_status">client.structure.<a href="./src/structify/resources/structure.py">job_status</a>(\*\*<a href="src/structify/types/structure_job_status_params.py">params</a>) -> <a href="./src/structify/types/structure_job_status_response.py">StructureJobStatusResponse</a></code>
- <code title="post /structure/run_async">client.structure.<a href="./src/structify/resources/structure.py">run_async</a>(\*\*<a href="src/structify/types/structure_run_async_params.py">params</a>) -> str</code>

# Shared

Types:

```python
from structify.types import (
    DatasetDescriptor,
    Entity,
    KnowledgeGraph,
    PropertyType,
    Relationship,
    Table,
)
```
