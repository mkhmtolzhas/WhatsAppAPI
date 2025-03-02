from pydantic import BaseModel

class MessageBase(BaseModel):
    to: str
    class Config:
        from_attributes = True


class SendMessage(MessageBase):
    body: str


class SendVoice(MessageBase):
    audio: str

