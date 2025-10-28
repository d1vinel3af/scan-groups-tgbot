from pydantic_settings import BaseSettings
from pydantic_settings import SettingsConfigDict

class Settings(BaseSettings):
    api_id: str
    api_hash: str
    api_bot_token: str
    
    

settings = Settings()