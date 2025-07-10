from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Category")],
    [KeyboardButton(text="DATA"), KeyboardButton(text="Contacts")]
])