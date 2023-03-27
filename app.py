async def on_start(dp):

    from utils.notify_admins import on_startup_notify
    await on_startup_notify(dp)

    from utils.setBotCommandes import setdefcom
    await setdefcom(dp)

    print('bot on')

if __name__ == '__main__':
    from aiogram import executor
    from handlers import dp

    executor.start_polling(dp, on_startup=on_start)

