from aiogram import types
from main import db
from black_jack_logic import Game


async def start_game(message: types.Message):
    if not db.check_user(message.from_user.id):
        db.add_user(message.from_user.id)
    elif db.check_balance(message.from_user.id) <= 0:
        await message.answer(text='У вас закончились деньги')
    await message.answer(text='Игра начата')
    game = Game(player_name=message.from_user.id)
    await game.start(message)


async def user_balance(message: types.Message):
    if not db.check_user(message.from_user.id):
        db.add_user(message.from_user.id)
    await message.answer(text='Ваш баланс: {}$'.format(db.check_balance(message.from_user.id)))


async def story_game(message: types.Message):
    if not db.check_user(message.from_user.id):
        db.add_user(message.from_user.id)
    if not db.check_story(message.from_user.id):
        await message.answer(text='Вы еще не играли')
    for story in db.check_story(message.from_user.id):
        await message.answer(text='История игр: {}'.format(story))
