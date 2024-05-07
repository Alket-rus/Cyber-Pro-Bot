from aiogram import types, Router
from aiogram.filters.command import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from keyboards.keywords import keywords_training
from keyboards.keyboards import kb1, confirm_keyboard
from keyboards.keyboards_select import make_row_keyboard

router = Router(name=__name__)


keyboard_training_start = ['Полный 0', 'Опытный', 'Уже играл на турнирах']

class TrainingStates(StatesGroup):
    CHOOSING = State()
    MESSAGE = State()

async def start_training(message: types.Message, state: FSMContext):
    name = message.chat.first_name
    await message.answer(f"Я рад тебя видеть, {name}! Выбери свой уровень подготовки.", reply_markup=make_row_keyboard(keyboard_training_start))
    await state.set_state(TrainingStates.CHOOSING)

@router.message(TrainingStates.CHOOSING)
async def choose_preparation_training(message: types.Message, state: FSMContext):
    await state.update_data(choose_preparation_training=message.text.lower())
    if message.text == "Полный 0":
        await full_0(message, state)
    elif message.text == "Опытный":
        await experienced(message, state)
    elif message.text == "Уже играл на турнирах":
        await played_in_tournaments(message, state)

async def full_0(message: types.Message, state: FSMContext):
    await message.answer("Вам подойдет: «Полный курс подготовки к турнирам (20 часов)»")
    await message.answer(("Примите вызов и готовьтесь к доминированию на турнирах с нашим полным курсом подготовки к турнирам продолжительностью 20 часов! Этот интенсивный курс разработан нашими выдающимися тренерами, чтобы предоставить вам все необходимые инструменты для достижения успеха в мире киберспорта. На протяжении 20 часов вы будете погружены в интенсивные тренировки, которые охватывают все аспекты вашей игры. Наши эксперты проведут вас через тщательно разработанные уроки, нацеленные на улучшение вашей техники, стратегии и командной работы. Этот курс идеально подходит для игроков всех уровней подготовки, от начинающих до опытных профессионалов. Вы получите персонализированные советы, анализ вашей игры и индивидуальный подход к вашему прогрессу. Подготовьтесь к тому, чтобы покорить сцену киберспорта с нашим полным курсом подготовки к турнирам. Разберитесь с каждым аспектом вашей игры, повысьте свои навыки до новых высот и докажите всему миру, что вы - настоящий чемпион!."))
    await message.answer("Стоимость: 32 000 рублей.")
    await message.answer("Хотите ли вы пройти обучение по «Полный курс подготовки к турнирам (20 часов)»? (подтвердить/вернуться в выбору)", reply_markup=confirm_keyboard)
    await state.set_state(TrainingStates.MESSAGE)

async def experienced(message: types.Message, state: FSMContext):
    await message.answer("Вам подойдет: «Интенсивный курс тренировок для участия в турнирах (15 часов)»")
    await message.answer(("Вступайте в ряды элиты киберспорта с нашим интенсивным курсом тренировок для участия в турнирах продолжительностью 15 часов! Этот курс специально разработан, чтобы помочь вам подготовиться к турнирам наивысшего уровня и достичь ваших амбициозных целей в киберспорте. В течение 15 часов вы будете заниматься под руководством наших опытных тренеров, которые обладают богатым опытом в индустрии киберспорта. Мы сосредоточимся на развитии вашей игровой стратегии, технических навыков и психологической подготовке, чтобы вы были готовы к любым вызовам, которые могут вас ожидать на турнире. Этот интенсивный курс подходит для игроков всех уровней, от начинающих до опытных профессионалов, которые стремятся к успеху на турнирной сцене. Вы получите персонализированные рекомендации, анализ вашей игры и индивидуальные тренировки, которые помогут вам раскрыть свой потенциал в киберспорте. Подготовьтесь к тому, чтобы сделать свой след в мире киберспорта с нашим интенсивным курсом тренировок для участия в турнирах. Давайте вместе добьемся вашего максимального успеха!."))
    await message.answer("Стоимость: 25 000 рублей.")
    await message.answer("Хотите ли вы пройти обучение по «Интенсивный курс тренировок для участия в турнирах (15 часов)»? (подтвердить/вернуться в выбору)", reply_markup=confirm_keyboard)
    await state.set_state(TrainingStates.MESSAGE)

async def played_in_tournaments(message: types.Message, state: FSMContext):
    await message.answer("Вам подойдет: «Пакет из 10 часов индивидуальных тренировок»")
    await message.answer(("Готовьтесь к достижению высот в мире киберспорта с нашим эксклюзивным пакетом из 10 часов индивидуальных тренировок! Наши опытные тренеры-профессионалы будут работать с вами в одном на один, чтобы развить ваши игровые навыки и стратегическое мышление. Этот пакет идеально подходит как для начинающих, стремящихся к освоению основ, так и для опытных игроков, желающих усовершенствовать свою игру до совершенства. Каждая сессия будет индивидуально настроена под ваши потребности и цели. Получите персонализированный подход к обучению, максимально эффективные методы тренировок и детальные аналитические отчеты о вашем прогрессе. Покажите миру свой истинный потенциал в киберспорте с нашим пакетом из 10 часов индивидуальных тренировок!."))
    await message.answer("Стоимость: 18 000 рублей.")
    await message.answer("Хотите ли вы пройти обучение по «Пакет из 10 часов индивидуальных тренировок»? (подтвердить/вернуться в выбору)", reply_markup=confirm_keyboard)
    await state.set_state(TrainingStates.MESSAGE)

@router.message(TrainingStates.MESSAGE)
async def confirm_training(message: types.Message, state: FSMContext):
    if message.text == "Подтвердить":
        await message.answer("Спасибо за подтверждение! Мы свяжемся с вами для уточнения деталей.", reply_markup=kb1)
        await state.set_state(None)
    elif message.text == "Вернуться в выбору":
        await message.answer("Возвращаемся к выбору подготовки:", reply_markup=make_row_keyboard(keyboard_training_start))
        await state.set_state(TrainingStates.CHOOSING)
    else:
        await message.answer("Используйте кнопки на клавиатуре для выбора действия.")

def contains_keywords(message: types.Message) -> bool:
    return any(keyword in message.text.lower() for keyword in keywords_training)

@router.message(Command("training"))
@router.message(contains_keywords)
async def handle_training_messages(message: types.Message, state: FSMContext):
    await start_training(message, state)
