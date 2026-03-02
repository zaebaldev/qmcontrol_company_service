from typing import Annotated, Optional

from pydantic import BaseModel, Field


class PhoneNumberMixin(BaseModel):
    phone_number: Annotated[
        str,
        Field(
            pattern=r"^[1-9]\d{1,14}$",
            examples=["998991234567"],
        ),
    ]


class PhoneNumberReadMixin(BaseModel):
    phone_number: str


class PhoneNumberUpdateMixin(BaseModel):
    phone_number: Annotated[
        str | None,
        Field(
            pattern=r"^[1-9]\d{1,14}$",
            examples=["998991112233"],
            default=None,
        ),
    ]


class PhoneNumberFilterMixin(BaseModel):
    phone_number: Optional[str] = None
