from aiogram import types, Router
from aiogram.filters.command import Command
from keyboards.keyboards import kb1
from keyboards.keywords import keywords_hello, keywords_cmd_info

router= Router(name=__name__)
@router.message(Command('start'))
async def cmd_start(message: types.Message):
    await message.answer(f"Приветствую тебя, геймер! Я — телеграмм-бот компьютерного клуба Cyber-Pro.")
    await message.answer(f"Какой у тебя вопрос?", reply_markup=kb1)
@router.message(Command('info'))
async def cmd_info(message: types.Message):
    print(message.chat)
    await message.answer("Я — телеграмм-бот компьютерного клуба Cyber-Pro.")
    await message.answer("Основные команды:")
    await message.answer("/start")
    await message.answer("/info")
    await message.answer("/rent")
    await message.answer("/training")
    await message.answer("/tournament")
    await message.answer("/support")
    await message.answer("/discount")
@router.message()
async def msg_echo(message: types.Message):
    msg_user = message.text.lower()
    if any(keyword in msg_user for keyword in keywords_hello):
        await message.answer('Приветствую тебя, геймер!', reply_markup=kb1)
    elif any(keyword in msg_user for keyword in keywords_cmd_info):
        await cmd_info(message)
    else:
        await message.answer('Я не знаю такого слова!', reply_markup=kb1)
