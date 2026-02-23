from pydantic import BaseModel, EmailStr
from typing import Optional

# -------- USER --------

class UserCreate(BaseModel):
    name: str
    email: EmailStr
    password: str

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

# -------- HOSPITAL --------

class HospitalBase(BaseModel):
    name: str
    address: Optional[str] = None
    latitude: float
    longitude: float

class HospitalResponse(HospitalBase):
    id: int

    class Config:
        from_attributes = True
