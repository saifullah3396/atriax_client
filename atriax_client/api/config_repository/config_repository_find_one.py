from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.config_repository import ConfigRepository
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    username: Union[None, Unset, str] = UNSET,
    name: Union[None, Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_username: Union[None, Unset, str]
    if isinstance(username, Unset):
        json_username = UNSET
    else:
        json_username = username
    params["username"] = json_username

    json_name: Union[None, Unset, str]
    if isinstance(name, Unset):
        json_name = UNSET
    else:
        json_name = name
    params["name"] = json_name

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/config_repository/find_one/",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ConfigRepository, HTTPValidationError]]:
    if response.status_code == 200:
        response_200 = ConfigRepository.from_dict(response.json())

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
) -> Response[Union[ConfigRepository, HTTPValidationError]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    username: Union[None, Unset, str] = UNSET,
    name: Union[None, Unset, str] = UNSET,
) -> Response[Union[ConfigRepository, HTTPValidationError]]:
    """Find One

    Args:
        username (Union[None, Unset, str]):
        name (Union[None, Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ConfigRepository, HTTPValidationError]]
    """

    kwargs = _get_kwargs(
        username=username,
        name=name,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    username: Union[None, Unset, str] = UNSET,
    name: Union[None, Unset, str] = UNSET,
) -> Optional[Union[ConfigRepository, HTTPValidationError]]:
    """Find One

    Args:
        username (Union[None, Unset, str]):
        name (Union[None, Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ConfigRepository, HTTPValidationError]
    """

    return sync_detailed(
        client=client,
        username=username,
        name=name,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    username: Union[None, Unset, str] = UNSET,
    name: Union[None, Unset, str] = UNSET,
) -> Response[Union[ConfigRepository, HTTPValidationError]]:
    """Find One

    Args:
        username (Union[None, Unset, str]):
        name (Union[None, Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ConfigRepository, HTTPValidationError]]
    """

    kwargs = _get_kwargs(
        username=username,
        name=name,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    username: Union[None, Unset, str] = UNSET,
    name: Union[None, Unset, str] = UNSET,
) -> Optional[Union[ConfigRepository, HTTPValidationError]]:
    """Find One

    Args:
        username (Union[None, Unset, str]):
        name (Union[None, Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ConfigRepository, HTTPValidationError]
    """

    return (
        await asyncio_detailed(
            client=client,
            username=username,
            name=name,
        )
    ).parsed
