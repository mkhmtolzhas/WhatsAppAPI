from fastapi import FastAPI
from src.core.messaging.broker import broker
from src.api.v2.whatsapp.router import consuming

class Listener:
    @staticmethod
    async def startup():
        await broker.connect()
        await consuming()
    
    @staticmethod
    async def shutdown():
        await broker.close()

    @staticmethod
    def init_listeners(app: FastAPI):
        app.add_event_handler("startup", Listener.startup)
        app.add_event_handler("shutdown", Listener.shutdown)