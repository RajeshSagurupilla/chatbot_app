from pydantic import BaseModel


class Chat(BaseModel):
    model:str
    prompt:str
    