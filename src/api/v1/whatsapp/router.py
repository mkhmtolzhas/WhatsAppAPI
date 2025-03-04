from fastapi import APIRouter
from .exeptions import WhatsAppException
from .service import service
from .schemas.message import SendMessage, SendVoice
from .schemas.recieve import RecieveMessage
from .utils import WhatsAppUtils
from src.core.broker.client import broker_client

router = APIRouter(prefix="/whatsapp", tags=["WhatsApp"])

@router.post("/send_message")
async def send_message(data: SendMessage):
    if not WhatsAppUtils.is_valid_phone_number(data.to):
        raise WhatsAppException.InvalidPhoneNumber()
    if not data.body:
        raise WhatsAppException.InvalidMessage()
    return await service.send_message(data.to, data.body)

@router.post("/send_voice")
async def send_voice(data: SendVoice):
    if not WhatsAppUtils.is_valid_phone_number(data.to):
        raise WhatsAppException.InvalidPhoneNumber()
    if not data.audio:
        raise WhatsAppException.InvalidAudio()
    return await service.send_audio(data.to, data.audio)


@router.post("/on_message")
async def on_message(data: RecieveMessage):
    message = {
        "user": data.data.from_,
        "response": data.data.body
    }
    await broker_client.publish(message)
    return {"status": "OK"}