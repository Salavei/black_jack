from aiogram.dispatcher.filters.builtin import CommandStart
from main import db, dp
from aiogram import types
from utils.user_funk import start_game, user_balance, story_game
from keyboards.markup import keyboard


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    if not db.check_user(message.from_user.id):
        db.add_user(message.from_user.id)
        await message.answer('Добро пожаловать')
    else:
        await message.answer('Ты уже зареган', reply_markup=keyboard)


async def error(message):
    await message.delete()


@dp.message_handler(content_types=['text'])
async def command_start_text(message: types.Message):
    data = {
        'Начать игру': start_game,
        'Баланс': user_balance,
        'История игр': story_game,
    }
    await data.get(message.text)(message)
