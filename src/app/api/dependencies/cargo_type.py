from typing import Annotated

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.session_dep import SessionDep, TransactionSessionDep
from app.models.cargo_type import CargoType
from app.repositories.cargo_type import CargoTypeRepository
from app.services.cargo_type import CargoTypeService


async def get_cargo_type_service(
    session: Annotated[AsyncSession, SessionDep],
) -> CargoTypeService:
    repo = CargoTypeRepository(session, CargoType)
    return CargoTypeService(session, repo)


async def get_cargo_type_service_tx(
    session: Annotated[AsyncSession, TransactionSessionDep],
) -> CargoTypeService:
    repo = CargoTypeRepository(session, CargoType)
    return CargoTypeService(session, repo)


CargoTypeServiceDep = Annotated[CargoTypeService, Depends(get_cargo_type_service)]
CargoTypeServiceTxDep = Annotated[CargoTypeService, Depends(get_cargo_type_service_tx)]
