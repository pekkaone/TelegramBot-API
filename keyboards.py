from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

main = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="/myinfo"), KeyboardButton(text="github")],
    [KeyboardButton(text="/AboutBot"), KeyboardButton(text="Contacts")]
],  
                            resize_keyboard=True,
                            input_field_placeholder="Choose the command")

settings = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Github', url='https://github.com/pekkaone')]
    ])