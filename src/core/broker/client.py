import asyncio
from redis.asyncio import Redis
from json import loads
from ..config import settings

class BrokerClient:
    def __init__(self, host: str, port: int, password: str, username: int):
        self.client = Redis(host=host, port=port, password=password, username=username, decode_responses=True)
        self.subscribe_channel = 'llm_to_whatsapp'
        self.publish_channel = 'whatsapp_to_llm'
        self.pubsub = self.client.pubsub()
        self.subtask = None
    

    async def connect(self):
        await self.client.ping() 


    async def publish(self, message: str):
        await self.client.publish(self.publish_channel, message)


    async def listen(self, callback: callable):
        await self.pubsub.subscribe(self.subscribe_channel)

        try:
            while True:
                message = await self.pubsub.get_message(ignore_subscribe_messages=True)
                if message:
                    message = loads(message['data'])
                    await callback(to=message['user'], body=message['response'])
                await asyncio.sleep(0.01)
        except Exception as e:
            print(e)
    
    async def subscribe(self, callback: callable):
        self.subtask = asyncio.create_task(self.listen(callback))

    async def close(self):
        await self.client.close()

broker_client = BrokerClient(
    host=settings.redis_host,
    port=settings.redis_port,
    password=settings.redis_password,
    username=settings.redis_username
)
        
        

        