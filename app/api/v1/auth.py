from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from db.database import SessionLocal
from app.schemas.auth import RegisterRequest, RegisterResponse
from app.services.auth_service import register_user

router = APIRouter(prefix="/api/v1/auth", tags=["auth"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/register", response_model=RegisterResponse, status_code=201)
def register(request: RegisterRequest, db: Session = Depends(get_db)):
    try:
        return register_user(db, request)
    except HTTPException:
        # Re-raise FastAPI HTTPExceptions
        raise
    except Exception as exc:
        # Generic error -> 500
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(exc))
