import asyncio
import logging
from datetime import datetime
from aiogram import Bot, Dispatcher, types, F
from aiogram.types import Message
from aiogram.filters.command import Command
from aiogram.enums.dice_emoji import DiceEmoji
from configreader import config
from handlers import router

logging.basicConfig(level=logging.INFO)
bot = Bot(token=config.bot_token.get_secret_value())
dp = Dispatcher()


async def run_bot():
    dp.include_router(router)
    await dp.start_polling(bot)