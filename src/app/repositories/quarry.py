import logging
from typing import Optional, Type

from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.quarry import Quarry
from app.schemas.quarry import QuarryRead

from .base import BaseRepository

log = logging.getLogger(__name__)


class QuarryRepository(BaseRepository[Quarry]):
    def __init__(
        self,
        session: AsyncSession,
        model: Type[Quarry] = Quarry,
    ):
        super().__init__(session, model)

    async def get_by_name(
        self,
        name: str,
    ) -> Quarry | None:
        """Get company by TIN."""
        return await self.find_one(
            filters=[
                Quarry.name == name,
            ],
        )

    async def create(
        self,
        name: str,
        image_url: Optional[str] = None,
    ) -> Quarry:
        """Create a new quarry."""
        return await self.add(
            instance=Quarry(
                name=name,
                image_url=image_url,
            ),
        )

    async def get_with_companies_count(
        self,
    ) -> list[QuarryRead]:
        query = text(
            """
            SELECT
                qr.name,
                qr.image_url,
                COUNT(cp.company_tin) AS companies_count
            FROM quarries qr
            LEFT JOIN companies cp ON qr.name = cp.quarry
            GROUP BY qr.name
            ORDER BY qr.name;
            """
        )
        result = await self.session.execute(query)
        rows = result.mappings().all()
        return [QuarryRead.model_validate(row) for row in rows]
