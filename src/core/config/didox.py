from pydantic import BaseModel


class DidoxConfig(BaseModel):
    base_url: str = "https://api.didox.uz"
    partner_token: str = ""
