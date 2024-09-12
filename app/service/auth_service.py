# service/leave_service.py
from fastapi import HTTPException
from fastapi.openapi.utils import status_code_ranges
from sqlalchemy.orm import Session
from app.repository.user_repository import UserRepository
from app.core.security import verify_password, create_access_token, get_password_hash
from datetime import timedelta

#auth
class AuthService:
    def __init__(self, db: Session):
        self.user_repository = UserRepository(db)

    def login(self, email_id: str, password: str):
        user = self.user_repository.get_user_by_email(email_id=email_id)
        if not user or not verify_password(password, user.hashed_password):
            raise HTTPException(status_code=404, detail="Incorrect username or password")

        access_token_expires = timedelta(minutes=30)
        access_token = create_access_token(
            data={"sub": user.email_id}, expires_delta=access_token_expires
        )
        return {"access_token": access_token, "token_type": "bearer"}