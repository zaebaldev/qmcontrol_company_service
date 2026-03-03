import asyncio
import logging
from typing import Any, Optional

import aiohttp

logger = logging.getLogger(__name__)


class AiohttpClient:
    """
    Async HTTP client без base_url.
    Работает только с полными URL.
    Поддерживает connection pool и lifecycle.
    """

    def __init__(
        self,
        timeout: int = 30,
        pool_size: int = 100,
        ssl: bool = False,
        default_headers: Optional[dict] = None,
    ):
        self.timeout = aiohttp.ClientTimeout(total=timeout)
        self.pool_size = pool_size
        self.ssl = ssl
        self.default_headers = default_headers or {"User-Agent": "AiohttpClient/1.0"}

        self._session: Optional[aiohttp.ClientSession] = None
        self._connector: Optional[aiohttp.TCPConnector] = None

    # -------------------------------------------------------------------------
    # Lifecycle
    # -------------------------------------------------------------------------

    async def start(self) -> None:
        """Создать connector и сессию."""
        if self._session and not self._session.closed:
            logger.warning("Client already started")
            return

        self._connector = aiohttp.TCPConnector(
            limit=self.pool_size,
            limit_per_host=20,
            ttl_dns_cache=300,
            ssl=self.ssl,
            enable_cleanup_closed=True,
        )

        self._session = aiohttp.ClientSession(
            connector=self._connector,
            timeout=self.timeout,
            headers=self.default_headers,
            raise_for_status=False,
        )

        logger.info("AiohttpClient started (pool_size=%d)", self.pool_size)

    async def stop(self) -> None:
        """Закрыть сессию."""
        if self._session and not self._session.closed:
            await self._session.close()
            logger.info("AiohttpClient stopped")

        await asyncio.sleep(0.25)

    async def __aenter__(self) -> "AiohttpClient":
        await self.start()
        return self

    async def __aexit__(self, *_) -> None:
        await self.stop()

    # -------------------------------------------------------------------------
    # Core request
    # -------------------------------------------------------------------------

    async def _request(
        self,
        method: str,
        url: str,
        *,
        params: Optional[dict] = None,
        json: Optional[Any] = None,
        data: Optional[Any] = None,
        headers: Optional[dict] = None,
        timeout: Optional[int] = None,
        **kwargs,
    ) -> dict:
        if not url.startswith("http"):
            raise ValueError("URL must be absolute (start with http/https)")

        if self._session is None or self._session.closed:
            raise RuntimeError("Client is not started. Call await client.start()")

        request_timeout = (
            aiohttp.ClientTimeout(total=timeout) if timeout else self.timeout
        )

        try:
            async with self._session.request(
                method,
                url,
                params=params,
                json=json,
                data=data,
                headers=headers,
                timeout=request_timeout,
                **kwargs,
            ) as response:
                content_type = response.content_type or ""

                if "application/json" in content_type:
                    body = await response.json()
                else:
                    body = await response.text()

                return {
                    "status": response.status,
                    "headers": dict(response.headers),
                    "body": body,
                    "ok": response.status < 400,
                }

        except aiohttp.ClientConnectorError as e:
            logger.error("Connection error [%s %s]: %s", method, url, e)
            raise
        except asyncio.TimeoutError:
            logger.error("Timeout [%s %s]", method, url)
            raise

    # -------------------------------------------------------------------------
    # HTTP methods
    # -------------------------------------------------------------------------

    async def get(self, url: str, **kwargs) -> dict:
        return await self._request("GET", url, **kwargs)

    async def post(self, url: str, **kwargs) -> dict:
        return await self._request("POST", url, **kwargs)

    async def put(self, url: str, **kwargs) -> dict:
        return await self._request("PUT", url, **kwargs)

    async def patch(self, url: str, **kwargs) -> dict:
        return await self._request("PATCH", url, **kwargs)

    async def delete(self, url: str, **kwargs) -> dict:
        return await self._request("DELETE", url, **kwargs)

    # -------------------------------------------------------------------------
    # Pool info
    # -------------------------------------------------------------------------

    @property
    def pool_info(self) -> dict:
        if not self._connector:
            return {"status": "not started"}

        return {
            "limit": self._connector.limit,
            "limit_per_host": self._connector.limit_per_host,
            "acquired": len(self._connector._acquired),
            "closed": self._connector.closed,
        }


http_client = AiohttpClient(pool_size=200)
