from typing import Optional, List

from pydantic import BaseModel, EmailStr
from enum import Enum


class Subject(BaseModel):
    name: str


class CV(BaseModel):
    subject: List[Subject]
    text: str
    rating: float


class RoleEnum(str, Enum):
    Client = 'Client'
    Administrator = 'Admin'
    Tutor = 'Tutor'


class User(BaseModel):
    first_name: str
    last_name: str
    location: Optional[str] = None
    username: str
    password: str
    email: EmailStr
    role: RoleEnum


    class Config:
        use_enum_values = True


class Login(BaseModel):
    username: str
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: Optional[str] = None
