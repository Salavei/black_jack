from aiogram.dispatcher.filters.builtin import CommandStart
from main import db, bot
from aiogram import types


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    if not db.check_user(message.from_user.id):
        db.add_user(message.from_user.id)
    await message.answer('Ты уже зареган')


async def error(bot, message):
    await message.delete()


@dp.message_handler(content_types=['text'])
async def command_start_text(message: types.Message):
    data = {
        'Начать игру': None,
        'Баланс': None,
        'История игр': None,
        'Еще': None,
        'Пасс': None,
    }
    await data.get(message.text, error)(bot, message)
