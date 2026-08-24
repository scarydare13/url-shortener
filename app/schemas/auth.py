from datetime import datetime
from typing import Optional
from uuid import UUID

from pydantic import BaseModel, EmailStr, constr


class RegisterRequest(BaseModel):
    email: EmailStr
    display_name: Optional[constr(max_length=100)] = None
    password: constr(min_length=8, max_length=128)


class RegisterResponse(BaseModel):
    id: UUID
    email: EmailStr
    display_name: Optional[str] = None
    is_active: bool
    is_verified: bool
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
