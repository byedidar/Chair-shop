from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel

from src.schemas.chair import ChairRead
from src.schemas.user import UserRead

class WishlistRead(BaseModel):
    id: int
    bought_date: datetime
    shell_color_id: int
    upholstery_color_id: int
    bought: Optional[bool] = False
    user: UserRead
    chair: ChairRead
    
    class Config:
        from_attributes=True


class WishlistCreate(BaseModel):
    user_id: int
    chair_id: int
    shell_color_id: int
    upholstery_color_id: int

    class Config:
        from_attributes=True

