from aiogram import types, F, Router
from aiogram.filters.command import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from keyboards.keywords import keywords_support
from keyboards.keyboards import kb1, confirm_keyboard
from keyboards.keyboards_select import make_row_keyboard

router = Router(name=__name__)


keyboard_support_start = ['Аренда', 'Тренировки', 'Турниры']

class SupportStates(StatesGroup):
    CHOOSING = State()
    MESSAGE = State()

async def start_support(message: types.Message, state: FSMContext):
    name = message.chat.first_name
    await message.answer(f"Я рад тебя видеть, {name}! Пожалуйста, выберите категорию, по которой у вас возникли вопросы, или напишите в чат свой вопрос.", reply_markup=make_row_keyboard(keyboard_support_start))
    await state.set_state(SupportStates.CHOOSING)

@router.message(SupportStates.CHOOSING)
async def choose_technical_support(message: types.Message, state: FSMContext):
    await state.update_data(choose_technical_support=message.text.lower())
    if message.text == "Аренда":
        await message.answer("Вы уверены, что ваш вопрос связан с арендой компьютеров? (подтвердить/вернуться в выбору)", reply_markup=confirm_keyboard)
        await state.set_state(SupportStates.MESSAGE)
    elif message.text == "Тренировки":
        await message.answer("Вы уверены, что ваш вопрос связан с киберспортивными тренировками? (подтвердить/вернуться в выбору)", reply_markup=confirm_keyboard)
        await state.set_state(SupportStates.MESSAGE)
    elif message.text == "Турниры":
        await message.answer("Вы уверены, что ваш вопрос связан с турнирами, что проводятся в нашем клубе? (подтвердить/вернуться в выбору)", reply_markup=confirm_keyboard)
        await state.set_state(SupportStates.MESSAGE)
    else:
        await message.answer("Спасибо за вопрос! Мы свяжемся с вами для уточнения деталей.", reply_markup=kb1)
        await state.set_state(None)

@router.message(SupportStates.MESSAGE)
async def confirm_tournament(message: types.Message, state: FSMContext):
    if message.text == "Подтвердить":
        await message.answer("Спасибо за подтверждение! Мы свяжемся с вами для уточнения деталей.", reply_markup=kb1)
        await state.set_state(None)
    elif message.text == "Вернуться в выбору":
        await message.answer("Возвращаемся к выбору комплектующих:", reply_markup=make_row_keyboard(keyboard_support_start))
        await state.set_state(SupportStates.CHOOSING)
    else:
        await message.answer("Используйте кнопки на клавиатуре для выбора действия.")

def contains_keywords(message: types.Message) -> bool:
    return any(keyword in message.text.lower() for keyword in keywords_support)

@router.message(Command("support"))
@router.message(contains_keywords)
async def handle_support_messages(message: types.Message, state: FSMContext):
    await start_support(message, state)
