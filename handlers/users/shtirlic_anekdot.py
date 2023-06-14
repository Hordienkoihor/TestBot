from aiogram import types
from loader import dp


@dp.message_handler(text='Штірліц')
async def shtyrlic_an(message: types.Message):
    await message.answer(f'"Штирлиц долго смотрел в одну точку. Потом в другую. Двоеточие!'
                         f' - наконец-то смекнул Штирлиц."')
