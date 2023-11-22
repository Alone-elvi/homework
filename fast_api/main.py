"""
FastAPI main.py
"""
from fastapi import FastAPI
from pydantic import BaseModel
from .settings import settings

app = FastAPI()


class Status(BaseModel):
    """Status
    args: status: str  = "ok"
    """

    status: str = "ok"


@app.get(settings.main_url + "status", response_model=Status)
async def status() -> Status:
    """
    A function to handle the GET request for the "status" endpoint.

    Parameters:
        None

    Returns:
        A "Status" object representing the status of the application.
    """
    return Status()
