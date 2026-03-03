from fastapi import APIRouter

from app.api.dependencies.quarry import QuarryServiceDep, QuarryServiceTxDep
from app.schemas.quarry import QuarryCreate, QuarryRead
from app.schemas.response import DataResponse, ListResponse
from core.config import settings

router = APIRouter(
    prefix=settings.api.v1.quarries,
    tags=["Quarries"],
)


@router.post(
    "",
    response_model=DataResponse[QuarryRead],
)
async def create_quarry(
    quarry_data: QuarryCreate,
    quarry_service: QuarryServiceTxDep,
):
    quarry = await quarry_service.create(quarry_data)
    return DataResponse(
        data=quarry,
    )


@router.get(
    "",
    response_model=ListResponse[QuarryRead],
)
async def get_quarries(
    quarry_service: QuarryServiceDep,
):
    quarries = await quarry_service.get_all()
    return ListResponse(
        data=quarries,
    )
