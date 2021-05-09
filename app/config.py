from aiogram.contrib.fsm_storage.memory import MemoryStorage
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.engine import Engine
from sqlalchemy import create_engine
from aiogram import Bot, Dispatcher
from dynaconf import Dynaconf

settings: Dynaconf = Dynaconf(
    env='development',
    settings_files=['app/settings.toml', 'app/.secrets.toml'],
    environments=True
)

bot: Bot = Bot(settings.TOKEN)
storage: MemoryStorage = MemoryStorage()
dp: Dispatcher = Dispatcher(bot, storage=storage)

engine: Engine = create_engine('sqlite:///app/app.db', echo=True)
Session = sessionmaker(bind=engine)
session: Session = Session()
Base = declarative_base()
