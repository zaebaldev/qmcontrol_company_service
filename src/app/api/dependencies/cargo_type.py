from typing import Annotated

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.session_dep import SessionDep, TransactionSessionDep
from app.models.cargo_type import CargoType
from app.models.company_cargo_type import CompanyCargoType
from app.repositories.cargo_type import CargoTypeRepository
from app.repositories.company_cargo_type import CompanyCargoTypeRepository
from app.services.cargo_type import CargoTypeService


async def get_cargo_type_service(
    session: Annotated[AsyncSession, SessionDep],
) -> CargoTypeService:
    repo = CargoTypeRepository(session, CargoType)
    company_cargo_type_repo = CompanyCargoTypeRepository(session, CompanyCargoType)
    return CargoTypeService(session, repo, company_cargo_type_repo)


async def get_cargo_type_service_tx(
    session: Annotated[AsyncSession, TransactionSessionDep],
) -> CargoTypeService:
    repo = CargoTypeRepository(session, CargoType)
    company_cargo_type_repo = CompanyCargoTypeRepository(session, CompanyCargoType)
    return CargoTypeService(session, repo, company_cargo_type_repo)


CargoTypeServiceDep = Annotated[CargoTypeService, Depends(get_cargo_type_service)]
CargoTypeServiceTxDep = Annotated[CargoTypeService, Depends(get_cargo_type_service_tx)]
