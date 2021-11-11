import random
import string
from sqlalchemy import Column, Integer, String, ForeignKey, BLOB, Enum, FLOAT
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship


BaseModel = declarative_base()

secret_key = ''.join(random.choice(string.ascii_uppercase + string.digits) for x in range(32))


class User(BaseModel):
    __tablename__ = 'User'

    id = Column(Integer, primary_key=True)
    first_name = Column(String(55), unique=False, nullable=False)
    last_name = Column(String(55), unique=False, nullable=False)
    location = Column(String(55), unique=False, nullable=True)
    username = Column(String(55), unique=True, nullable=False)
    password_hash = Column(String(300), unique=False, nullable=False)
    email = Column(String(60), unique=True, nullable=False)
    phone = Column(String(15), unique=True, nullable=True)
    photo = Column(BLOB, unique=False, nullable=True)  # TODO: create default blob object
    role = Column(Enum('Tutor', 'Admin', 'Client'), unique=False, nullable=False, default='Client')

    def __repr__(self):
        return f"User('{self.username}','{self.first_name}','{self.last_name}','{self.email}','{self.phone}')"

    @property
    def serialize(self):
        return {
            "id": self.id,
            "username": self.username,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "location": self.location,
            "email": self.email,
            "phone": self.phone,
            "photo": self.photo
        }


class CV(BaseModel):
    __tablename__ = 'CV'

    id = Column(Integer, primary_key=True)
    text = Column(String(2000), unique=False, nullable=False)
    rating = Column(FLOAT, unique=False, nullable=True)

    user_id = Column(Integer, ForeignKey("User.id"), unique=True, nullable=False)

    user = relationship(User)

    def __repr__(self):
        return f"CV('{self.text}','{self.rating}')"

    @property
    def serialize(self):
        return {
            "id": self.id,
            "text": self.text,
            "rating": self.rating,
            "user_id": self.user_id
        }


class Subject(BaseModel):
    __tablename__ = 'Subject'

    id = Column(Integer, primary_key=True)
    name = Column(
        Enum('English', 'Germany', 'History', 'Astronomy', 'Math', 'Chemistry', 'Physics', 'Biology', 'Literature'),
        unique=False, nullable=True)

    cv_id = Column(Integer, ForeignKey("CV.id"), unique=True, nullable=False)
    cv_user_id = Column(Integer, ForeignKey("User.id"), unique=False, nullable=False)

    cv = relationship(CV)
    cv_user = relationship(User)

    def __repr__(self):
        return f"Subject('{self.name}')"

    @property
    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "cv_id": self.cv_id,
            "cv_user_id": self.cv_user_id
        }


class Review(BaseModel):
    __tablename__ = 'Review'

    id = Column(Integer, primary_key=True)
    text = Column(String(1000), unique=False, nullable=False)
    mark = Column(Integer, unique=False, nullable=False, default=0)
    user_id = Column(Integer, ForeignKey("User.id"), unique=False, nullable=False)
    user = relationship(User)

    def __repr__(self):
        return f"Review('{self.text}','{self.mark}')"

    @property
    def serialize(self):
        return {
            "id": self.id,
            "text": self.text,
            "mark": self.mark,
            "user_id": self.user_id
        }
