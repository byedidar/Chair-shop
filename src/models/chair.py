from settings.database.database_connection import Base
from sqlalchemy import Column, Integer, String, BigInteger, ForeignKey
from sqlalchemy.orm import relationship
from src.schemas.chair import ChairRead
from src.models.review import Review

class Chair(Base):
    __tablename__ = "Chair"
    id = Column(BigInteger, primary_key=True)
    name = Column(String, nullable=False)
    price = Column(Integer, nullable=False)
    price_on_sale = Column(Integer, nullable=True,default=None)
    type = Column(BigInteger, ForeignKey("ChairType.id",ondelete="CASCADE"))
    images = relationship("Image", lazy="selectin")
    reviews = relationship("Review", lazy="selectin")
    

    def avg_star(self):
        total_star_rating = sum(review.star for review in self.reviews)
        num_reviews = len(self.reviews)
        if num_reviews == 0:
            return 0
        else:
            return round(total_star_rating / num_reviews, 1)

    def to_read_model(self) -> ChairRead:
        images_read=[image.to_read_model() for image in self.images]
        return ChairRead(
            id=self.id,
            name=self.name,
            price=self.price,
            price_on_sale=self.price_on_sale,
            type=self.type,
            images=images_read,
            avg_rating=self.avg_star()
        )