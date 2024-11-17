from aiogram.dispatcher import FSMContext
from aiogram.types import Message
from loader import dp, bot
from config import ADMINS
from db import count_users

@dp.message_handler(user_id=ADMINS, text='/all')
async def all_users(message: Message):
    total_users = count_users()

    await message.answer(f"Total users using this bot: {total_users}")