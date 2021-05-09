from sqlalchemy import Column, Integer
from app.config import Base


class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer)
