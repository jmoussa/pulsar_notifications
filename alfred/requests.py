from pydantic import BaseModel


class UserTokenRequest(BaseModel):
    username: str
    password: str


class AnonymizeRequest(BaseModel):
    username: str
    password: str
    data: dict


class PulsarMessage(BaseModel):
    message: str or dict
