from aiogram import types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

button1 = types.KeyboardButton(text='Начать')
button2 = types.KeyboardButton(text='Информация')
button3 = types.KeyboardButton(text='Аренда компьютерного места')
button4 = types.KeyboardButton(text='Индивидуальные тренировки киберспортивных навыков')
button5 = types.KeyboardButton(text='Турниры')
button6 = types.KeyboardButton(text='Техническая поддержка и консультации')
button7 = types.KeyboardButton(text='Акции')

keyboard1 = [
[button1, button2, button3],
[button4, button5, button6,
 button7],
]

kb1 = types.ReplyKeyboardMarkup(keyboard=keyboard1, resize_keyboard=True)


confirm_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Подтвердить"),
            KeyboardButton(text="Вернуться в выбору")
        ]
    ],
    resize_keyboard=True  # Опционально: сделать клавиатуру масштабируемой
)