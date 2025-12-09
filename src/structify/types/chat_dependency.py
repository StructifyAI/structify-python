# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["ChatDependency"]


class ChatDependency(BaseModel):
    """A chat session dependency"""

    package_name: str
    """Name of the Python package"""

    version_spec: Optional[str] = None
    """Optional version specifier (e.g., ">=1.0.0", "==2.0.0")"""
