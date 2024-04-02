from settings.database.database_connection import Base
from sqlalchemy import Column, Integer, String

from src.schemas.color import ColorRead


class Color(Base):
    __tablename__ = "Color"
    id = Column(Integer, primary_key=True)
    name = Column(String(45), nullable=False)
    hex = Column(String(45), nullable=False)

    def to_read_model(self)->ColorRead:
        return ColorRead(
            id=self.id,
            name=self.name,
            hex=self.hex
        )
