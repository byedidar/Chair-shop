from typing import Optional
from pydantic import BaseModel, Field

class ReviewRead(BaseModel):
    id: Optional[int] = Field(None, gt=0, lt=6)
    star: int
    text: str
    user_id: int
    chair_id: int

    class Config:
        from_attributes = True


class ReviewCreate(BaseModel):
    star: Optional[int] = Field(None, gt=0, lt=6)
    text: str
    user_id: int
    chair_id: int

    class Config:
        from_attributes=True