from typing import Optional

from pydantic import BaseModel

from .mixins import FromAttributesMixin


class CameraBase(BaseModel):
    name: str
    quarry: str
    camera_path: str
    company_tin: Optional[str] = None
    latitude: Optional[float] = None
    longitude: Optional[float] = None


class CameraCreate(CameraBase):
    pass


class CameraRead(CameraBase, FromAttributesMixin):
    camera_url: Optional[str] = None
    is_active: bool = True
