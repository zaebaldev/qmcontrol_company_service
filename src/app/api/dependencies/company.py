from typing import Annotated

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.session_dep import SessionDep, TransactionSessionDep
from app.models.company import Company
from app.repositories.company import CompanyRepository
from app.services.company import CompanyService


async def get_company_service(
    session: Annotated[AsyncSession, SessionDep],
) -> CompanyService:
    repo = CompanyRepository(session, Company)
    return CompanyService(session, repo)


async def get_company_service_tx(
    session: Annotated[AsyncSession, TransactionSessionDep],
) -> CompanyService:
    repo = CompanyRepository(session, Company)
    return CompanyService(session, repo)


CompanyServiceDep = Annotated[CompanyService, Depends(get_company_service)]
CompanyServiceTxDep = Annotated[CompanyService, Depends(get_company_service_tx)]
