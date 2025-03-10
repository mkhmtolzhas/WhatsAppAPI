from .broker import broker
import asyncio

class MessagingUtils:
    @staticmethod
    async def consume_messages():
        await broker.connect()
        await broker.consume("whatsapp", MessagingUtils.on_message, "whatsapp", "whatsapp")