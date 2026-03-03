from typing import Annotated

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.session_dep import SessionDep, TransactionSessionDep
from app.models.quarry import Quarry
from app.repositories.quarry import QuarryRepository
from app.services.quarry import QuarryService


async def get_quarry_service(
    session: Annotated[AsyncSession, SessionDep],
) -> QuarryService:
    repo = QuarryRepository(session, Quarry)
    return QuarryService(session, repo)


async def get_quarry_service_tx(
    session: Annotated[AsyncSession, TransactionSessionDep],
) -> QuarryService:
    repo = QuarryRepository(session, Quarry)
    return QuarryService(session, repo)


QuarryServiceDep = Annotated[QuarryService, Depends(get_quarry_service)]
QuarryServiceTxDep = Annotated[QuarryService, Depends(get_quarry_service_tx)]
