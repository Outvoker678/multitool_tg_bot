import asyncio
import logging

from aiogram import Bot, Dispatcher

from handlers.handlers import router

from config import TOKEN


async def main():
    """Точка входа для запуска Telegram-бота."""
    bot = Bot(token=TOKEN)
    dispatcher = Dispatcher()
    dispatcher.include_router(router)

    await dispatcher.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Exit")