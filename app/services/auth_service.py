from sqlalchemy.orm import Session

from app.core.security import hash_password
from app.models.user import User
from app.repositories.user_repository import (
    create_user,
    get_user_by_email,
)
from app.schemas.auth import RegisterRequest


def register_user(
    db: Session,
    request: RegisterRequest,
) -> User:

    # 1. Check whether email already exists
    existing_user = get_user_by_email(
        db,
        request.email,
    )

    if existing_user:
        raise ValueError("Email already registered")

    # 2. Hash password
    password_hash = hash_password(
        request.password
    )

    # 3. Create User model
    user = User(
        email=request.email,
        display_name=request.display_name,
        password_hash=password_hash,
    )

    # 4. Save user
    return create_user(db, user)