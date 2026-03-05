from typing import Optional

from pydantic import BaseModel, field_validator

from app.schemas.mixins.config_dict_mixin import FromAttributesMixin


class CompanyBase(BaseModel):
    # --- Основная информация ---
    phone_number: str
    name: Optional[str] = None
    short_name: Optional[str] = None
    full_name: Optional[str] = None
    reg_date: Optional[str] = None
    status_code: Optional[str] = None
    status_name: Optional[str] = None

    # --- Банковская информация ---
    account: Optional[str] = None
    bank_account: Optional[str] = None
    bank_code: Optional[str] = None
    mfo: Optional[str] = None

    # --- Налоговая информация ---
    vat_code: Optional[str] = None
    has_vat: Optional[bool] = False

    # --- Руководитель и бухгалтер ---
    director: Optional[str] = None
    director_tin: Optional[str] = None
    director_pinfl: Optional[str] = None
    accountant: Optional[str] = None

    # --- Прочее ---
    address: Optional[str] = None

    # --- Геолокация ---
    latitude: Optional[float] = None
    longitude: Optional[float] = None

    @field_validator("status_code", mode="before")
    def convert_to_str(cls, value):
        if value is None:
            return value
        return str(value)


class CompanyCreate(CompanyBase):
    company_tin: str
    quarry: str


class CompanyRead(CompanyBase, FromAttributesMixin):
    company_tin: str
    quarry: Optional[str] = None
    is_active: Optional[bool] = None
