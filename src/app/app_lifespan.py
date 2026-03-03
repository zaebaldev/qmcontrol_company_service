from contextlib import asynccontextmanager
from typing import AsyncGenerator

from fastapi import FastAPI

from app.clients.http_client import http_client
from app.db.db_helper import db_helper

# from app.messaging.fs_broker import broker


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator[None, None]:
    # startup
    # await broker.start()
    await http_client.start()

    yield
    # shutdown
    await db_helper.dispose()
    # await broker.stop()
    await http_client.stop()
