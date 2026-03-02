from sqlalchemy import Boolean
from sqlalchemy.orm import Mapped, declared_attr, mapped_column


class IsActiveMixin:
    @declared_attr
    def is_active(cls) -> Mapped[bool]:
        return mapped_column(
            Boolean,
            default=True,
            server_default="true",
        )
