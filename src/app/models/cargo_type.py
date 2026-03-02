from sqlalchemy import Boolean, String
from sqlalchemy.orm import Mapped, mapped_column

from app.models.base import Base


class CargoType(Base):
    catalogcode: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
        index=True,
        unique=True,
        primary_key=True,
    )
    catalogname: Mapped[str] = mapped_column(
        String(255),
        nullable=True,
    )
    productname: Mapped[str] = mapped_column(
        String(255),
        nullable=True,
    )
    packagecode: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
        index=True,
    )
    packagename: Mapped[str] = mapped_column(
        String(255),
        nullable=True,
    )
    is_count: Mapped[bool] = mapped_column(
        Boolean,
        default=True,
        server_default="true",
    )
