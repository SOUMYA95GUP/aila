# repository/user_repository.py
from sqlalchemy.orm import Session
from app.model.user import User
from app.core.security import get_password_hash

class UserRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_user(self, user_data):
        user = User(**user_data)
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return user

    def get_user(self, user_id: int):
        return self.db.query(User).filter(User.id == user_id).first()

    def get_users(self, skip: int = 0, limit: int = 10):
        return self.db.query(User).offset(skip).limit(limit).all()

    def update_user(self, user_id: int, user_data):
        user = self.get_user(user_id)
        if user:
            for key, value in user_data.items():
                setattr(user, key, value)
            self.db.commit()
            self.db.refresh(user)
        return user

    def delete_user(self, user_id: int):
        user = self.get_user(user_id)
        if user:
            self.db.delete(user)
            self.db.commit()
        return user

    def get_user_by_email(self, email_id: str):
        user = self.db.query(User).filter(User.email_id == email_id).first()
        if user:
            user.hashed_password = get_password_hash("password")
        return user