
from fastapi import APIRouter, Depends, HTTPException

from src.services.chair import ChairService



chair_router = APIRouter(prefix="/v1/chair", tags=["chair"])

@chair_router.get(
        "/{chair_id}",
        status_code=200, 
        summary="Получение информации о стуле"
)
async def get_chair(chair_id: int, chair_service: ChairService = Depends()):
    chair = await chair_service.get_entity(id=chair_id)
    if chair is None:
        raise HTTPException(status_code=404, detail="Стул не найден")
    return chair