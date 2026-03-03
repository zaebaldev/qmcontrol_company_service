import logging
from typing import Type

from sqlalchemy.ext.asyncio import AsyncSession

from app.models.company import Company

from .base import BaseRepository

log = logging.getLogger(__name__)


class CompanyRepository(BaseRepository[Company]):
    def __init__(
        self,
        session: AsyncSession,
        model: Type[Company] = Company,
    ):
        super().__init__(session, model)

    async def get_by_tin(
        self,
        company_tin: str,
    ) -> Company | None:
        """Get company by TIN."""
        return await self.find_one(
            filters=[
                Company.company_tin == company_tin,
            ],
        )

    async def create(
        self,
        company: Company,
    ) -> Company:
        """Create a new company."""
        return await self.add(instance=company)
