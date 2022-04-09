from aiogram.types import KeyboardButton
from aiogram import types

btn_game_start = KeyboardButton('Начать игру')
btn_balance = KeyboardButton('Баланс')
btn_story_game = KeyboardButton('История игр')
keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
keyboard.add(btn_game_start, btn_balance, btn_story_game)

btn_yes = KeyboardButton('y')
btn_pass = KeyboardButton('n')
keyboard_game = types.ReplyKeyboardMarkup(resize_keyboard=True)
keyboard_game.add(btn_yes, btn_pass)
