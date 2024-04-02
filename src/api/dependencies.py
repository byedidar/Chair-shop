from src.reposotories.all_repositories import (
    UserRepository, ChairRepository, ColorRepository, ChairColorRepository,
    ChairTypeRepository, ImageRepository, ReviewRepository, WishlistRepository
    )

from src.services.user import UserService
from src.services.chair import ChairService
from src.services.chair_type import ChairTypeService
from src.services.chair_color import ChairColorService
from src.services.image import ImageService
from src.services.review import ReviewService
from src.services.color import ColorService
from src.services.wishlist import WishlistService


def user_service():
    return UserService(UserRepository())


def chair_service():
    return ChairService(ChairRepository())


def chair_type_service():
    return ChairTypeService(ChairTypeRepository())


def chair_color_service():
    return ChairColorService(ChairColorRepository())


def image_service():
    return ImageService(ImageRepository())


def review_service():
    return ReviewService(ReviewRepository())


def color_service():
    return ColorService(ColorRepository())


def wishlist_service():
    return WishlistService(WishlistRepository())