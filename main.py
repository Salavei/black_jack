from aiogram import Bot, Dispatcher, executor
import logging
from utils.db_api import SQLBot

TOKEN = ''
logging.basicConfig(level=logging.INFO)
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)
db = SQLBot('path')

if __name__ == '__main__':
    from handlers.app import dp

    executor.start_polling(dp, skip_updates=True)
