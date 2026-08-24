from sqlalchemy.orm import Session
from fastapi import HTTPException, status

from app.repositories.user_repository import get_user_by_email, create_user
from app.core.security import hash_password
from app.schemas.auth import RegisterRequest, RegisterResponse


def register_user(db: Session, request: RegisterRequest) -> RegisterResponse:
    # Check if email already exists
    existing = get_user_by_email(db, request.email)
    if existing:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email already registered")

    password_hash = hash_password(request.password)
    user = create_user(db, email=request.email, password_hash=password_hash, display_name=request.display_name)

    return RegisterResponse.from_orm(user)
