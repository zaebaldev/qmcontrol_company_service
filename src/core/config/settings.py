from pathlib import Path

from pydantic_settings import (
    BaseSettings,
    SettingsConfigDict,
)

from core.config.api import ApiPrefix
from core.config.app import AppConfig
from core.config.cors import CorsConfig
from core.config.database import DatabaseConfig
from core.config.gunicorn import GunicornConfig
from core.config.logging import LoggingConfig
from core.config.rabbitmq import RabbitConfig
from core.config.redis import RedisConfig

CONFIG_DIR = Path(__file__).resolve().parent
ENVS_DIR = CONFIG_DIR / "envs"


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_nested_delimiter="__",
        env_prefix="APP__",
        case_sensitive=False,
        extra="ignore",
        env_file=(
            ENVS_DIR / ".env.template",
            ENVS_DIR / ".env",
        ),
    )
    db: DatabaseConfig
    logging: LoggingConfig = LoggingConfig()
    app: AppConfig = AppConfig()
    gunicorn: GunicornConfig = GunicornConfig()
    api: ApiPrefix = ApiPrefix()
    cors: CorsConfig = CorsConfig()
    redis: RedisConfig
    rabbitmq: RabbitConfig


settings = Settings()
