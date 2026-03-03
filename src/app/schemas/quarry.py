from typing import Optional

from pydantic import BaseModel

from app.schemas.mixins.config_dict_mixin import FromAttributesMixin


class QuarryBase(BaseModel):
    image_url: Optional[str] = None


class QuarryCreate(QuarryBase):
    name: str


class QuarryRead(QuarryBase, FromAttributesMixin):
    name: str
    companies_count: Optional[int] = 0
