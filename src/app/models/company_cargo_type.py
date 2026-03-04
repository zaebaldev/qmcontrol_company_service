from decimal import Decimal

from sqlalchemy import ForeignKey, Numeric
from sqlalchemy.orm import Mapped, mapped_column

from app.models.base import Base
from app.models.mixins import CreatedAtMixin, IntIdMixin, NameMixin


class CompanyCargoType(Base, IntIdMixin, NameMixin, CreatedAtMixin):
    _name_primary_key = False
    company_tin: Mapped[str] = mapped_column(ForeignKey("companies.company_tin"))
    cargo_type_id: Mapped[str] = mapped_column(ForeignKey("cargo_types.catalogcode"))
    price_per_volume: Mapped[Decimal] = mapped_column(
        Numeric(15, 2),
        nullable=False,
        default=Decimal("0.00"),
        server_default="0.00",
    )
