from typing import Optional
from pydantic import BaseModel


class UserRead(BaseModel):
    id: int
    username: str
    role_id: Optional[int] = None

    class Config:
        from_attributes = True


class UserRegistration(BaseModel):
    username: str
    password: str
    confirm_password: str

    class Config:
        from_attributes = True


class UserCreate(BaseModel):
    username: str
    password: str
    class Config:
        from_attributes = True


class LoginInput(BaseModel):
    username: str
    password: str

    class Config:
        from_attributes = True


class LoginOutput(BaseModel):
    access_token: str
    token_type: str
    refresh_token: str

    class Config:
        from_attributes = True


class RefreshInput(BaseModel):
    refresh_token: str

    class Config:
        from_attributes = True


class RefreshOutput(BaseModel):
    access_token: str
    token_type: str


    class Config:
        from_attributes = True