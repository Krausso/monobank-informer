from aiogram.contrib.fsm_storage.memory import MemoryStorage
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