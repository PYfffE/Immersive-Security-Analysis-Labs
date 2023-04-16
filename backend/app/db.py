import uuid

from backend.app.models.user import User


def get_user_by_username(username: str) -> User:
    return User(str(uuid.uuid4()), username, 'password')


def get_user_by_id(user_id: str) -> User:
    return User(user_id, "username", 'password')