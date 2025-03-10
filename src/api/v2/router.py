from fastapi import APIRouter
from .whatsapp.router import router as whatsapp_router

router = APIRouter(prefix="/v2")

router.include_router(whatsapp_router)