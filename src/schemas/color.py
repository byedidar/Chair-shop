from pydantic import BaseModel

class ColorRead(BaseModel):
    id: int
    name: str
    hex: str

    class Config:
        from_attributes=True
