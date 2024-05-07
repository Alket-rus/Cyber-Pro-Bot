from aiogram import types, F, Router
from aiogram.filters.command import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from keyboards.keywords import keywords_rent
from keyboards.keyboards import kb1, confirm_keyboard
from keyboards.keyboards_select import make_row_keyboard

router = Router(name=__name__)


keyboard_rent_start = ['Общий зал', 'BootCamp VIP', 'Аренда TV']

class RentStates(StatesGroup):
    CHOOSING = State()
    MESSAGE = State()

async def start_rent(message: types.Message, state: FSMContext):
    name = message.chat.first_name
    await message.answer(f"Я рад тебя видеть, {name}! Выбери подходящие комплектующие для тебя.", reply_markup=make_row_keyboard(keyboard_rent_start))
    await state.set_state(RentStates.CHOOSING)

@router.message(RentStates.CHOOSING)
async def choose_computers_rent(message: types.Message, state: FSMContext):
    await state.update_data(choice_rent_components=message.text.lower())
    if message.text == "Общий зал":
        await message.answer("Вы выбрали общий зал. Информация о комплектующих будет отправлена.")
        await common_room(message, state)
    elif message.text == "BootCamp VIP":
        await message.answer("Вы выбрали BootCamp VIP. Информация о комплектующих будет отправлена.")
        await bootcamp_vip(message, state)
    elif message.text == "Аренда TV":
        await message.answer("Вы выбрали аренду TV. Информация о комплектующих будет отправлена.")
        await tv_rental(message, state)

async def common_room(message: types.Message, state: FSMContext):
    await message.answer("\n".join(["Комплектующие общего зала:",
                        "Процессор: Intel Core i7-10700K",
                        "Видеокарта: NVIDIA GeForce RTX 3070",
                        "Оперативная память: 16 ГБ",
                        "SSD: Patriot Burst 480GB SATA III"]))
    await message.answer("\n".join(["Периферия общего зала:",
                        "Монитор: ASUS ROG Strix XG279Q",
                        "Клавиатура: Logitech G Pro X",
                        "Мышь: Logitech G Pro Wireless",
                        "Наушники: HyperX Cloud II"]))
    await message.answer("Стоимость: 300 рублей/час.")
    await message.answer("Согласны ли вы на аренду? (подтвердить/вернуться в выбору)", reply_markup=confirm_keyboard)
    await state.set_state(RentStates.MESSAGE)

async def bootcamp_vip(message: types.Message, state: FSMContext):
    await message.answer("\n".join(["Комплектующие BootCamp VIP:",
                        "Процессор: Intel Core i9-10900K",
                        "Видеокарта: NVIDIA GeForce RTX 4090",
                        "Оперативная память: 32 ГБ",
                        "SSD: Samsung 970 PRO 1TB NVMe PCIe M.2 SSD"]))
    await message.answer("\n".join(["Периферия BootCamp VIP:",
                        "Монитор: ASUS ROG Swift",
                        "Клавиатура: Razer BlackWidow Elite",
                        "Мышь: Razer DeathAdder V2",
                        "Наушники: SteelSeries Arctis Pro"]))
    await message.answer("Стоимость: 800 рублей/час.")
    await message.answer("Согласны ли вы на аренду? (подтвердить/вернуться в выбору)", reply_markup=confirm_keyboard)
    await state.set_state(RentStates.MESSAGE)

async def tv_rental(message: types.Message, state: FSMContext):
    await message.answer("\n".join(["Комплектующие Аренда TV:",
                        "Экран: 60''",
                        "Консоль: Sony PlayStation 5 Digital Edition"]))
    await message.answer("Стоимость: 600 рублей/час.")
    await message.answer("Согласны ли вы на аренду? (подтвердить/вернуться в выбору)", reply_markup=confirm_keyboard)
    await state.set_state(RentStates.MESSAGE)

@router.message(RentStates.MESSAGE)
async def confirm_rental(message: types.Message, state: FSMContext):
    if message.text == "Подтвердить":
        await message.answer("Спасибо за подтверждение! Мы свяжемся с вами для уточнения деталей.", reply_markup=kb1)
        await state.set_state(None)
    elif message.text == "Вернуться в выбору":
        await message.answer("Возвращаемся к выбору комплектующих:", reply_markup=make_row_keyboard(keyboard_rent_start))
        await state.set_state(RentStates.CHOOSING)
    else:
        await message.answer("Используйте кнопки на клавиатуре для выбора действия.")

def contains_keywords(message: types.Message) -> bool:
    return any(keyword in message.text.lower() for keyword in keywords_rent)

@router.message(Command("rent"))
@router.message(contains_keywords)
async def handle_rent_messages(message: types.Message, state: FSMContext):
    await start_rent(message, state)
