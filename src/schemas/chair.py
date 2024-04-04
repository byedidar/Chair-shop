from typing import List, Optional
from pydantic import BaseModel
from src.schemas.image import ImageRead

class ChairRead(BaseModel):
    id: int
    name: str
    price: Optional[int]
    price_on_sale: Optional[int]
    type: Optional[int]
    images: List[ImageRead]
    avg_rating: Optional[int] = None
    
    class Config:
        from_attributes = True
  