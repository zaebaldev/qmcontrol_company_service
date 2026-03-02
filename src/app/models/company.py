from sqlalchemy import Boolean, Integer, String, Text
from sqlalchemy.orm import Mapped, mapped_column

from app.models.base import Base
from app.models.mixins import CoordinatesMixin, IsActiveMixin, PhoneNumberMixin


class Company(Base, PhoneNumberMixin, IsActiveMixin, CoordinatesMixin):
    _phone_number_nullable = True
    _phone_number_unique = False
    _phone_number_index = False
    quarry_id: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
    )
    company_tin: Mapped[str] = mapped_column(
        String(24),
        unique=True,
        index=True,
        primary_key=True,
    )
    # --- Основная информация ---
    short_name: Mapped[str | None] = mapped_column(String(512), nullable=True)
    full_name: Mapped[str | None] = mapped_column(String(1024), nullable=True)
    reg_date: Mapped[str | None] = mapped_column(String(255), nullable=True)
    status_code: Mapped[str | None] = mapped_column(String(50), nullable=True)
    status_name: Mapped[str | None] = mapped_column(String(255), nullable=True)

    # --- Банковская информация ---
    account: Mapped[str | None] = mapped_column(String(255), nullable=True)
    bank_account: Mapped[str | None] = mapped_column(String(255), nullable=True)
    bank_code: Mapped[str | None] = mapped_column(String(255), nullable=True)
    mfo: Mapped[str | None] = mapped_column(String(255), nullable=True)

    # --- Налоговая информация ---
    vat_code: Mapped[str | None] = mapped_column(String(255), nullable=True)
    has_vat: Mapped[bool] = mapped_column(
        Boolean,
        default=True,
        server_default="true",
        nullable=False,
    )

    # --- Руководитель и бухгалтер ---
    director: Mapped[str | None] = mapped_column(String(512), nullable=True)
    director_tin: Mapped[str | None] = mapped_column(String(255), nullable=True)
    director_pinfl: Mapped[str | None] = mapped_column(String(255), nullable=True)
    accountant: Mapped[str | None] = mapped_column(String(512), nullable=True)

    # --- Прочее ---
    address: Mapped[str | None] = mapped_column(Text, nullable=True)
