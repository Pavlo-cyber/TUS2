from typing import Optional, List

from pydantic import BaseModel, EmailStr
from enum import Enum


class Subject(str, Enum):
    Math = 'Math'
    English = 'English'
    Physics = 'Physics'
    German = 'German'
    Biology = 'Biology'
    History = 'History'
    Astronomy = 'Astronomy'
    Chemistry = 'Chemistry'
    Literature = 'Literature'


class CV(BaseModel):
    subject: Subject
    text: str
    rating: Optional[float] = 5.0


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


class CVResponse(BaseModel):
    id: int
    subject: str
    first_name: str
    last_name: str
    text: str
    rating: float
    photo: Optional[str] = None
    email: str
    phone: Optional[str] = None


class Review(BaseModel):
    text: str
