from http import HTTPStatus
from typing import Any, Optional, Union
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: UUID,
    branch: str,
    split: str,
    *,
    page: Union[Unset, int] = 0,
    page_size: Union[Unset, int] = 1,
    paginated: Union[Unset, bool] = True,
    order_by: Union[Unset, str] = "sample_id",
    order: Union[Unset, str] = "asc",
    search: Union[None, Unset, str] = UNSET,
    search_by: Union[None, Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["page"] = page

    params["page_size"] = page_size

    params["paginated"] = paginated

    params["order_by"] = order_by

    params["order"] = order

    json_search: Union[None, Unset, str]
    if isinstance(search, Unset):
        json_search = UNSET
    else:
        json_search = search
    params["search"] = json_search

    json_search_by: Union[None, Unset, str]
    if isinstance(search_by, Unset):
        json_search_by = UNSET
    else:
        json_search_by = search_by
    params["search_by"] = json_search_by

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/api/v1/dataset/{id}/table/{branch}/{split}",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, HTTPValidationError]]:
    if response.status_code == 200:
        response_200 = response.json()
        return response_200
    if response.status_code == 422:
        response_422 = HTTPValidationError.from_dict(response.json())

        return response_422
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Any, HTTPValidationError]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: UUID,
    branch: str,
    split: str,
    *,
    client: AuthenticatedClient,
    page: Union[Unset, int] = 0,
    page_size: Union[Unset, int] = 1,
    paginated: Union[Unset, bool] = True,
    order_by: Union[Unset, str] = "sample_id",
    order: Union[Unset, str] = "asc",
    search: Union[None, Unset, str] = UNSET,
    search_by: Union[None, Unset, str] = UNSET,
) -> Response[Union[Any, HTTPValidationError]]:
    """Get Table

    Args:
        id (UUID):
        branch (str):
        split (str):
        page (Union[Unset, int]):  Default: 0.
        page_size (Union[Unset, int]):  Default: 1.
        paginated (Union[Unset, bool]):  Default: True.
        order_by (Union[Unset, str]):  Default: 'sample_id'.
        order (Union[Unset, str]):  Default: 'asc'.
        search (Union[None, Unset, str]):
        search_by (Union[None, Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, HTTPValidationError]]
    """

    kwargs = _get_kwargs(
        id=id,
        branch=branch,
        split=split,
        page=page,
        page_size=page_size,
        paginated=paginated,
        order_by=order_by,
        order=order,
        search=search,
        search_by=search_by,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: UUID,
    branch: str,
    split: str,
    *,
    client: AuthenticatedClient,
    page: Union[Unset, int] = 0,
    page_size: Union[Unset, int] = 1,
    paginated: Union[Unset, bool] = True,
    order_by: Union[Unset, str] = "sample_id",
    order: Union[Unset, str] = "asc",
    search: Union[None, Unset, str] = UNSET,
    search_by: Union[None, Unset, str] = UNSET,
) -> Optional[Union[Any, HTTPValidationError]]:
    """Get Table

    Args:
        id (UUID):
        branch (str):
        split (str):
        page (Union[Unset, int]):  Default: 0.
        page_size (Union[Unset, int]):  Default: 1.
        paginated (Union[Unset, bool]):  Default: True.
        order_by (Union[Unset, str]):  Default: 'sample_id'.
        order (Union[Unset, str]):  Default: 'asc'.
        search (Union[None, Unset, str]):
        search_by (Union[None, Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, HTTPValidationError]
    """

    return sync_detailed(
        id=id,
        branch=branch,
        split=split,
        client=client,
        page=page,
        page_size=page_size,
        paginated=paginated,
        order_by=order_by,
        order=order,
        search=search,
        search_by=search_by,
    ).parsed


async def asyncio_detailed(
    id: UUID,
    branch: str,
    split: str,
    *,
    client: AuthenticatedClient,
    page: Union[Unset, int] = 0,
    page_size: Union[Unset, int] = 1,
    paginated: Union[Unset, bool] = True,
    order_by: Union[Unset, str] = "sample_id",
    order: Union[Unset, str] = "asc",
    search: Union[None, Unset, str] = UNSET,
    search_by: Union[None, Unset, str] = UNSET,
) -> Response[Union[Any, HTTPValidationError]]:
    """Get Table

    Args:
        id (UUID):
        branch (str):
        split (str):
        page (Union[Unset, int]):  Default: 0.
        page_size (Union[Unset, int]):  Default: 1.
        paginated (Union[Unset, bool]):  Default: True.
        order_by (Union[Unset, str]):  Default: 'sample_id'.
        order (Union[Unset, str]):  Default: 'asc'.
        search (Union[None, Unset, str]):
        search_by (Union[None, Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, HTTPValidationError]]
    """

    kwargs = _get_kwargs(
        id=id,
        branch=branch,
        split=split,
        page=page,
        page_size=page_size,
        paginated=paginated,
        order_by=order_by,
        order=order,
        search=search,
        search_by=search_by,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: UUID,
    branch: str,
    split: str,
    *,
    client: AuthenticatedClient,
    page: Union[Unset, int] = 0,
    page_size: Union[Unset, int] = 1,
    paginated: Union[Unset, bool] = True,
    order_by: Union[Unset, str] = "sample_id",
    order: Union[Unset, str] = "asc",
    search: Union[None, Unset, str] = UNSET,
    search_by: Union[None, Unset, str] = UNSET,
) -> Optional[Union[Any, HTTPValidationError]]:
    """Get Table

    Args:
        id (UUID):
        branch (str):
        split (str):
        page (Union[Unset, int]):  Default: 0.
        page_size (Union[Unset, int]):  Default: 1.
        paginated (Union[Unset, bool]):  Default: True.
        order_by (Union[Unset, str]):  Default: 'sample_id'.
        order (Union[Unset, str]):  Default: 'asc'.
        search (Union[None, Unset, str]):
        search_by (Union[None, Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, HTTPValidationError]
    """

    return (
        await asyncio_detailed(
            id=id,
            branch=branch,
            split=split,
            client=client,
            page=page,
            page_size=page_size,
            paginated=paginated,
            order_by=order_by,
            order=order,
            search=search,
            search_by=search_by,
        )
    ).parsed
