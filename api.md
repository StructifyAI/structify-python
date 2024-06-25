# AdminUsers

Types:

```python
from structify.types import UserNode, AdminUserListResponse
```

Methods:

- <code title="get /admin/users/list">client.admin_users.<a href="./src/structify/resources/admin_users.py">list</a>() -> <a href="./src/structify/types/admin_user_list_response.py">AdminUserListResponse</a></code>

# Datasets

Types:

```python
from structify.types import (
    DatasetDescriptor,
    DatasetNode,
    KgEntity,
    DatasetListResponse,
    DatasetViewResponse,
)
```

Methods:

- <code title="post /dataset/create">client.datasets.<a href="./src/structify/resources/datasets.py">create</a>(\*\*<a href="src/structify/types/dataset_create_params.py">params</a>) -> None</code>
- <code title="get /dataset/list">client.datasets.<a href="./src/structify/resources/datasets.py">list</a>() -> <a href="./src/structify/types/dataset_list_response.py">DatasetListResponse</a></code>
- <code title="delete /dataset/delete">client.datasets.<a href="./src/structify/resources/datasets.py">delete</a>(\*\*<a href="src/structify/types/dataset_delete_params.py">params</a>) -> None</code>
- <code title="get /dataset/info">client.datasets.<a href="./src/structify/resources/datasets.py">retrieve_info</a>(\*\*<a href="src/structify/types/dataset_retrieve_info_params.py">params</a>) -> <a href="./src/structify/types/dataset_descriptor.py">Optional</a></code>
- <code title="get /dataset/view">client.datasets.<a href="./src/structify/resources/datasets.py">view</a>(\*\*<a href="src/structify/types/dataset_view_params.py">params</a>) -> <a href="./src/structify/types/dataset_view_response.py">DatasetViewResponse</a></code>

# Documents

Types:

```python
from structify.types import SourceNode, UserFile, DocumentListResponse
```

Methods:

- <code title="get /documents/list">client.documents.<a href="./src/structify/resources/documents.py">list</a>() -> <a href="./src/structify/types/document_list_response.py">DocumentListResponse</a></code>
- <code title="delete /documents/delete/{path}">client.documents.<a href="./src/structify/resources/documents.py">delete</a>(path) -> None</code>
- <code title="get /documents/download/{path}">client.documents.<a href="./src/structify/resources/documents.py">download</a>(path) -> BinaryAPIResponse</code>
- <code title="get /source/get_sources">client.documents.<a href="./src/structify/resources/documents.py">get_sources</a>(\*\*<a href="src/structify/types/document_get_sources_params.py">params</a>) -> <a href="./src/structify/types/source_node.py">SourceNode</a></code>
- <code title="post /documents/upload">client.documents.<a href="./src/structify/resources/documents.py">upload</a>(\*\*<a href="src/structify/types/document_upload_params.py">params</a>) -> None</code>

# Label

## LlmAssist

Types:

```python
from structify.types.label import ToolInput, LlmAssistRetrieveResponse
```

Methods:

- <code title="get /label/llm_assist/{uuid}">client.label.llm_assist.<a href="./src/structify/resources/label/llm_assist.py">retrieve</a>(uuid) -> <a href="./src/structify/types/label/llm_assist_retrieve_response.py">LlmAssistRetrieveResponse</a></code>

## Refresh

Types:

```python
from structify.types.label import RefreshResponse
```

Methods:

- <code title="get /label/refresh">client.label.refresh.<a href="./src/structify/resources/label/refresh.py">retrieve</a>(\*\*<a href="src/structify/types/label/refresh_retrieve_params.py">params</a>) -> <a href="./src/structify/types/label/refresh_response.py">Optional</a></code>

## RunAsync

Types:

```python
from structify.types.label import RunAsyncCreateResponse
```

Methods:

- <code title="post /label/run_async">client.label.run_async.<a href="./src/structify/resources/label/run_async.py">create</a>(\*\*<a href="src/structify/types/label/run_async_create_params.py">params</a>) -> str</code>

## Submit

Types:

```python
from structify.types.label import SubmitCreateResponse
```

Methods:

- <code title="post /label/submit/{uuid}">client.label.submit.<a href="./src/structify/resources/label/submit.py">create</a>(uuid, \*\*<a href="src/structify/types/label/submit_create_params.py">params</a>) -> str</code>

## Update

Types:

```python
from structify.types.label import UpdateCreateResponse
```

Methods:

- <code title="post /label/update/{run_uuid}/{run_idx}">client.label.update.<a href="./src/structify/resources/label/update.py">create</a>(run_idx, \*, run_uuid, \*\*<a href="src/structify/types/label/update_create_params.py">params</a>) -> str</code>

# Runs

Types:

```python
from structify.types import ExecutionHistory, JobNode, RunListResponse, RunDeleteResponse
```

Methods:

- <code title="get /runs/get/{uuid}">client.runs.<a href="./src/structify/resources/runs.py">retrieve</a>(uuid) -> <a href="./src/structify/types/execution_history.py">ExecutionHistory</a></code>
- <code title="get /runs/list">client.runs.<a href="./src/structify/resources/runs.py">list</a>() -> <a href="./src/structify/types/run_list_response.py">RunListResponse</a></code>
- <code title="post /runs/delete/{uuid}">client.runs.<a href="./src/structify/resources/runs.py">delete</a>(uuid) -> str</code>
- <code title="post /runs/cancel/{uuid}">client.runs.<a href="./src/structify/resources/runs.py">cancel</a>(uuid) -> <a href="./src/structify/types/job_node.py">JobNode</a></code>
- <code title="post /runs/schedule">client.runs.<a href="./src/structify/resources/runs.py">schedule</a>() -> None</code>

# Server

Types:

```python
from structify.types import ServerInformation
```

Methods:

- <code title="get /server/version">client.server.<a href="./src/structify/resources/server.py">version</a>() -> <a href="./src/structify/types/server_information.py">ServerInformation</a></code>

# Structure

Types:

```python
from structify.types import (
    StructureIsCompleteResponse,
    StructureJobStatusResponse,
    StructureRunAsyncResponse,
)
```

Methods:

- <code title="post /structure/is_complete">client.structure.<a href="./src/structify/resources/structure.py">is_complete</a>(\*\*<a href="src/structify/types/structure_is_complete_params.py">params</a>) -> str</code>
- <code title="post /structure/job_status">client.structure.<a href="./src/structify/resources/structure.py">job_status</a>(\*\*<a href="src/structify/types/structure_job_status_params.py">params</a>) -> <a href="./src/structify/types/structure_job_status_response.py">object</a></code>
- <code title="post /structure/run_async">client.structure.<a href="./src/structify/resources/structure.py">run_async</a>(\*\*<a href="src/structify/types/structure_run_async_params.py">params</a>) -> str</code>

# Usage

Types:

```python
from structify.types import UsageGetJobInfoResponse
```

Methods:

- <code title="post /usage/get_job_info">client.usage.<a href="./src/structify/resources/usage.py">get_job_info</a>(\*\*<a href="src/structify/types/usage_get_job_info_params.py">params</a>) -> <a href="./src/structify/types/usage_get_job_info_response.py">object</a></code>

# Account

Types:

```python
from structify.types import NewToken, UserInfoResponse
```

Methods:

- <code title="post /user/create_test_token">client.account.<a href="./src/structify/resources/account.py">create_test_token</a>() -> <a href="./src/structify/types/new_token.py">NewToken</a></code>
- <code title="get /user/info">client.account.<a href="./src/structify/resources/account.py">info</a>() -> <a href="./src/structify/types/user_info_response.py">UserInfoResponse</a></code>
