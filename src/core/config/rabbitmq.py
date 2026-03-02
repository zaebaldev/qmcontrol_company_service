from pydantic import AmqpDsn, computed_field
from pydantic_settings import BaseSettings


class RabbitConfig(BaseSettings):
    host: str = "localhost"
    port: int = 5672
    user: str = "guest"
    password: str = "guest"
    vhost: str = "/"

    @computed_field
    @property
    def url(self) -> AmqpDsn:
        return AmqpDsn(
            f"amqp://{self.user}:{self.password}@{self.host}:{self.port}/{self.vhost}"
        )
