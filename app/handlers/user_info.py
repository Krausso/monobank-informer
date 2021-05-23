from aiogram.types import Message
from typing import NoReturn
from app.utils import get_info
from app.models import User
from app.config import dp


@dp.message_handler(commands='info', state='*')
async def _(msg: Message) -> NoReturn:
    user = User.find_instance(msg.from_user.id)
    if user.api_token:
        await msg.reply(get_info(user.api_token))
        return

    await msg.reply('You haven\'t set up your API Token yet')
