from settings.database.database_connection import Base
from sqlalchemy import Column, Integer, String

from src.schemas.chair_type import ChairTypeRead

class ChairType(Base):
    __tablename__ = "ChairType"

    id = Column(Integer, primary_key=True)
    name = Column(String(length=45))
    
    def to_read_model(self) -> ChairTypeRead:
        return ChairTypeRead(
            id = self.id,
            name = self.name
        )