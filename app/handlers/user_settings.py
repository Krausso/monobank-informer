from aiogram.types import Message
from app.config import dp, bot
from app.models import User
from typing import NoReturn


@dp.message_handler(commands='settings', state='*')
async def _(msg: Message) -> NoReturn:
    found_user = User.find_instance(msg.from_user.id).api_token
    if found_user == '':
        await msg.reply('You haven\'t set your API Token yet.')
        return

    text = f'Current API Token: {found_user}'
    await msg.reply(text)