from fastapi import APIRouter, Request
from .exeptions import WhatsAppException
from .service import service
from .schemas import SendMessage, SendVoice
from .utils import WhatsAppUtils

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
async def on_message(data: Request):
    await service.send_message(to="+77767301903", body=data.json())
    return {"status": "OK"}