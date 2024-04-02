from typing import List
from src.models.wishlist import Wishlist
from src.services.base import BaseService

class WishlistService(BaseService):
    async def get_my_wishlists(self, user_id: int) -> List[Wishlist]:
        wishlists = await self.get_entities(user_id=user_id)
        return wishlists