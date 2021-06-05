from typing import NoReturn

from aiogram.types import Message

from app.config import dp


@dp.message_handler(commands="about", state="*")
async def about(msg: Message) -> NoReturn:
    await msg.reply(f'''
Hey, {msg.from_user.username or msg.from_user.first_name}:)

Monobank Informer bot is created as an analogue to a Monobank application.
Currently, there's only ability to check your current balance, although bot is going to be updated as soon as I'll have some free time.
Commands:
/start - Get instructions
/about - Some useful information
/info - Request for your mono information
/settings - Check your current settings
/set_token - Set up your API Token
/remove_token - Remove your API Token

This project is open-source, so you can request your ideas or features as an issue in a repo below.
Source code: github.com/Krausso/monobank-informer
Developer: @krau5
    ''')
