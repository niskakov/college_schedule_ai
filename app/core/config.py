from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str = "sqlite:///./college_schedule.db"
    SECRET_KEY: str = "your-secret-key"
    
    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

settings = Settings()
