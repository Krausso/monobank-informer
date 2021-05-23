from typing import NoReturn

from sqlalchemy import Column, Integer, String

from app.config import Base, session


class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True)
    api_token = Column(String(128), unique=True, default="")
    user_id = Column(Integer, unique=True)

    @classmethod
    def create_instance(cls, user_id: int) -> NoReturn:
        session.add(cls(user_id))
        session.commit()

    @classmethod
    def instance_exists(cls, user_id: int) -> bool:
        user_ids = list(map(lambda current_user: current_user.user_id, session.query(cls).all()))
        if user_id not in user_ids:
            return False
        return True

    @classmethod
    def find_instance(cls, user_id: int):
        found_user = session.query(cls).filter(cls.user_id == user_id).first()
        return found_user

    @classmethod
    def remove_token(cls, user_id: int) -> NoReturn:
        user = cls.find_instance(user_id)
        user.api_token = ''
        session.commit()
