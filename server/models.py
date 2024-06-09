from pydantic import BaseModel, Field
from typing import Literal


class Message(BaseModel):
    role: Literal["assistant", "system", "user"] = Field(default="user")
    content: str | None


class ChatBody(BaseModel):
    messages = list[Message]
