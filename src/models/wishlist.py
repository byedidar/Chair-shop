from settings.database.database_connection import Base
from sqlalchemy import Boolean, Column, Integer, BigInteger, ForeignKey, TIMESTAMP, func
from sqlalchemy.orm import relationship

from src.schemas.wishlist import WishlistRead
class Wishlist(Base):
    __tablename__ = "Wishlist"
    id = Column(BigInteger, primary_key=True)
    user_id = Column(BigInteger, ForeignKey("User.id"))
    chair_id = Column(BigInteger, ForeignKey("Chair.id"))
    bought_date =Column(TIMESTAMP(timezone=True),server_default=func.now())
    upholstery_color_id = Column(Integer, ForeignKey("Color.id"))
    shell_color_id = Column(Integer, ForeignKey("Color.id"))
    bought = Column(Boolean, nullable=True, default=False)
    
    users = relationship('User', back_populates='wishlist', lazy="selectin")
    chairs = relationship('Chair', back_populates='wishlists', lazy="selectin")

    def to_read_model(self)->WishlistRead:
        users_read = [user.to_read_model() for user in self.users]
        chairs_read = [chair.to_read_model() for chair in self.chairs]
        
        return WishlistRead(
            id=self.id,
            user_id=self.user_id,
            chair_id=self.chair_id,
            bought_date=self.bought_date,
            upholstery_color_id=self.upholstery_color_id,
            shell_color_id=self.shell_color_id,
            bought=self.bought,
            users=users_read,
            chairs=chairs_read
        )