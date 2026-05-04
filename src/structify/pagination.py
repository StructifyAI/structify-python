# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Any, List, Type, Generic, Mapping, TypeVar, Optional, cast
from typing_extensions import override

from httpx import Response

from ._utils import is_mapping
from ._models import BaseModel
from .types.event import Event
from ._base_client import BasePage, PageInfo, BaseSyncPage, BaseAsyncPage

__all__ = [
    "SyncAnalyticsEvents",
    "AsyncAnalyticsEvents",
    "SyncJobsList",
    "AsyncJobsList",
    "SyncListConnectorCatalog",
    "AsyncListConnectorCatalog",
]

_BaseModelT = TypeVar("_BaseModelT", bound=BaseModel)

_T = TypeVar("_T")


class SyncAnalyticsEvents(BaseSyncPage[_T], BasePage[_T], Generic[_T]):
    items: Optional[Event] = None
    next_cursor: Optional[str] = None

    @override
    def _get_page_items(self) -> List[_T]:
        data = self.data
        return data

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        next_cursor = self.next_cursor
        if not next_cursor:
            return None

        return PageInfo(params={"cursor": next_cursor})


class AsyncAnalyticsEvents(BaseAsyncPage[_T], BasePage[_T], Generic[_T]):
    items: Optional[Event] = None
    next_cursor: Optional[str] = None

    @override
    def _get_page_items(self) -> List[_T]:
        data = self.data
        return data

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        next_cursor = self.next_cursor
        if not next_cursor:
            return None

        return PageInfo(params={"cursor": next_cursor})


class SyncJobsList(BaseSyncPage[_T], BasePage[_T], Generic[_T]):
    items: List[_T]

    @override
    def _get_page_items(self) -> List[_T]:
        items = self.items
        if not items:
            return []
        return items

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        offset = self._options.params.get("offset") or 0
        if not isinstance(offset, int):
            raise ValueError(f'Expected "offset" param to be an integer but got {offset}')

        length = len(self._get_page_items())
        current_count = offset + length

        return PageInfo(params={"offset": current_count})

    @classmethod
    def build(cls: Type[_BaseModelT], *, response: Response, data: object) -> _BaseModelT:  # noqa: ARG003
        return cls.construct(
            None,
            **{
                **(cast(Mapping[str, Any], data) if is_mapping(data) else {"items": data}),
            },
        )


class AsyncJobsList(BaseAsyncPage[_T], BasePage[_T], Generic[_T]):
    items: List[_T]

    @override
    def _get_page_items(self) -> List[_T]:
        items = self.items
        if not items:
            return []
        return items

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        offset = self._options.params.get("offset") or 0
        if not isinstance(offset, int):
            raise ValueError(f'Expected "offset" param to be an integer but got {offset}')

        length = len(self._get_page_items())
        current_count = offset + length

        return PageInfo(params={"offset": current_count})

    @classmethod
    def build(cls: Type[_BaseModelT], *, response: Response, data: object) -> _BaseModelT:  # noqa: ARG003
        return cls.construct(
            None,
            **{
                **(cast(Mapping[str, Any], data) if is_mapping(data) else {"items": data}),
            },
        )


class SyncListConnectorCatalog(BaseSyncPage[_T], BasePage[_T], Generic[_T]):
    items: List[_T]

    @override
    def _get_page_items(self) -> List[_T]:
        items = self.items
        if not items:
            return []
        return items

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        offset = self._options.params.get("offset") or 0
        if not isinstance(offset, int):
            raise ValueError(f'Expected "offset" param to be an integer but got {offset}')

        length = len(self._get_page_items())
        current_count = offset + length

        return PageInfo(params={"offset": current_count})

    @classmethod
    def build(cls: Type[_BaseModelT], *, response: Response, data: object) -> _BaseModelT:  # noqa: ARG003
        return cls.construct(
            None,
            **{
                **(cast(Mapping[str, Any], data) if is_mapping(data) else {"items": data}),
            },
        )


class AsyncListConnectorCatalog(BaseAsyncPage[_T], BasePage[_T], Generic[_T]):
    items: List[_T]

    @override
    def _get_page_items(self) -> List[_T]:
        items = self.items
        if not items:
            return []
        return items

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        offset = self._options.params.get("offset") or 0
        if not isinstance(offset, int):
            raise ValueError(f'Expected "offset" param to be an integer but got {offset}')

        length = len(self._get_page_items())
        current_count = offset + length

        return PageInfo(params={"offset": current_count})

    @classmethod
    def build(cls: Type[_BaseModelT], *, response: Response, data: object) -> _BaseModelT:  # noqa: ARG003
        return cls.construct(
            None,
            **{
                **(cast(Mapping[str, Any], data) if is_mapping(data) else {"items": data}),
            },
        )
