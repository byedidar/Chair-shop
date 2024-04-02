from src.api.v1.auth import auth_router
from src.api.v1.review import review_router
from src.api.v1.wishlist import wishlist_router
from src.api.v1.chair import chair_router
from src.api.v1.user import user_router
all_routers = [
    auth_router,
    review_router,
    wishlist_router,
    chair_router,
    user_router
]
