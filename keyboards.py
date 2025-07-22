from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder

main = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="/myinfo"), KeyboardButton(text="/github")],
    [KeyboardButton(text="/AboutBot"), KeyboardButton(text="/bitches")]
],  
                            resize_keyboard=True,
                            input_field_placeholder="Choose the command")

settings = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Github', url='https://github.com/pekkaone')]
    ])

bitches = ['Monika', 'Snizana', 'Twiy tato']

async def inline_bitches():
    keyboard = InlineKeyboardBuilder()
    for i, bitch in enumerate(bitches):
        keyboard.add(InlineKeyboardButton(text=bitch, callback_data=f'bitch{i}'))
    return keyboard.adjust(2).as_markup()
