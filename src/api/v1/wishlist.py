from fastapi import APIRouter, Depends, HTTPException

from src.api.dependencies import wishlist_service
from src.schemas.wishlist import WishlistCreate, WishlistRead
from src.services.wishlist import WishlistService

wishlist_router = APIRouter(prefix="/v1/wishlist", tags=["wishlist"])


@wishlist_router.post(
        "/",
        status_code=201,
        summary="Добавление стула в Wishlist"
)
async def create_wishlist(wishlist_create: WishlistCreate, wishlist_service: WishlistService = Depends(wishlist_service)):
    chair_exists = await wishlist_service.get_entity(chair_id=wishlist_create.chair_id)
    if not chair_exists:
        raise HTTPException(status_code=404, detail="Кресло не найдено")
    
    wishlist_id = await wishlist_service.create_entity(wishlist_create)
    return {"id": wishlist_id}


@wishlist_router.get(
        "/{id}",
        status_code=201,
        summary="Получение инфо о стуле в Wishlist-e"
)
async def get_wishlist(id: int, wishlist_service: WishlistService = Depends(wishlist_service)):
    wishlist = await wishlist_service.get_entity(id=id)
    if not wishlist:
        raise HTTPException(status_code=404, detail="Wishlist not found")
    return wishlist


@wishlist_router.delete(
        "/{id}", 
        status_code=200,
        summary="Удаление стула из Wishlist-a"
)
async def delete_wishlist(id: int, wishlist_service: WishlistService = Depends(wishlist_service))->bool:
    wishlist = await wishlist_service.get_entity(id=id)
    if not wishlist:
        raise HTTPException(status_code=404, detail="Wishlist not found")
    result = await wishlist_service.delete_entity(id=id)
    return {"success": result}


