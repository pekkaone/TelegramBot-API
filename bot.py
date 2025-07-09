import asyncio
import logging
from datetime import datetime
from aiogram import Bot, Dispatcher, types, F
from aiogram.types import Message
from aiogram.filters.command import Command
from aiogram.enums.dice_emoji import DiceEmoji
from configreader import config

logging.basicConfig(level=logging.INFO)
bot = Bot(token=config.bot_token.get_secret_value())
dp = Dispatcher()

@dp.message(Command('start'))
async def start_command(message: types.Message):
    await message.answer("This is a testing bot, gladly working\nMade by @Pekka_One")

@dp.message(F.text.lower() == "bitch")
async def bad_word(message: Message):
    user_id = message.from_user.id
    def_username = 1438774321
    await bot.send_message(chat_id=def_username, text=f"You shoud beat {user_id} ass))")
    await message.answer("You are gonna regret")

@dp.message(Command('myinfo'))
async def user_id(message: Message):
    my_id = message.from_user.id
    my_else = message.from_user.username
    my_else2 = message.from_user.is_premium
    my_else3 = message.from_user.full_name
    await message.reply(f"your id is {my_id}\nUsername is @{my_else}\nis Premium: {my_else2}\nFull name: {my_else3}")


@dp.message()
async def not_recognised(message: Message):
    await message.answer("Not recognised")


async def run_bot():
    await dp.start_polling(bot)