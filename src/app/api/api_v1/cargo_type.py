from fastapi import APIRouter

from app.api.dependencies.cargo_type import CargoTypeServiceTxDep
from app.schemas.cargo_type import CargoTypeCreate, CargoTypeRead
from app.schemas.response import DataResponse, ListResponse
from core.config import settings

router = APIRouter(
    prefix=settings.api.v1.cargo_types,
    tags=["Cargo Types"],
)


@router.post(
    "",
    response_model=DataResponse[CargoTypeRead],
)
async def create_cargo_type(
    cargo_type_data: CargoTypeCreate,
    cargo_type_service: CargoTypeServiceTxDep,
) -> DataResponse[CargoTypeRead]:
    return DataResponse(
        data=await cargo_type_service.create(cargo_type_data),
    )


@router.get(
    "",
    response_model=ListResponse[CargoTypeRead],
)
async def get_cargo_types(
    cargo_type_service: CargoTypeServiceTxDep,
) -> ListResponse[CargoTypeRead]:
    return ListResponse(
        data=await cargo_type_service.get_cargo_types(),
    )
