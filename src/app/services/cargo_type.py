import logging
from typing import TYPE_CHECKING

from sqlalchemy.ext.asyncio import AsyncSession

from app.repositories.cargo_type import CargoTypeRepository
from app.repositories.company_cargo_type import (
    CompanyCargoTypeRepository,
)
from app.schemas.cargo_type import CargoTypeCreate, CargoTypeRead
from app.schemas.company_cargo_type import (
    CompanyCargoTypeCreateInternal,
    CompanyCargoTypeFullRead,
    CompanyCargoTypeRead,
)

if TYPE_CHECKING:
    pass

log = logging.getLogger(__name__)


class CargoTypeService:
    """Service for cargo type"""

    def __init__(
        self,
        session: AsyncSession,
        repo: CargoTypeRepository,
        company_cargo_type_repo: CompanyCargoTypeRepository,
    ):
        self.session = session
        self.repo = repo
        self.company_cargo_type_repo = company_cargo_type_repo

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

    async def add_company_cargo_type(
        self,
        company_cargo_type_data: CompanyCargoTypeCreateInternal,
    ) -> CompanyCargoTypeRead:
        return await self.company_cargo_type_repo.create(company_cargo_type_data)

    async def get_company_cargo_types(
        self,
        company_tin: str,
    ) -> list[CompanyCargoTypeFullRead]:
        company_cargos = await self.company_cargo_type_repo.get_all_full(
            company_tin,
        )
        if not company_cargos:
            return []
        return company_cargos
