from sqlalchemy import BigInteger, Column, Text, ForeignKey
from settings.database.database_connection import Base
from src.schemas.image import ImageRead

class Image(Base):
    __tablename__ = "Image"
    id = Column(BigInteger, primary_key=True)
    path = Column(Text)
    chair_id = Column(BigInteger, ForeignKey("Chair.id", ondelete="CASCADE"))
    
    def to_read_model(self)-> ImageRead:
        return ImageRead(
            id=self.id,
            path=self.path,
            chair_id=self.chair_id
        )