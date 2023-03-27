from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

kb_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='1'),
            KeyboardButton(text='0')
        ],
        [
            KeyboardButton(text='!')
        ],
    ],
    resize_keyboard=True
)
