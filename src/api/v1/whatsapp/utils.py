import httpx
import asyncio
from re import fullmatch
from src.core.config import settings

class WhatsAppUtils:
    @staticmethod
    def is_valid_phone_number(phone_number: str) -> bool:
        return bool(fullmatch(r"^\+?7\d{10}$", phone_number))
    
    @staticmethod
    async def get_response(user: str, message: str):
        url = f"{settings.llm_host}/api/v1/llm/response"
        async with httpx.AsyncClient() as client:
            response = await client.post(url=url, json={"user": user, "message": message})
            return response.json()


    
