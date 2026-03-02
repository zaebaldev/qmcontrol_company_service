from http import HTTPStatus
from typing import Any

import aiohttp

from core.config import settings
from core.exceptions.common import ExternalServiceError


class HttpClient:
    def __init__(
        self,
        base_url: str,
        timeout: int = 10,
    ):
        self.base_url = base_url.rstrip("/")
        self._timeout = aiohttp.ClientTimeout(total=timeout)
        self._session: aiohttp.ClientSession | None = None

    async def start(self) -> None:
        if self._session is None:
            self._session = aiohttp.ClientSession(
                timeout=self._timeout,
                connector=aiohttp.TCPConnector(limit=100),
            )

    async def close(self) -> None:
        if self._session and not self._session.closed:
            await self._session.close()

    async def post(
        self,
        path: str,
        *,
        data: dict[str, Any],
        headers: dict[str, str],
    ) -> dict[str, Any]:
        if not self._session:
            raise RuntimeError("HTTP client not started")

        url = f"{self.base_url}{path}"

        try:
            async with self._session.post(
                url,
                data=data,
                headers=headers,
            ) as response:
                text = await response.text()

                if response.status != HTTPStatus.OK:
                    raise ExternalServiceError(
                        f"External service error: {response.status} - {text}"
                    )

                try:
                    return await response.json()
                except Exception:
                    raise ExternalServiceError(
                        "Invalid JSON response from external service"
                    )

        except TimeoutError:
            raise ExternalServiceError("External service timeout")

        except aiohttp.ClientError as e:
            raise ExternalServiceError(
                f"Network error while connecting to external service: {e!s}"
            )


http_client = HttpClient(base_url=settings.didox.base_url)
