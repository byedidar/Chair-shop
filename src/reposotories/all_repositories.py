
from src.reposotories.repository import SQLAlchemyRepository
from src.models.chair import Chair
from src.models.chair_color import ChairColor
from src.models.chair_type import ChairType
from src.models.color import Color
from src.models.image import Image
from src.models.review import Review
from src.models.user import User
from src.models.wishlist import Wishlist


class UserRepository(SQLAlchemyRepository):
    model = User

class ChairRepository(SQLAlchemyRepository):
    model = Chair
    
class ColorRepository(SQLAlchemyRepository):
    model = Color  

class ChairColorRepository(SQLAlchemyRepository):
    model = ChairColor 


class ChairTypeRepository(SQLAlchemyRepository):
    model = ChairType


class ImageRepository(SQLAlchemyRepository):
    model = Image


class ReviewRepository(SQLAlchemyRepository):
    model = Review


class WishlistRepository(SQLAlchemyRepository):
    model = Wishlist