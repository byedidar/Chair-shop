from pydantic import BaseModel

class ReviewRead(BaseModel):
    id: int
    star: int
    text: str
    user_id: int
    chair_id: int

    class Config:
        from_attributes = True