"""
Settings for FastAPI
"""
from pydantic import BaseModel
from pydantic_settings import BaseSettings


class User(BaseModel):
    """User model

    Args:
        BaseModel (BaseModel): Pydantic BaseModel
    """

    username: str
    email: str
    full_name: str
    disabled: bool


class Settings(BaseSettings):
    """Settings for FastAPI

    Args:
        BaseSettings (BaseSettings): Pydantic BaseSettings
    """

    API_V1_STR: str = "/api/v1"
    main_url: str = ""
    status: str = "status"


settings = Settings()
