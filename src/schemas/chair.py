from typing import List, Optional
from pydantic import BaseModel
from src.schemas.image import ImageRead

class ChairRead(BaseModel):
    id: int
    name: str
    price: int
    price_on_sale: Optional[int]
    type: int
    images: List[ImageRead]
    avg_rating: int
    
    class Config:
        from_attributes = True
  