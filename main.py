import asyncio
import confing
from aiogram import Bot, Dispatcher
import logging
from handlers.common import router as router_common_start



async def main():
    #Логирование
    logging.basicConfig(level=logging.INFO)

    #Обьект бота
    bot = Bot(token=confing.tokentelegrambot)

    #Обьект диспетчера
    dp = Dispatcher()
    dp.include_router(router_common_start)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
