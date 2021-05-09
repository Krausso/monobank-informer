from aiogram.types import Message
from app.config import dp, bot
from app.models import User
from typing import NoReturn


@dp.message_handler(commands='info', state='*')
async def _(msg: Message) -> NoReturn:
    found_user = User.find_instance(msg.from_user.id)
    text = f'Current API Token: {found_user.api_token}'

    await msg.reply(text)