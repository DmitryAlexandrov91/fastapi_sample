import os

from loguru import logger
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    BASE_DIR: str = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    DB_URL: str = f"sqlite+aiosqlite:///{BASE_DIR}/data/db.sqlite3"
    SECRET_KEY: str
    ALGORITHM: str
    TOKEN: str

    FORMAT_LOG: str = "{time:YYYY-MM-DD at HH:mm:ss} | {level} | {message}"
    LOG_ROTATION: str = "10 MB"

    model_config = SettingsConfigDict(env_file=f"{BASE_DIR}/.env")


settings = Settings()
database_url = settings.DB_URL


def configure_logging() -> None:
    """Концигурация loguru."""
    log_file_path = os.path.join(
        settings.BASE_DIR, "log.txt")
    logger.add(
        log_file_path,
        format=settings.FORMAT_LOG,
        level="INFO",
        rotation=settings.LOG_ROTATION)
