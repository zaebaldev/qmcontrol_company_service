import logging
from typing import Type

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.cargo_type import CargoType
from app.models.company_cargo_type import CompanyCargoType
from app.schemas.company_cargo_type import (
    CompanyCargoTypeCreateInternal,
    CompanyCargoTypeFullRead,
    CompanyCargoTypeRead,
)

from .base import BaseRepository

log = logging.getLogger(__name__)


class CompanyCargoTypeRepository(BaseRepository[CompanyCargoType]):
    def __init__(
        self,
        session: AsyncSession,
        model: Type[CompanyCargoType] = CompanyCargoType,
    ):
        super().__init__(session, model)

    async def create(
        self,
        cargo_type_data: CompanyCargoTypeCreateInternal,
    ) -> CompanyCargoTypeRead:
        cargo_type = await self.add(
            instance=CompanyCargoType(
                **cargo_type_data.model_dump(),
            )
        )

        return CompanyCargoTypeRead.model_validate(cargo_type)

    async def get_all_full(
        self,
        company_tin: str,
    ) -> list[CompanyCargoTypeFullRead]:
        stmt = (
            select(
                CompanyCargoType.id.label("id"),
                CompanyCargoType.company_tin,
                CompanyCargoType.catalogcode,
                CompanyCargoType.price_per_volume,
                CompanyCargoType.name,
                CargoType.catalogcode,
                CargoType.catalogname,
                CargoType.productname,
                CargoType.packagecode,
                CargoType.packagename,
            )
            .outerjoin(CargoType, CompanyCargoType.catalogcode == CargoType.catalogcode)
            .where(CompanyCargoType.company_tin == company_tin)
        )

        result = await self.session.execute(stmt)
        return [
            CompanyCargoTypeFullRead.model_validate(row)
            for row in result.mappings().all()
        ]
