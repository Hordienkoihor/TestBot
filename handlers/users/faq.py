from aiogram import types
from loader import dp


@dp.message_handler(text='/faq')
async def command_faq(message: types.Message):
    await message.answer(f'Designed by me.\n'
                         )
