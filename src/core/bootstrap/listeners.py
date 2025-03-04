from fastapi import FastAPI
from ..broker.client import broker_client
from src.api.v1.whatsapp.service import service


class Listener:
    @staticmethod
    async def startup():
        await broker_client.connect()
        await broker_client.subscribe(service.send_message)
    
    @staticmethod
    async def shutdown():
        await broker_client.close()
        if broker_client.subtask:
            broker_client.subtask.cancel()
            broker_client.subtask = None #TODO: Add getter for subtask
        
    @staticmethod
    def init_listeners(app: FastAPI):
        app.add_event_handler("startup", Listener.startup)
        app.add_event_handler("shutdown", Listener.shutdown)
        
    
    

