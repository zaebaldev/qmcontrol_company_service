__all__ = ("broker",)

from faststream.rabbit import RabbitBroker

from core.config import settings

broker = RabbitBroker(
    str(settings.rabbitmq.url),
)
