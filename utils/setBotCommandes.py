from aiogram import types


async def setdefcom(dp):
    await dp.bot.set_my_commands([
        types.BotCommand('start', 'Start bot'),
        types.BotCommand('faq', 'FAQ')
    ])
