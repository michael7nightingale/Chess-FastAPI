from pydantic import BaseModel, Field


class UserLogin(BaseModel):
    """Schema for logging"""
    username: str = Field(min_length=5, max_length=40)
    password: str = Field(min_length=5, max_length=40)


class UserShow(BaseModel):
    """Schema for response"""
    id: str
    username: str
    first_name: str | None = None
    last_name: str | None = None
    is_superuser: bool


class UserRegister(BaseModel):
    """Schema for registering"""
    username: str
    password: str = Field(min_length=5, max_length=40)
    email: str = Field(min_length=5, max_length=50)
    first_name: str | None = None
    last_name: str | None = None
