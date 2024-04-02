from fastapi import APIRouter, Depends

wishlist_router = APIRouter(prefix="/v1/wishlist", tags=["wishlist"])


@wishlist_router.post()
async def create_wishlist():
    pass

@wishlist_router.delete()
async def delete_wishlist():
    pass