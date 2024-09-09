# app/model/user.py
from pydantic import BaseModel

class UserModel(BaseModel):
    username: str
    hashed_password: str
