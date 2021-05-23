from typing import NoReturn

from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import Message

from app.config import dp, bot, session
from app.models import User


class ProcessToken(StatesGroup):
    api_token = State()


@dp.message_handler(commands='remove_token', state='*')
async def remove_token(msg: Message) -> NoReturn:
    User.remove_token(msg.from_user.id)
    await msg.reply('Token has been removed successfully')


@dp.message_handler(commands='set_token', state='*')
async def set_token(msg: Message) -> NoReturn:
    await msg.reply('Enter your Mono API token')
    await ProcessToken.api_token.set()


@dp.message_handler(content_types='text', state=ProcessToken.api_token)
async def get_token(msg: Message, state: FSMContext):
    user = User.find_instance(msg.from_user.id)
    old_api_token = user.api_token[:]

    await state.update_data(api_token=msg.text)
    user_data = await state.get_data()

    if user_data['api_token'] == old_api_token:
        await msg.reply('Your token is same as the entered one')
        return

    user.api_token = user_data['api_token']
    session.commit()

    await msg.reply(f'API Token is set successfully.\nNew API Token: {user_data["api_token"]}')
    await state.finish()
