# Admin

## Users

Types:

```python
from structify.types.admin import UserNode, UserListResponse
```

Methods:

- <code title="get /admin/users/list">client.admin.users.<a href="./src/structify/resources/admin/users.py">list</a>() -> <a href="./src/structify/types/admin/user_list_response.py">UserListResponse</a></code>

# Dataset

Types:

```python
from structify.types import (
    DatasetDescriptor,
    DatasetNode,
    KgEntity,
    DatasetListResponse,
    DatasetViewEntriesResponse,
)
```

Methods:

- <code title="post /dataset/create">client.dataset.<a href="./src/structify/resources/dataset.py">create</a>(\*\*<a href="src/structify/types/dataset_create_params.py">params</a>) -> None</code>
- <code title="get /dataset/list">client.dataset.<a href="./src/structify/resources/dataset.py">list</a>() -> <a href="./src/structify/types/dataset_list_response.py">DatasetListResponse</a></code>
- <code title="delete /dataset/delete">client.dataset.<a href="./src/structify/resources/dataset.py">delete</a>(\*\*<a href="src/structify/types/dataset_delete_params.py">params</a>) -> None</code>
- <code title="get /dataset/info">client.dataset.<a href="./src/structify/resources/dataset.py">retrieve_info</a>(\*\*<a href="src/structify/types/dataset_retrieve_info_params.py">params</a>) -> <a href="./src/structify/types/dataset_descriptor.py">Optional</a></code>
- <code title="get /dataset/view">client.dataset.<a href="./src/structify/resources/dataset.py">view_entries</a>(\*\*<a href="src/structify/types/dataset_view_entries_params.py">params</a>) -> <a href="./src/structify/types/dataset_view_entries_response.py">DatasetViewEntriesResponse</a></code>

# Documents

Types:

```python
from structify.types import DocumentListResponse, DocumentDownloadFileIDResponse
```

Methods:

- <code title="get /documents/list">client.documents.<a href="./src/structify/resources/documents.py">list</a>() -> <a href="./src/structify/types/document_list_response.py">DocumentListResponse</a></code>
- <code title="delete /documents/delete/{path}">client.documents.<a href="./src/structify/resources/documents.py">delete_file_path</a>(path) -> None</code>
- <code title="get /documents/download/{id}">client.documents.<a href="./src/structify/resources/documents.py">download_file_id</a>(id) -> str</code>
- <code title="post /documents/upload">client.documents.<a href="./src/structify/resources/documents.py">upload</a>(\*\*<a href="src/structify/types/document_upload_params.py">params</a>) -> None</code>

# Server

Types:

```python
from structify.types import ServerInformation
```

Methods:

- <code title="get /server/version">client.server.<a href="./src/structify/resources/server.py">version</a>() -> <a href="./src/structify/types/server_information.py">ServerInformation</a></code>

# Source

Types:

```python
from structify.types import Source
```

Methods:

- <code title="get /source/get_sources">client.source.<a href="./src/structify/resources/source.py">list_sources</a>(\*\*<a href="src/structify/types/source_list_sources_params.py">params</a>) -> <a href="./src/structify/types/source.py">Source</a></code>

# Structure

Types:

```python
from structify.types import IsComplete, StructureExecuteResponse, StructureExecuteAsyncResponse
```

Methods:

- <code title="post /structure/run">client.structure.<a href="./src/structify/resources/structure.py">execute</a>(\*\*<a href="src/structify/types/structure_execute_params.py">params</a>) -> <a href="./src/structify/types/structure_execute_response.py">object</a></code>
- <code title="post /structure/run_async">client.structure.<a href="./src/structify/resources/structure.py">execute_async</a>(\*\*<a href="src/structify/types/structure_execute_async_params.py">params</a>) -> <a href="./src/structify/types/structure_execute_async_response.py">object</a></code>
- <code title="post /structure/is_complete">client.structure.<a href="./src/structify/resources/structure.py">mark_complete</a>(\*\*<a href="src/structify/types/structure_mark_complete_params.py">params</a>) -> <a href="./src/structify/types/is_complete.py">IsComplete</a></code>

# User

Types:

```python
from structify.types import NewToken
```

Methods:

- <code title="post /user/create_test_token">client.user.<a href="./src/structify/resources/user.py">create_test_token</a>() -> <a href="./src/structify/types/new_token.py">NewToken</a></code>
