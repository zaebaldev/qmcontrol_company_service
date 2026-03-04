import logging
from typing import TYPE_CHECKING

from sqlalchemy.ext.asyncio import AsyncSession

from app.repositories.camera import CameraRepository
from app.schemas.camera import CameraCreate

if TYPE_CHECKING:
    from app.models.camera import Camera

log = logging.getLogger(__name__)


class CameraService:
    """Service for company operations."""

    def __init__(
        self,
        session: AsyncSession,
        repo: CameraRepository,
    ):
        self.session = session
        self.repo = repo

    async def get_all(self) -> list["Camera"]:
        """Get all cameras."""
        cameras = await self.repo.get_all()
        if cameras is None:
            return []
        return cameras

    async def create(
        self,
        camera_data: CameraCreate,
    ) -> "Camera":
        """Create a new camera."""
        return await self.repo.create(camera_data)
