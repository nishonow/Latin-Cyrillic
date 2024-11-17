from db import add_user, user_exists
from aiogram.dispatcher import FSMContext
from aiogram.types import Message
from config import ADMINS
from loader import dp, bot

@dp.message_handler(text='/start')
async def new_user(message: Message):
    telegram_id = message.from_user.id
    name = message.from_user.first_name
    username = message.from_user.username

    if not user_exists(telegram_id):
        add_user(telegram_id, name, username)

    await message.answer("Welcome to the Latin-Cyrillic Transliteration bot.\n\n"
                         "\n/lat_to_cyr - for latin to cyrilllic\n"
                         "/cyr_to_lat - for cyrillic to latin")