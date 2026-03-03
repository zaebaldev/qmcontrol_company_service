import logging

from sqlalchemy.ext.asyncio import AsyncSession

from app.models.company import Company
from app.repositories.company import CompanyRepository
from app.schemas.company import CompanyCreate, CompanyRead
from core.exceptions.common import NotFoundError

log = logging.getLogger(__name__)


HTTP_OK = 200


class CompanyService:
    """Service for company operations."""

    def __init__(
        self,
        session: AsyncSession,
        repo: CompanyRepository,
    ):
        self.session = session
        self.repo = repo

    async def get_by_tin(
        self,
        company_tin: str,
    ) -> CompanyRead:
        company = await self.repo.get_by_tin(company_tin=company_tin)
        if company is None:
            raise NotFoundError(
                message="Company not found",
            )
        return CompanyRead.model_validate(company)

    async def create(
        self,
        company_data: CompanyCreate,
    ) -> CompanyRead:
        company = Company(
            company_tin=company_data.company_tin,
            quarry=company_data.quarry,
            name=company_data.name,
            short_name=company_data.short_name,
            full_name=company_data.full_name,
            reg_date=company_data.reg_date,
            status_code=company_data.status_code,
            status_name=company_data.status_name,
            account=company_data.account,
            bank_account=company_data.bank_account,
            bank_code=company_data.bank_code,
            mfo=company_data.mfo,
            vat_code=company_data.vat_code,
            has_vat=company_data.has_vat,
            director=company_data.director,
            director_tin=company_data.director_tin,
            director_pinfl=company_data.director_pinfl,
            accountant=company_data.accountant,
            address=company_data.address,
            latitude=company_data.latitude,
            longitude=company_data.longitude,
        )
        created_company = await self.repo.create(company)
        return CompanyRead.model_validate(created_company)

    async def get_all(self) -> list[CompanyRead]:
        companies = await self.repo.get_all()
        if companies is None:
            return []
        return [CompanyRead.model_validate(company) for company in companies]
