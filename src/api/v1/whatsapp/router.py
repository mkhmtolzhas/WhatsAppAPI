from fastapi import APIRouter
from .exeptions import WhatsAppException
from .service import service
from .schemas.message import SendMessage, SendVoice
from .schemas.recieve import RecieveMessage
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
async def on_message(data: RecieveMessage):
    response = await WhatsAppUtils.get_response(data.data.from_, data.data.body)

    await service.send_message(data.data.from_, response["response"])
    return {"status": "OK"}