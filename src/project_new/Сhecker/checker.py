import os
from dotenv import load_dotenv
from passlib.context import CryptContext

load_dotenv()

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def hash_line(line: str) -> str:
    return pwd_context.hash(line)


LOGIN_HASH = hash_line(os.getenv("ADMIN_LOGIN"))
PASSWORD_HASH = hash_line(os.getenv("ADMIN_PASSWORD"))


def verify_login(check_login: str) -> bool:
    return pwd_context.verify(check_login, LOGIN_HASH)


def verify_password(check_password: str) -> bool:
    return pwd_context.verify(check_password, PASSWORD_HASH)