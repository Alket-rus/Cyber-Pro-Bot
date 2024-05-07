from aiogram import types

def make_row_keyboard(item: list[str]) -> types.ReplyKeyboardMarkup:
    row = [types.KeyboardButton(text=item) for item in item]
    return types.ReplyKeyboardMarkup(keyboard=[row], resize_keyboard=True)