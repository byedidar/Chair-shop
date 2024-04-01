from src.models.user import User
from src.reposotories.repository import SQLAlchemyRepository


class UserRepository(SQLAlchemyRepository):
    model = User
