from sqlalchemy import Column, Integer, String, Float, Boolean
from .database import Base

class Hospital(Base):
    __tablename__ = "hospitais"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)
    address = Column(String)
    phone = Column(String)
    has_sus = Column(Boolean, default=False)
    has_private = Column(Boolean, default=False)
    emergency_24h = Column(Boolean, default=False)

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, nullable=False)
    hashed_password = Column(String, nullable=False)
