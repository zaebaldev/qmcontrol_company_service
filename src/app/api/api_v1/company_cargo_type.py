from fastapi import APIRouter, Depends

from app.api.dependencies.auth import UserClaims, require_company_admin
from app.api.dependencies.cargo_type import CargoTypeServiceDep, CargoTypeServiceTxDep
from app.schemas.company_cargo_type import (
    CompanyCargoTypeCreate,
    CompanyCargoTypeCreateInternal,
    CompanyCargoTypeFullRead,
    CompanyCargoTypeRead,
)
from app.schemas.response import DataResponse, ListResponse
from core.config import settings

router = APIRouter(
    prefix=settings.api.v1.companies,
    tags=["Company Cargo Types"],
)


@router.post(
    "/cargo_types",
    response_model=DataResponse[CompanyCargoTypeRead],
)
async def create_company_cargo_type(
    company_cargo_type_data: CompanyCargoTypeCreate,
    cargo_type_service: CargoTypeServiceTxDep,
    company_admin: UserClaims = Depends(require_company_admin),
):
    return DataResponse(
        data=await cargo_type_service.add_company_cargo_type(
            CompanyCargoTypeCreateInternal(
                **company_cargo_type_data.model_dump(),
                company_tin=company_admin.sub,
            ),
        ),
    )


@router.get(
    "/cargo_types",
    response_model=ListResponse[CompanyCargoTypeFullRead],
)
async def get_company_cargo_types(
    cargo_type_service: CargoTypeServiceDep,
    company_admin: UserClaims = Depends(require_company_admin),
):
    return DataResponse(
        data=await cargo_type_service.get_company_cargo_types(
            company_admin.sub,
        ),
    )
