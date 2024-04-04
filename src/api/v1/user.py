from typing import List
from fastapi import APIRouter, Depends, HTTPException

from src.api.dependencies import wishlist_service
from src.helper_functions.auth_handler import get_current_user
from src.schemas.chair import ChairRead

user_router = APIRouter(prefix="/v1/user", tags=["user"])


@user_router.get(
    "/me/wishlist", 
    status_code=200,
    summary="Получение всех стульев из Wishlist"
)
async def get_my_wishlist(
    current_user: dict = Depends(get_current_user),
    chairs: List[ChairRead] = Depends(wishlist_service)
):
    user_id = current_user.get('id')
    wishlists = await wishlist_service.get_my_wishlists(user_id)
    
    if not wishlists:
        raise HTTPException(status_code=404, detail="No chairs found in your wishlist")
    
    chairs = [wishlist.chair.to_read_model() for wishlist in wishlists]
    return chairs