from fastapi import APIRouter
from .whatsapp.router import router as whatsapp_router

router = APIRouter(prefix="/v1")

router.include_router(whatsapp_router)