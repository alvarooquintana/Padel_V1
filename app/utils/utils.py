from passlib.context import CryptContext
from databases.database import engine
from models.model import User



password_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def get_hashed_password(password: str) -> str:
    return password_context.hash(password)

def verify_password(plain_password, hashed_password):
    return password_context.verify(plain_password, hashed_password)

def find_user_by_email(email: str) -> User:
    user = engine.find_one(User, User.email == email)
    return user
