from aiogram import types, F, Router
from aiogram.filters.command import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from keyboards.keywords import keywords_discounts
from keyboards.keyboards import kb1
from keyboards.keyboards_select import make_row_keyboard

router = Router(name=__name__)


keyboard_discounts_start = ['Аренда', 'Тренировки']

class DiscountsStates(StatesGroup):
    MESSAGE = State()

async def start_discounts(message: types.Message, state: FSMContext):
    name = message.chat.first_name
    await message.answer(f"Я рад тебя видеть, {name}! Пожалуйста, укажите категорию проводимых акций, которая вас интересует.", reply_markup=make_row_keyboard(keyboard_discounts_start))
    await state.set_state(DiscountsStates.MESSAGE)

@router.message(DiscountsStates.MESSAGE)
async def choose_discounts(message: types.Message, state: FSMContext):
    await state.update_data(choose_discounts=message.text.lower())
    await message.answer("Благодарим за проявленный интерес! Мы свяжемся с вами, чтобы сообщить о проводимых акциях.", reply_markup=kb1)
    await state.set_state(None)


def contains_keywords(message: types.Message) -> bool:
    return any(keyword in message.text.lower() for keyword in keywords_discounts)

@router.message(Command("discount"))
@router.message(contains_keywords)
async def handle_discounts_messages(message: types.Message, state: FSMContext):
    await start_discounts(message, state)
