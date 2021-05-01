from aiogram import executor
from app.config import settings, dp
import app.handlers

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
