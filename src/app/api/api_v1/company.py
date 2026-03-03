from fastapi import APIRouter

from app.api.dependencies.company import CompanyServiceDep, CompanyServiceTxDep
from app.schemas.company import CompanyCreate, CompanyRead
from app.schemas.response import DataResponse, ListResponse
from core.config import settings

router = APIRouter(
    prefix=settings.api.v1.companies,
    tags=["Companies"],
)


@router.post(
    "",
    response_model=DataResponse[CompanyRead],
)
async def create_company(
    company_data: CompanyCreate,
    company_service: CompanyServiceTxDep,
):
    return DataResponse(
        data=await company_service.create(company_data),
    )


@router.get(
    "",
    response_model=ListResponse[CompanyRead],
)
async def get_companies(
    company_service: CompanyServiceDep,
):
    return ListResponse(
        data=await company_service.get_all(),
    )


@router.get(
    "/{company_tin}",
    response_model=DataResponse[CompanyRead],
)
async def get_company_by_tin(
    company_tin: str,
    company_service: CompanyServiceDep,
):
    return DataResponse(
        data=await company_service.get_by_tin(company_tin),
    )
