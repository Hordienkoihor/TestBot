import logging
import time

from aiogram import types


from loader import dp


@dp.message_handler(text='/start')
async def command_start(message: types.Message):
    user_id = message.from_user.id
    user_full_name = message.from_user.full_name
    logging.info(f'{user_id=} {user_full_name=}')
    await message.answer(f'Hello {message.from_user.full_name}! \n'
                         f'Your id: {message.from_user.id}')
