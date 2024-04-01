from src.reposotories.all_repositories import UserRepository
from src.services.user import UserService



def user_service():
    return UserService(UserRepository())
