import logging
from typing import Type

from sqlalchemy.ext.asyncio import AsyncSession

from app.models.camera import Camera
from app.schemas.camera import CameraCreate

from .base import BaseRepository

log = logging.getLogger(__name__)


class CameraRepository(BaseRepository[Camera]):
    def __init__(
        self,
        session: AsyncSession,
        model: Type[Camera] = Camera,
    ):
        super().__init__(session, model)

    async def create(
        self,
        camera: CameraCreate,
    ) -> Camera:
        return await self.add(
            Camera(
                **camera.model_dump(),
            )
        )
