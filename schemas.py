from pydantic import BaseModel


class HospitalBase(BaseModel):
    name: str
    latitude: float
    longitude: float
    address: str | None = None
    phone: str | None = None
    has_sus: bool = False
    has_private: bool = False
    emergency_24h: bool = False

class HospitalResponse(HospitalBase):
        id: int
        distance_km: float | None = None

        class Config:
              from_attributes = True
    
class UserCreate(BaseModel):
    email: str
    password: str


class UserLogin(BaseModel):
    email: str
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str
