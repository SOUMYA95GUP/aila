# app/api/v1/endpoints/auth.py
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

from app.api.v1.endpoints.leave import get_leave_service
from app.core.security import verify_password, create_access_token, get_password_hash
from app.schema.auth_schema import Token
from app.repository.user_repository import UserRepository
from app.core import security
from fastapi import APIRouter, Depends, HTTPException
from datetime import timedelta
from app.core.security import create_access_token
from app.core.dependencies import authenticate_user
from app.service.auth_service import AuthService
from sqlalchemy.orm import Session
from app.core.database import get_db
# from app.core.config import ACCESS_TOKEN_EXPIRE_MINUTES
ACCESS_TOKEN_EXPIRE_MINUTES=30
router = APIRouter()


# For OAuth2 login form
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

def get_auth_service(db: Session = Depends(get_db)):
    return AuthService(db)


# Login endpoint
@router.post("/login", response_model=Token)
def login(form_data: OAuth2PasswordRequestForm = Depends(), service: AuthService = Depends(get_auth_service)):
    return service.login(form_data.username, form_data.password)


# Dependency for securing other routes
async def get_current_user(token: str = Depends(oauth2_scheme)):
    payload = security.decode_access_token(token)
    if payload is None:
        raise HTTPException(status_code=401, detail="Invalid authentication")
    return payload["sub"]

