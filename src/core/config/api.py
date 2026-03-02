from pydantic import BaseModel


class ApiV1Prefix(BaseModel):
    prefix: str = "/v1"
    companies: str = "/companies"


class ApiPrefix(BaseModel):
    prefix: str = "/api"
    v1: ApiV1Prefix = ApiV1Prefix()
