# External services namespace for Structify Python client

from __future__ import annotations

from .whitelabel import WhitelabelResource
from .search import SearchResource
from .._compat import cached_property

__all__ = ["ExternalResource"]


class ExternalResource(WhitelabelResource):
    """
    Container for all external/whitelabel services.
    
    This provides a namespace for external services that are
    separate from the core Structify functionality.
    """
    
    @cached_property
    def search(self) -> SearchResource:
        """Access the search service."""
        return SearchResource(self._client)