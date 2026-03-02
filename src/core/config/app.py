from pydantic import BaseModel


class AppConfig(BaseModel):
    title: str = "QMControl"
    host: str = "0.0.0.0"
    port: int = 8000
