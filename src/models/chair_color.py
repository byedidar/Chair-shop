from settings.database.database_connection import Base
from sqlalchemy import Boolean, Column, Integer, ForeignKey

from src.schemas.chair_color import ChairColorRead


class ChairColor(Base):
    __tablename__ = "ChairColor"
    id = Column(Integer, primary_key=True)
    chair_id = Column(Integer, ForeignKey("Chair.id"),nullable=False)
    color_id = Column(Integer, ForeignKey("Color.id"),nullable=False)
    upholstery = Column(Boolean, nullable=False)

    def to_read_model(self)->ChairColorRead:
        return ChairColorRead(
            id=self.id,
            chair_id=self.chair_id,
            color_id=self.color_id,
            upholstery=self.upholstery
        )