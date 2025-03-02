from aiohttp import ClientSession
from src.core.config import settings


class WhatsAppService:
    def __init__(self):
        self.instance_id = settings.ultramsg_instance_id
        self.token = settings.ultramsg_token
        self.host = f"https://api.ultramsg.com/{self.instance_id}"
    
    async def send_message(self, to: str, body: str):
        url = f"{self.host}/messages/chat"
        data = {
            "token": self.token,
            "to": to,
            "body": body,
        }

        async with ClientSession() as session:
            async with session.post(url, json=data) as response:
                return await response.json()


    async def send_audio(self, to: str, audio: str):
        url = f"{self.host}/messages/voice"
        data = {
            "token": self.token,
            "to": to,
            "audio": audio,
        }
        async with ClientSession() as session:
            async with session.post(url, json=data) as response:
                return await response.json()
    

service = WhatsAppService()