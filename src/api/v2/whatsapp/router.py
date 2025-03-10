import asyncio
import json
from aio_pika import IncomingMessage
from fastapi import APIRouter
from .service import service
from .schemas.recieve import RecieveMessage
from .utils import WhatsAppUtils
from src.core.messaging.broker import broker


router = APIRouter(prefix="/whatsapp", tags=["WhatsApp"])

async def callback(message: IncomingMessage):
    async with message.process():
        message = json.loads(message.body.decode())
        print(message)
        await service.send_message(message["user"], message["response"])

async def consuming():
    await broker.consume(callback=callback, queue_name="llm", exchange_name="llm", routing_key="llm")


@router.post("/on_message")
async def on_message(data: RecieveMessage):
    await WhatsAppUtils.publish_message(data.data.from_, data.data.body)
    return {"status": "OK"}