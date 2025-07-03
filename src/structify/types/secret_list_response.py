# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .project_secret_summary import ProjectSecretSummary

__all__ = ["SecretListResponse"]

SecretListResponse: TypeAlias = List[ProjectSecretSummary]
