from sqlalchemy import Enum as SqlEnum
from sqlalchemy import ForeignKey, String, text
from sqlalchemy.orm import Mapped, mapped_column

from app.models.base import Base
from app.models.mixins import CoordinatesMixin, NameMixin
from core.enums.car_position import CarPositionEnum


class Camera(Base, NameMixin, CoordinatesMixin):
    _name_primary_key = True
    _name_unique = True
    quarry_id: Mapped[int] = mapped_column(
        ForeignKey("quarries.id"),
    )
    company_tin: Mapped[str] = mapped_column(
        ForeignKey("companies.company_tin"),
        nullable=True,
    )
    camera_path: Mapped[str] = mapped_column(
        String,
        nullable=False,
        unique=True,
        index=True,
    )
    entry_car_position: Mapped[str] = mapped_column(
        SqlEnum(CarPositionEnum, name="car_position_enum"),
        default=CarPositionEnum.FORWARD,
        server_default=text("'FORWARD'"),
        nullable=False,
    )
