from fastapi import APIRouter

from core.config import settings

from .company import router as company_router
from .quarry import router as quarry_rotuer

router = APIRouter(
    prefix=settings.api.v1.prefix,
)
router.include_router(quarry_rotuer)
router.include_router(company_router)
