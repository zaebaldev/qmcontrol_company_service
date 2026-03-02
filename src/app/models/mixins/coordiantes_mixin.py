from sqlalchemy import Float
from sqlalchemy.orm import Mapped, mapped_column


class CoordinatesMixin:
    latitude: Mapped[float | None] = mapped_column(
        Float,
        nullable=True,
        comment="Широта",
    )
    longitude: Mapped[float | None] = mapped_column(
        Float,
        nullable=True,
        comment="Долгота",
    )
