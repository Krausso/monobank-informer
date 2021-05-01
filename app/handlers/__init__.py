from aiogram.types import Message
from app.config import dp, bot
from typing import NoReturn


@dp.message_handler(content_types='text')
async def _(msg: Message) -> NoReturn:
    await bot.send_message(msg.from_user.id, 'Hello, world')
