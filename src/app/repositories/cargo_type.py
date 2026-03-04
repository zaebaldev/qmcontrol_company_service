import logging
from typing import Type

from sqlalchemy.ext.asyncio import AsyncSession

from app.models.cargo_type import CargoType
from app.schemas.cargo_type import CargoTypeCreate, CargoTypeRead

from .base import BaseRepository

log = logging.getLogger(__name__)


class CargoTypeRepository(BaseRepository[CargoType]):
    def __init__(
        self,
        session: AsyncSession,
        model: Type[CargoType] = CargoType,
    ):
        super().__init__(session, model)

    async def create(
        self,
        cargo_type_data: CargoTypeCreate,
    ) -> CargoTypeRead:
        cargo_type = await self.add(
            instance=CargoType(
                **cargo_type_data.model_dump(),
            )
        )
        return CargoTypeRead.model_validate(cargo_type)
