from pydantic import BaseModel

class ChairColorRead(BaseModel):
    id: int
    chair_id: int
    color_id: int
    upholstery: bool

    class Congif:
        from_attributes=True