from fastapi import APIRouter

from core.config import settings

from .company import router as company_router

router = APIRouter(
    prefix=settings.api.v1.prefix,
)
router.include_router(company_router)
