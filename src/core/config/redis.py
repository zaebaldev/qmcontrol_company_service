from pydantic import BaseModel
from pydantic.networks import RedisDsn


class RedisConfig(BaseModel):
    url: RedisDsn
    port: int
    host: str
