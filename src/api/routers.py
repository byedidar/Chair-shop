from src.api.v1.auth import auth_router
from src.api.v1.review import review_router
from src.api.v1.wishlist import wishlist_router
all_routers = [
    auth_router,
    review_router,
    wishlist_router
]
