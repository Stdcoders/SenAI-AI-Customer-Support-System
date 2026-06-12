from pydantic_settings import BaseSettings
class Settings(BaseSettings):
    APP_NAME: str = "SenAI Agentic CRM"
    APP_VERSION: str = "1.0.0"

    DATABASE_URL: str = "sqlite:///./senai.db"

    GOOGLE_API_KEY: str = "AIzaSyBxwlsjYs1ewGkLglO2SLkVHQ8t6enQGKQ"

    CHROMA_DB_PATH: str = "./chroma_db"

    EMBEDDING_MODEL: str = "all-MiniLM-L6-v2"

    class Config:
        env_file = ".env"


settings = Settings()