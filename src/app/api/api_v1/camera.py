from fastapi import APIRouter

from app.api.dependencies.camera import CameraServiceDep, CameraServiceTxDep
from app.schemas.camera import CameraCreate, CameraRead
from app.schemas.response import DataResponse, ListResponse
from core.config import settings

router = APIRouter(
    prefix=settings.api.v1.cameras,
    tags=["Cameras"],
)


@router.get(
    "",
    response_model=ListResponse[CameraRead],
)
async def get_cameras(
    camera_service: CameraServiceDep,
):
    return ListResponse(
        data=await camera_service.get_all(),
    )


@router.post(
    "",
    response_model=DataResponse[CameraRead],
)
async def create_camera(
    camera_data: CameraCreate,
    camera_service: CameraServiceTxDep,
):
    return DataResponse(
        data=await camera_service.create(camera_data),
    )
