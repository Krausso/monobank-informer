from aiogram.types import Message
from app.handlers import process_token, user_info
from app.config import dp, bot, session
from app.models import User
from typing import NoReturn


@dp.message_handler(content_types='text', state='*')
async def _(msg: Message) -> NoReturn:
    if not User.exists(msg.from_user.id):
        session.add(User(user_id=msg.from_user.id))
        session.commit()
        return

    await bot.send_message(msg.from_user.id, 'You are already added')
