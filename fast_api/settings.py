"""
Settings for FastAPI
"""
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Settings for FastAPI

    Args:
        BaseSettings (BaseSettings): Pydantic BaseSettings
    """
    API_V1_STR: str = "/api/v1"
    main_url: str = ""


settings = Settings()
