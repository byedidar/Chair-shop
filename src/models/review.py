from settings.database.database_connection import Base
from sqlalchemy import Column, Integer, BigInteger, ForeignKey, Text, CheckConstraint
from src.schemas.review import ReviewRead
from sqlalchemy.orm import relationship
class Review(Base):
    __tablename__ = "Review"
    id = Column(BigInteger, primary_key=True)
    star = Column(Integer, CheckConstraint('star >= 1 AND star <= 5', name='check_star_range'))
    text = Column(Text)
    user_id = Column(Integer, ForeignKey("User.id", ondelete="CASCADE"))
    chair_id = Column(Integer, ForeignKey("Chair.id", ondelete="CASCADE"))

    chair = relationship("Chair", back_populates="reviews", lazy="selectin")
    user = relationship("User", back_populates="reviews", lazy="selectin")


    def to_read_model(self)->ReviewRead:
        return ReviewRead(
            id=self.id,
            star=self.star,
            text=self.text,
            user_id=self.user_id,
            chair_id=self.chair_id
        )