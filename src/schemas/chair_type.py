from pydantic import BaseModel

class ChairTypeRead(BaseModel):
    id: int
    name: str
    
    class Config:
        from_attributes = True
        