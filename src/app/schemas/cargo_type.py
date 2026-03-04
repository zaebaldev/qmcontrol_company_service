from typing import Optional

from pydantic import BaseModel

from app.schemas.mixins.config_dict_mixin import FromAttributesMixin


class CargoTypeBase(BaseModel):
    catalogcode: str
    catalogname: Optional[str] = None
    productname: Optional[str] = None
    packagecode: str
    packagename: Optional[str] = None
    is_count: bool = True


class CargoTypeCreate(CargoTypeBase):
    pass


class CargoTypeRead(CargoTypeBase, FromAttributesMixin):
    pass
