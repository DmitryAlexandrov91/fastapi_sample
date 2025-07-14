import asyncio

from aiogram import Bot, Dispatcher
from loguru import logger

from app.config import configure_logging, settings


configure_logging()


bot = Bot(settings.TOKEN)
dp = Dispatcher()


async def main() -> None:
    """Основная функция main запускающая поллинг."""
    await dp.start_polling(bot)


if __name__ == '__main__':
    try:
        asyncio.run(main())
        logger.info("Бот запускается...")
    except KeyboardInterrupt:
        logger.info("Бот остановлен.")
