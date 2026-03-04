from typing import Annotated

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.session_dep import SessionDep, TransactionSessionDep
from app.models.camera import Camera
from app.repositories.camera import CameraRepository
from app.services.camera import CameraService


async def get_camera_service(
    session: Annotated[AsyncSession, SessionDep],
) -> CameraService:
    repo = CameraRepository(session, Camera)
    return CameraService(session, repo)


async def get_camera_service_tx(
    session: Annotated[AsyncSession, TransactionSessionDep],
) -> CameraService:
    repo = CameraRepository(session, Camera)
    return CameraService(session, repo)


CameraServiceDep = Annotated[CameraService, Depends(get_camera_service)]
CameraServiceTxDep = Annotated[CameraService, Depends(get_camera_service_tx)]
