from decimal import Decimal
from typing import Optional

from pydantic import BaseModel

from app.schemas.cargo_type import CargoTypeBase
from app.schemas.mixins.config_dict_mixin import FromAttributesMixin


class CompanyCargoTypeBase(BaseModel):
    catalogcode: str
    price_per_volume: Optional[Decimal] = Decimal(0)
    name: str


class CompanyCargoTypeCreate(CompanyCargoTypeBase):
    pass


class CompanyCargoTypeCreateInternal(CompanyCargoTypeBase):
    company_tin: str


class CompanyCargoTypeRead(CompanyCargoTypeBase, FromAttributesMixin):
    id: int
    company_tin: str


class CompanyCargoTypeFullRead(
    CompanyCargoTypeBase, CargoTypeBase, FromAttributesMixin
):
    id: int
    company_tin: str


class CompanyCargoTypeUpdate(BaseModel):
    name: Optional[str] = None
    price_per_volume: Optional[Decimal] = None
