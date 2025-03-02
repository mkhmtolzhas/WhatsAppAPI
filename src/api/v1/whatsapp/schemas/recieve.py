from pydantic import BaseModel, Field
from typing import Optional, Dict, List


class DataModel(BaseModel):
    id: str
    from_: str = Field(alias="from")
    to: str
    author: Optional[str] = None
    pushname: Optional[str] = None
    ack: Optional[str] = None
    type: str
    body: Optional[str] = None
    media: Optional[str] = None
    fromMe: bool
    self: bool
    isForwarded: bool
    isMentioned: bool
    quotedMsg: Dict
    mentionedIds: List[str]
    time: int


class RecieveMessage(BaseModel):
    event_type: str
    instanceId: str
    id: Optional[str] = None
    referenceId: Optional[str] = None
    hash: str
    data: DataModel

    class Config:
        from_attributes = True


