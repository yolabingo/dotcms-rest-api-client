from typing import Any, Dict, Union

import httpx

from ...client import Client
from ...types import UNSET, Response, Unset


def _get_kwargs(
    layout_id: str,
    *,
    client: Client,
    userid: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    url = "{}/v1/toolgroups/{layoutId}/_addtouser".format(client.base_url, layoutId=layout_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["userid"] = userid

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "put",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _build_response(*, response: httpx.Response) -> Response[Any]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=None,
    )


def sync_detailed(
    layout_id: str,
    *,
    client: Client,
    userid: Union[Unset, None, str] = UNSET,
) -> Response[Any]:
    """
    Args:
        layout_id (str):
        userid (Union[Unset, None, str]):

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        layout_id=layout_id,
        client=client,
        userid=userid,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


async def asyncio_detailed(
    layout_id: str,
    *,
    client: Client,
    userid: Union[Unset, None, str] = UNSET,
) -> Response[Any]:
    """
    Args:
        layout_id (str):
        userid (Union[Unset, None, str]):

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        layout_id=layout_id,
        client=client,
        userid=userid,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)
