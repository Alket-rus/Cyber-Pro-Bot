from aiogram import types, F, Router
from aiogram.filters.command import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from keyboards.keywords import keywords_tournament
from keyboards.keyboards import kb1, confirm_keyboard
from keyboards.keyboards_select import make_row_keyboard

router = Router(name=__name__)


keyboard_tournament_start = ['Strike: Global Offensive', 'League of Legends', 'Dota 2']

class TournamentStates(StatesGroup):
    CHOOSING = State()
    MESSAGE = State()

async def start_tournament(message: types.Message, state: FSMContext):
    name = message.chat.first_name
    await message.answer(f"Я рад тебя видеть, {name}! Пожалуйста, выберите игру, в которой вы хотели бы принять участие на турнире.", reply_markup=make_row_keyboard(keyboard_tournament_start))
    await state.set_state(TournamentStates.CHOOSING)

@router.message(TournamentStates.CHOOSING)
async def choose_games_tournament(message: types.Message, state: FSMContext):
    await state.update_data(choose_games_tournament=message.text.lower())
    if message.text == "Strike: Global Offensive":
        await message.answer("Вам подойдут следующие турниры:")
        await cs_go(message, state)
    elif message.text == "League of Legends":
        await message.answer("Вам подойдут следующие турниры:")
        await lol(message, state)
    elif message.text == "Dota 2":
        await message.answer("Вам подойдут следующие турниры:")
        await dota(message, state)

async def cs_go(message: types.Message, state: FSMContext):
    await message.answer("\n".join(["CS:GO CHAMPIONSHIP",
                        "Дата: 2024-01-15",
                        "Время: 12:00",
                        "Призовой фонд: $10,000"]))
    await message.answer("Вы хотите подать заявку на участие? (подтвердить/вернуться в выбору)", reply_markup=confirm_keyboard)
    await state.set_state(TournamentStates.MESSAGE)

async def lol(message: types.Message, state: FSMContext):
    await message.answer("\n".join(["LEAGUE OF LEGENDS TOURNAMENT",
                        "Дата: 2024-01-22",
                        "Время: 14:00",
                        "Призовой фонд: $15,000"]))
    await message.answer("\n".join(["LEAGUE OF LEGENDS MSI",
                        "Дата: 2024-06-28",
                        "Время: 18:00",
                        "Призовой фонд: $15,000"]))
    await message.answer("\n".join(["LEAGUE OF LEGENDS CYBER-PRO CHAMPIONSHIP",
                        "Дата: 2024-12-10",
                        "Время: 17:00",
                        "Призовой фонд: $25,000"]))
    await message.answer("Вы хотите подать заявку на участие? (подтвердить/вернуться в выбору)", reply_markup=confirm_keyboard)
    await state.set_state(TournamentStates.MESSAGE)

async def dota(message: types.Message, state: FSMContext):
    await message.answer("\n".join(["DOTA 2 INVITATIONAL",
                        "Дата: 2024-02-10",
                        "Время: 13:00",
                        "Призовой фонд: $20,000"]))
    await message.answer("\n".join(["DOTA 2 CYBER-PRO CHAMPIONSHIP",
                        "Дата: 2024-12-22",
                        "Время: 16:30",
                        "Призовой фонд: $25,000"]))
    await message.answer("Вы хотите подать заявку на участие? (подтвердить/вернуться в выбору)", reply_markup=confirm_keyboard)
    await state.set_state(TournamentStates.MESSAGE)

@router.message(TournamentStates.MESSAGE)
async def confirm_tournament(message: types.Message, state: FSMContext):
    if message.text == "Подтвердить":
        await message.answer("Спасибо за подтверждение! Мы свяжемся с вами для уточнения деталей.", reply_markup=kb1)
        await state.set_state(None)
    elif message.text == "Вернуться в выбору":
        await message.answer("Возвращаемся к выбору комплектующих:", reply_markup=make_row_keyboard(keyboard_tournament_start))
        await state.set_state(TournamentStates.CHOOSING)
    else:
        await message.answer("Используйте кнопки на клавиатуре для выбора действия.")

def contains_keywords(message: types.Message) -> bool:
    return any(keyword in message.text.lower() for keyword in keywords_tournament)

@router.message(Command("tournament"))
@router.message(contains_keywords)
async def handle_tournament_messages(message: types.Message, state: FSMContext):
    await start_tournament(message, state)
