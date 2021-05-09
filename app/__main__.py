from aiogram import executor
from app.config import settings, dp, engine, Base
import app.handlers
import os

if __name__ == "__main__":
    if not os.path.exists('app/app.db'):
        Base.metadata.create_all(bind=engine)

    executor.start_polling(dp, skip_updates=True)
