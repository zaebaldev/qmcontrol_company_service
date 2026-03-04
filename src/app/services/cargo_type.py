import logging
from typing import TYPE_CHECKING

from sqlalchemy.ext.asyncio import AsyncSession

from app.repositories.cargo_type import CargoTypeRepository
from app.schemas.cargo_type import CargoTypeCreate, CargoTypeRead

if TYPE_CHECKING:
    pass

log = logging.getLogger(__name__)


class CargoTypeService:
    """Service for cargo type"""

    def __init__(
        self,
        session: AsyncSession,
        repo: CargoTypeRepository,
    ):
        self.session = session
        self.repo = repo

    async def create(
        self,
        cargo_type_data: CargoTypeCreate,
    ) -> CargoTypeRead:
        return await self.repo.create(cargo_type_data)

    async def get_cargo_types(self) -> list[CargoTypeRead]:
        cargo_types = await self.repo.get_all()
        if not cargo_types:
            return []
        return [CargoTypeRead.model_validate(cargo_type) for cargo_type in cargo_types]
