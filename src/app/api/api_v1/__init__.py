from fastapi import APIRouter

from core.config import settings

from .camera import router as camera_router
from .cargo_type import router as cargo_type_router
from .company import router as company_router
from .quarry import router as quarry_rotuer

router = APIRouter(
    prefix=settings.api.v1.prefix,
)
router.include_router(quarry_rotuer)
router.include_router(company_router)
router.include_router(camera_router)
router.include_router(cargo_type_router)
