from http import HTTPStatus
from typing import Any, Optional, Union
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.dataset import Dataset
from ...models.dataset_processing_request_types import DatasetProcessingRequestTypes
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response


def _get_kwargs(
    id: UUID,
    branch: str,
    *,
    request_type: DatasetProcessingRequestTypes,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_request_type = request_type.value
    params["request_type"] = json_request_type

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": f"/api/v1/dataset/{id}/process/{branch}",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Dataset, HTTPValidationError]]:
    if response.status_code == 200:
        response_200 = Dataset.from_dict(response.json())

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
) -> Response[Union[Dataset, HTTPValidationError]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: UUID,
    branch: str,
    *,
    client: AuthenticatedClient,
    request_type: DatasetProcessingRequestTypes,
) -> Response[Union[Dataset, HTTPValidationError]]:
    """Process

    Args:
        id (UUID):
        branch (str):
        request_type (DatasetProcessingRequestTypes):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Dataset, HTTPValidationError]]
    """

    kwargs = _get_kwargs(
        id=id,
        branch=branch,
        request_type=request_type,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: UUID,
    branch: str,
    *,
    client: AuthenticatedClient,
    request_type: DatasetProcessingRequestTypes,
) -> Optional[Union[Dataset, HTTPValidationError]]:
    """Process

    Args:
        id (UUID):
        branch (str):
        request_type (DatasetProcessingRequestTypes):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Dataset, HTTPValidationError]
    """

    return sync_detailed(
        id=id,
        branch=branch,
        client=client,
        request_type=request_type,
    ).parsed


async def asyncio_detailed(
    id: UUID,
    branch: str,
    *,
    client: AuthenticatedClient,
    request_type: DatasetProcessingRequestTypes,
) -> Response[Union[Dataset, HTTPValidationError]]:
    """Process

    Args:
        id (UUID):
        branch (str):
        request_type (DatasetProcessingRequestTypes):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Dataset, HTTPValidationError]]
    """

    kwargs = _get_kwargs(
        id=id,
        branch=branch,
        request_type=request_type,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: UUID,
    branch: str,
    *,
    client: AuthenticatedClient,
    request_type: DatasetProcessingRequestTypes,
) -> Optional[Union[Dataset, HTTPValidationError]]:
    """Process

    Args:
        id (UUID):
        branch (str):
        request_type (DatasetProcessingRequestTypes):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Dataset, HTTPValidationError]
    """

    return (
        await asyncio_detailed(
            id=id,
            branch=branch,
            client=client,
            request_type=request_type,
        )
    ).parsed
