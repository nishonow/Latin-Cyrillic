from aiogram import types, executor
from aiogram.dispatcher import FSMContext
from aiogram.types import Message
from loader import dp, bot
from convert import latin_to_cyrillic, cyrillic_to_latin
import logging
import start
import admin

logging.basicConfig(format=u'%(filename)s [LINE:%(lineno)d] #%(levelname)-8s [%(asctime)s]  %(message)s',
                    level=logging.INFO,
                    )

@dp.message_handler(text='/lat_to_cyr')
async def latcyr(message: Message, state: FSMContext):
    await message.answer("Send me latin text."
                         "\n/cancel - cancel the current progress.")
    await state.set_state('latcyr')

@dp.message_handler(text='/cyr_to_lat')
async def cyrlat(message: Message, state: FSMContext):
    await message.answer("Send me cyrillic text."
                         "\n/cancel - cancel the current progress.")
    await state.set_state('cyrlat')

@dp.message_handler(text='/cancel', state='any')
async def cancel(message: Message, state: FSMContext):
    await state.finish()
    await message.answer("The progress has been cancelled.")


@dp.message_handler(content_types='text', state='latcyr')
async def convert(message: Message, state: FSMContext):
    text = message.text
    converted_text = latin_to_cyrillic(text)
    await message.reply(converted_text)
    await state.finish()

@dp.message_handler(content_types='text', state='cyrlat')
async def convert(message: Message, state: FSMContext):
    text = message.text
    converted_text = cyrillic_to_latin(text)
    await message.reply(converted_text)
    await state.finish()


















if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)