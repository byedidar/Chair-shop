from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel

from src.schemas.chair import ChairRead
from src.schemas.user import UserRead

class WishlistRead(BaseModel):
    id: int
    user_id: int
    chair_id: int
    bought_date: datetime
    shell_color_id: int
    upholstery_color_id: int
    bought: Optional[bool] = False
    users: List[UserRead]
    chairs: List[ChairRead]
    
    class Config:
        from_attributes=True