from pydantic import BaseModel


class SQLAlchemyConfig(BaseModel):
    echo: bool = False
    echo_pool: bool = False
    pool_size: int = 50
    max_overflow: int = 10
    naming_convention: dict[str, str] = {
        "ix": "ix_%(column_0_label)s",
        "uq": "uq_%(table_name)s_%(column_0_N_name)s",
        "ck": "ck_%(table_name)s_%(constraint_name)s",
        "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
        "pk": "pk_%(table_name)s",
    }


class DatabaseConfig(BaseModel):
    name: str = "postgres"
    host: str = "localhost"
    port: int = 5432
    user: str = "postgres"
    password: str
    driver: str = "postgresql+asyncpg"
    sqla: SQLAlchemyConfig = SQLAlchemyConfig()

    @property
    def async_url(self) -> str:
        return f"{self.driver}://{self.user}:{self.password}@{self.host}:{self.port}/{self.name}"
