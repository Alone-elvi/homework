"""
FastAPI main.py
"""
from datetime import timezone, datetime
from enum import Enum
from typing import List, Optional
from fastapi import FastAPI, Request, status
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import ValidationException
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field
from .settings import settings

app = FastAPI(title="Homework check", version="0.1.0")


@app.exception_handler(ValidationException)
async def validation_exception_handler(request: Request, exc: ValidationException):
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content={"detail": exc.errors(), "body": exc.body},
    )


fake_roles = [
    {"id": 1, "role": "admin"},
    {"id": 2, "role": "teacher"},
    {"id": 3, "role": "student"},
]


fake_users = [
    {
        "id": 1,
        "created_at": "2023-11-29T08:45:37.875Z",
        "role_id": {
            "id": 2,
            "created_at": "2023-11-29T08:39:49.822Z",
            "role": "teacher",
        },
        "name": "admin",
    },
    {"id": 2, "role_id": 2, "name": "Larissa"},
    {"id": 3, "role_id": 3, "name": "Lev"},
]


fake_questions = [
    {
        "id": 1,
        "user_id": 2,
        "question": "What is the capital of France?",
        "answer": "Paris",
    },
    {
        "id": 2,
        "user_id": 2,
        "question": "What is the capital of Germany?",
        "answer": "Berlin",
    },
]


class UsersRole(BaseModel):
    """User model

    Args:
        BaseModel (BaseModel): Pydantic BaseModel
    """

    id: int = Field(ge=1, default=1)
    created_at: datetime = Field(default_factory=lambda: datetime.now(tz=timezone.utc))
    role: str


class UserDegreeType(Enum):
    """User Degree type
    Args:
        Enum (Enum): Pydantic Enum
    """

    NEWBE = "newbe"
    STUDENT = "student"
    MASTER = "master"
    EXPERT = "expert"


class UserDegree(BaseModel):
    """User Degree model

    Args:
        id (int): The ID of the user degree.
        created_at (datetime): The timestamp when the user degree was created.
        type_degree (str): The type of degree.

    """

    id: int = Field(ge=1, default=1)
    created_at: datetime = Field(default_factory=lambda: datetime.now(tz=timezone.utc))
    type_degree: UserDegreeType


class User(BaseModel):
    """User model

    Args:
        BaseModel (BaseModel): Pydantic BaseModel
    """

    id: int = Field(ge=1, default=1)
    created_at: datetime = Field(default_factory=lambda: datetime.now(tz=timezone.utc))
    role_id: UsersRole
    name: str
    degree: Optional[List[UserDegree]] = Field(default_factory=list)


class Status(BaseModel):
    """Status
    args: status: str  = "ok"
    """

    status: str = "ok"


@app.get(settings.main_url, response_model=Status)
async def status() -> Status:
    """
    A function to handle the GET request for the "status" endpoint.

    Parameters:
        None

    Returns:
        A "Status" object representing the status of the application.
    """
    return Status()


@app.get("/users/{user_id}", response_model=List[User])
def get_user(user_id: int):
    """Get user by id

    Args:
        user_id (int): user id

    Returns:
            dict : user
    """
    return [user for user in fake_users if user.get("id") == user_id]


@app.get("/questions")
def get_questions(limit: int = 10, offset: int = 0):
    """Get questions

    Args:
        limit (int, optional): limit. Defaults to 10.
        offset (int, optional): offset. Defaults to 0.
    Returns:
        list : questions
    """
    return fake_questions[offset:][:limit]


@app.post("/users/{user_id}")
def change_user(user_id: int, new_name: str):
    """Change user name

    Args:
        user_id (int): user id
        new_name (str): new name

    Returns:
        dict : user
    """
    current_user = list(filter(lambda user: user.get("id") == user_id, User))[0]
    current_user["name"] = new_name
    return {"status": 200, "data": current_user}


@app.post("/users")
def create_user(new_users: List[User]):
    """Create user

    Args: new_user(dict): user data
    Returns: list : List[Users]
             dict: status
    """
    fake_users.extend(new_users)
    return {"status": 200, "data": fake_users}


@app.post("/users_roles")
def create_users_role(new_users_role: List[UsersRole]):
    """Create user

    Args: new_user(dict): user data
    Returns: list : List[Users]
             dict: status
    """
    UsersRole.extend(new_users_role)
    return {"status": 200, "data": UsersRole}
