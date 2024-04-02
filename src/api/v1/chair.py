
from fastapi import APIRouter



chair_router = APIRouter(prefix="/v1/chair", tags=["chair"])

@chair_router.get(
    "/",
    status_code=200,
    summary="Найти стулья"
)
async def get_chair():
    pass