from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="/myinfo")],
    [KeyboardButton(text="about bot"), KeyboardButton(text="Contacts")]
])