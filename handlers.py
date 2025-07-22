import asyncio
import logging
from datetime import datetime
from aiogram import Bot, Dispatcher, types, F, Router
from aiogram.types import Message, CallbackQuery
from aiogram.filters.command import Command
from aiogram.enums.dice_emoji import DiceEmoji
from configreader import config
import keyboards as kb
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext



router = Router()

class Reg(StatesGroup):
    name = State()
    yo = State()

@router.message(Command('reg'))
async def reg_one(message: Message, state: FSMContext):
    await state.set_state(Reg.name)
    await message.answer('Enter name for ur profile:')

@router.message(Reg.name)
async def reg_two(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await state.set_state(Reg.yo)
    await message.answer("Enter your years old")

@router.message(Reg.yo)
async def two_three(message: Message, state: FSMContext):
    await state.update_data(yo=message.text)
    data = await state.get_data()
    await message.answer("your profile is ready:")
    await message.answer(f'Name: {data['name']}\nYo: {data["yo"]}')
    await state.clear()


@router.message(Command('start'))
async def start_command(message: types.Message):
    await message.answer("This is a testing bot, gladly working\nMade by @Pekka_One", 
                         reply_markup=kb.main)

@router.message(F.text.lower() == "bitch")
async def bad_word(message: Message):
    from bot import bot
    user_id = message.from_user.username
    def_username = 1438774321
    await bot.send_message(chat_id=def_username, text=f"You shoud beat @{user_id} ass))")
    await message.answer("You are gonna regret")

@router.message(F.text, Command('AboutBot'))
async def about_us(message: types.Message):
    await message.answer("BOT i created by pekkaone on github\nthat is a preview project created by 14 yo. kiddo ;)",
                         reply_markup=kb.main)
    
@router.message(F.text, Command('github'))
async def my_github(message: Message):
    await message.answer("This is my github)", reply_markup=kb.settings)

@router.message(Command('myinfo'))
async def user_id(message: Message):
    my_id = message.from_user.id
    my_else = message.from_user.username
    my_else2 = message.from_user.is_premium
    my_else3 = message.from_user.full_name
    await message.reply(f"your id is {my_id}\nUsername is @{my_else}\nis Premium: {my_else2}\nFull name: {my_else3}",
                        reply_markup=kb.main)

@router.message(F.text, Command('bitches'))
async def my_bitches(message: Message):
    await message.answer('Here are my bitches:', reply_markup=await kb.inline_bitches())

@router.callback_query(F.data.startswith("bitch"))
async def handle_my_bitches(callback: CallbackQuery):
    index = int(callback.data.replace('bitch', ''))
    await callback.message.answer(f"{kb.bitches[index]} is rated at number {index + 1} by me")
    await callback.answer()

@router.message()
async def not_recognised(message: Message):
    await message.answer("Not recognised")

