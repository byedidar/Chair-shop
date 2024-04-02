from pydantic import BaseModel
 
class ImageRead(BaseModel):
    id: int
    path: str
    chair_id: int
    
    class Config:
        from_attributes = True


