# User

Types:

```python
from structify.types import NewToken, UserInfo
```

Methods:

- <code title="post /user/create_test_token">client.user.<a href="./src/structify/resources/user.py">create_test_token</a>() -> <a href="./src/structify/types/new_token.py">NewToken</a></code>
- <code title="get /user/info">client.user.<a href="./src/structify/resources/user.py">info</a>() -> <a href="./src/structify/types/user_info.py">UserInfo</a></code>

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
    Dataset,
    DatasetDescriptor,
    Entity,
    DatasetListResponse,
    DatasetViewResponse,
)
```

Methods:

- <code title="post /dataset/create">client.datasets.<a href="./src/structify/resources/datasets.py">create</a>(\*\*<a href="src/structify/types/dataset_create_params.py">params</a>) -> None</code>
- <code title="get /dataset/list">client.datasets.<a href="./src/structify/resources/datasets.py">list</a>() -> <a href="./src/structify/types/dataset_list_response.py">DatasetListResponse</a></code>
- <code title="delete /dataset/delete">client.datasets.<a href="./src/structify/resources/datasets.py">delete</a>(\*\*<a href="src/structify/types/dataset_delete_params.py">params</a>) -> None</code>
- <code title="get /dataset/info">client.datasets.<a href="./src/structify/resources/datasets.py">get</a>(\*\*<a href="src/structify/types/dataset_get_params.py">params</a>) -> <a href="./src/structify/types/dataset_descriptor.py">Optional</a></code>
- <code title="get /dataset/view">client.datasets.<a href="./src/structify/resources/datasets.py">view</a>(\*\*<a href="src/structify/types/dataset_view_params.py">params</a>) -> <a href="./src/structify/types/dataset_view_response.py">DatasetViewResponse</a></code>

# Documents

Types:

```python
from structify.types import DocumentListResponse
```

Methods:

- <code title="get /documents/list">client.documents.<a href="./src/structify/resources/documents.py">list</a>() -> <a href="./src/structify/types/document_list_response.py">DocumentListResponse</a></code>
- <code title="delete /documents/delete/{path}">client.documents.<a href="./src/structify/resources/documents.py">delete</a>(path) -> None</code>
- <code title="get /documents/download/{path}">client.documents.<a href="./src/structify/resources/documents.py">download</a>(path) -> BinaryAPIResponse</code>
- <code title="post /documents/upload">client.documents.<a href="./src/structify/resources/documents.py">upload</a>(\*\*<a href="src/structify/types/document_upload_params.py">params</a>) -> None</code>

# Runs

Types:

```python
from structify.types import RunListResponse, RunDeleteResponse, RunCancelResponse, RunGetResponse
```

Methods:

- <code title="get /runs/list">client.runs.<a href="./src/structify/resources/runs.py">list</a>() -> <a href="./src/structify/types/run_list_response.py">RunListResponse</a></code>
- <code title="post /runs/delete/{uuid}">client.runs.<a href="./src/structify/resources/runs.py">delete</a>(uuid) -> str</code>
- <code title="post /runs/cancel/{uuid}">client.runs.<a href="./src/structify/resources/runs.py">cancel</a>(uuid) -> <a href="./src/structify/types/run_cancel_response.py">RunCancelResponse</a></code>
- <code title="get /runs/get/{uuid}">client.runs.<a href="./src/structify/resources/runs.py">get</a>(uuid) -> <a href="./src/structify/types/run_get_response.py">RunGetResponse</a></code>
- <code title="post /runs/schedule">client.runs.<a href="./src/structify/resources/runs.py">schedule</a>() -> None</code>

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

# Label

Types:

```python
from structify.types import (
    LabelUpdateResponse,
    LabelGetMessagesResponse,
    LabelLlmAssistResponse,
    LabelRunResponse,
    LabelSubmitResponse,
)
```

Methods:

- <code title="post /label/update/{run_uuid}/{run_idx}">client.label.<a href="./src/structify/resources/label.py">update</a>(run_idx, \*, run_uuid, \*\*<a href="src/structify/types/label_update_params.py">params</a>) -> str</code>
- <code title="get /label/refresh">client.label.<a href="./src/structify/resources/label.py">get_messages</a>(\*\*<a href="src/structify/types/label_get_messages_params.py">params</a>) -> <a href="./src/structify/types/label_get_messages_response.py">Optional</a></code>
- <code title="get /label/llm_assist/{uuid}">client.label.<a href="./src/structify/resources/label.py">llm_assist</a>(uuid) -> <a href="./src/structify/types/label_llm_assist_response.py">LabelLlmAssistResponse</a></code>
- <code title="post /label/run_async">client.label.<a href="./src/structify/resources/label.py">run</a>(\*\*<a href="src/structify/types/label_run_params.py">params</a>) -> str</code>
- <code title="post /label/submit/{uuid}">client.label.<a href="./src/structify/resources/label.py">submit</a>(uuid, \*\*<a href="src/structify/types/label_submit_params.py">params</a>) -> str</code>

# Usage

Types:

```python
from structify.types import UsageGetJobInfoResponse
```

Methods:

- <code title="post /usage/get_job_info">client.usage.<a href="./src/structify/resources/usage.py">get_job_info</a>(\*\*<a href="src/structify/types/usage_get_job_info_params.py">params</a>) -> <a href="./src/structify/types/usage_get_job_info_response.py">UsageGetJobInfoResponse</a></code>
