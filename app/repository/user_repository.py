# app/repository/user_repository.py
from app.model.user import UserModel
from app.core.security import get_password_hash

async def get_user_by_username(username: str) -> UserModel | None:
    # Replace this with your actual data source (e.g., SQL or DynamoDB)
    hashed_password = get_password_hash("yourpassword")
    user = UserModel(username=username, hashed_password=hashed_password)
    return user
