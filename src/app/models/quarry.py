from typing import TYPE_CHECKING

from sqlalchemy import Text
from sqlalchemy.orm import Mapped, mapped_column

from app.models.base import Base
from app.models.mixins import NameMixin

if TYPE_CHECKING:
    pass


class Quarry(Base, NameMixin):
    _name_unique = True
    _name_primary_key = True
    image_url: Mapped[str] = mapped_column(
        Text,
        nullable=True,
    )
