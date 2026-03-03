import logging
from typing import TYPE_CHECKING

from sqlalchemy.ext.asyncio import AsyncSession

from app.repositories.quarry import QuarryRepository
from app.schemas.quarry import QuarryCreate, QuarryRead
from core.exceptions.common import NotFoundError

log = logging.getLogger(__name__)

if TYPE_CHECKING:
    from app.models.quarry import Quarry

HTTP_OK = 200


class QuarryService:
    def __init__(
        self,
        session: AsyncSession,
        repo: QuarryRepository,
    ):
        self.session = session
        self.repo = repo

    async def get_by_name(
        self,
        name: str,
    ) -> "Quarry | None":
        quarry = await self.repo.get_by_name(name=name)
        if quarry is None:
            raise NotFoundError(
                message="Quarry not found",
            )
        return quarry

    async def create(
        self,
        quarry_data: QuarryCreate,
    ) -> "Quarry":
        return await self.repo.create(
            name=quarry_data.name,
            image_url=quarry_data.image_url,
        )

    async def get_all(
        self,
    ) -> list[QuarryRead] | None:
        quarries = await self.repo.get_with_companies_count()
        if quarries is None:
            return []
        return quarries
