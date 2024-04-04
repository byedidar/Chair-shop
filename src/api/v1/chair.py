
from fastapi import APIRouter, Depends, HTTPException

from src.services.chair import ChairService
from src.api.dependencies import chair_service


chair_router = APIRouter(prefix="/v1/chair", tags=["chair"])


@chair_router.get(
        "/{id}",
        status_code=200, 
        summary="Получение информации о стуле"
)
async def get_chair(
        id: int,
        chairs_service: ChairService = Depends(chair_service)
):
    chair = await chairs_service.get_entity(id=id)
    if chair is None:
        raise HTTPException(status_code=404, detail="Стул не найден")
    return chair


@chair_router.get(
        "/",
        status_code=200,
        summary="Получение всех стульев"
)
async def get_chairs(
        chairs_service: ChairService = Depends(chair_service)
):
    chair = await chairs_service.get_entities()
    if chair is None:
        raise HTTPException(status_code=404, detail="Стул не найден")
    return chair



@chair_router.get(
        "/on_sale/",
        status_code=200,
        summary="Получение всех стульев"
)
async def get_chairs_with_sale(
        chairs_service: ChairService = Depends(chair_service)
):
    chairs = await chairs_service.get_entities()
    if chairs is None:
        raise HTTPException(status_code=404, detail="Стул не найден")
    chairs = [chair for chair in chairs if chair.price_on_sale is not None]
    return chairs





