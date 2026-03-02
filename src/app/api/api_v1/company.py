from fastapi import APIRouter

from app.schemas.company import CompanyCreate
from core.config import settings

router = APIRouter(
    prefix=settings.api.v1.prefix,
    tags=["Companies"],
)


@router.get("")
async def get_companies():
    return {"message": "Companies"}


@router.post("")
async def create_company(
    company_data: CompanyCreate,
):
    return {"message": "Companies"}
