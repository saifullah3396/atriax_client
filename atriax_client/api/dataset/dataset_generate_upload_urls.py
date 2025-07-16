from http import HTTPStatus
from typing import Any, Optional, Union
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.body_dataset_generate_upload_urls import BodyDatasetGenerateUploadUrls
from ...models.http_validation_error import HTTPValidationError
from ...models.pre_signed_url_response import PreSignedUrlResponse
from ...types import Response


def _get_kwargs(
    id: UUID,
    branch: str,
    *,
    body: BodyDatasetGenerateUploadUrls,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": f"/api/v1/dataset/{id}/generate_upload_urls/{branch}/",
    }

    _kwargs["data"] = body.to_dict()

    headers["Content-Type"] = "application/x-www-form-urlencoded"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[HTTPValidationError, PreSignedUrlResponse]]:
    if response.status_code == 200:
        response_200 = PreSignedUrlResponse.from_dict(response.json())

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
) -> Response[Union[HTTPValidationError, PreSignedUrlResponse]]:
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
    body: BodyDatasetGenerateUploadUrls,
) -> Response[Union[HTTPValidationError, PreSignedUrlResponse]]:
    """Generate Upload Urls

    Args:
        id (UUID):
        branch (str):
        body (BodyDatasetGenerateUploadUrls):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, PreSignedUrlResponse]]
    """

    kwargs = _get_kwargs(
        id=id,
        branch=branch,
        body=body,
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
    body: BodyDatasetGenerateUploadUrls,
) -> Optional[Union[HTTPValidationError, PreSignedUrlResponse]]:
    """Generate Upload Urls

    Args:
        id (UUID):
        branch (str):
        body (BodyDatasetGenerateUploadUrls):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, PreSignedUrlResponse]
    """

    return sync_detailed(
        id=id,
        branch=branch,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    id: UUID,
    branch: str,
    *,
    client: AuthenticatedClient,
    body: BodyDatasetGenerateUploadUrls,
) -> Response[Union[HTTPValidationError, PreSignedUrlResponse]]:
    """Generate Upload Urls

    Args:
        id (UUID):
        branch (str):
        body (BodyDatasetGenerateUploadUrls):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, PreSignedUrlResponse]]
    """

    kwargs = _get_kwargs(
        id=id,
        branch=branch,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: UUID,
    branch: str,
    *,
    client: AuthenticatedClient,
    body: BodyDatasetGenerateUploadUrls,
) -> Optional[Union[HTTPValidationError, PreSignedUrlResponse]]:
    """Generate Upload Urls

    Args:
        id (UUID):
        branch (str):
        body (BodyDatasetGenerateUploadUrls):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, PreSignedUrlResponse]
    """

    return (
        await asyncio_detailed(
            id=id,
            branch=branch,
            client=client,
            body=body,
        )
    ).parsed
