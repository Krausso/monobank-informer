from sqlalchemy import Column, Integer, String
from app.config import Base, session
from typing import NoReturn


class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True)
    token = Column(String(128), unique=True, default="")
    user_id = Column(Integer, unique=True)

    @classmethod
    def exists(cls, user: int) -> NoReturn:
        users = list(map(lambda current_user: current_user.user_id, session.query(cls).all()))
        if user not in users:
            return False

        return True
