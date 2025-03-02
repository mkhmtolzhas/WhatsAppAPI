from pydantic_settings import BaseSettings
from dotenv import load_dotenv

load_dotenv()

class Settings(BaseSettings):
    ultramsg_instance_id: str
    ultramsg_token: str

    class Config:
        env_file = ".env"

settings = Settings()