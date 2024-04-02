from fastapi import APIRouter, Depends, HTTPException

from src.api.dependencies import wishlist_service
from src.schemas.wishlist import WishlistCreate, WishlistRead
from src.services.wishlist import WishlistService

wishlist_router = APIRouter(prefix="/v1/wishlist", tags=["wishlist"])


@wishlist_router.post(
        "/", 
        response_model=WishlistRead, 
        status_code=201,
        summary="Добавление стула в Wishlist"
)
async def create_wishlist(wishlist_create: WishlistCreate, wishlist_service: WishlistService = Depends(wishlist_service)):
    wishlist_id = await wishlist_service.create_entity(wishlist_create)
    return {"id": wishlist_id}


@wishlist_router.get(
        "/{wishlist_id}", 
        response_model=WishlistRead,
        summary="Получение инфо о стуле в Wishlist-e"
)
async def get_wishlist(wishlist_id: int, wishlist_service: WishlistService = Depends(wishlist_service)):
    wishlist = await wishlist_service.get_entity(id=wishlist_id)
    if not wishlist:
        raise HTTPException(status_code=404, detail="Wishlist not found")
    return wishlist


@wishlist_router.delete(
        "/{wishlist_id}", 
        status_code=204,
        summary="Удаление стула из Wishlist-a"
)
async def delete_wishlist(wishlist_id: int, wishlist_service: WishlistService = Depends(wishlist_service)):
    deleted = await wishlist_service.delete_entity(id=wishlist_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Wishlist not found")
    return {"message": "Wishlist deleted successfully"}