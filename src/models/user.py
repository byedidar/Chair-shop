from sqlalchemy import Column, Integer, String, TIMESTAMP, func
from settings.database.database_connection import Base
from src.schemas.user import UserRead

class User(Base):
    __tablename__ = "User"
    id = Column(Integer, primary_key=True)
    username = Column(String(45), nullable=True, unique=True)
    hashed_password = Column(String(length=1024), nullable=True)
    registered_at = Column(TIMESTAMP(timezone=True), server_default=func.now())
    role_id = Column(Integer, nullable=True, default=1)

    def to_read_model(self) -> UserRead:
        return UserRead(
            id=self.id,
            username=self.username,
            role_id=self.role_id,
        )