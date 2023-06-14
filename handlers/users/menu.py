

from aiogram import types
from loader import dp
from keyboard.default import kb_menu


@dp.message_handler(text="menu")
async def menu(message: types.Message):
    await message.answer("WIP", reply_markup=kb_menu)
