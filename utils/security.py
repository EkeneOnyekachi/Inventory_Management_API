from passlib.context import CryptContext
from models.jwt_user import JWTUser
import jwt
from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
import time
from datetime import datetime, timedelta
from utils.const import JWT_EXPIRATION_TIME_MINUTES, JWT_ALGORITH, JWT_SECRET_KEY
from utils.db_functions import db_check_token_user, db_check_jwt_username
from starlette.status import HTTP_401_UNAUTHORIZED


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth_schema = OAuth2PasswordBearer(tokenUrl="/token")


def get_hashed_password(password):
    return pwd_context.hash(password)


def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


# hashed = "$2b$12$flnSxXV9nDvpXScIzcQP.e/r06rzCcTobDn/TC6KawafRDeZ9eXxy"
# print(get_hashed_password("11223344"))


async def authenticate_user(user: JWTUser):
    potential_users = await db_check_token_user(user)
    is_valid = False
    for db_user in potential_users:
        if verify_password(user.password, db_user["password"]):
            is_valid = True

    if is_valid:
        return user

    return None


# Create access jwt token
def create_jwt_token(user: JWTUser):
    expiration = datetime.utcnow() + timedelta(minutes=JWT_EXPIRATION_TIME_MINUTES)
    jwt_payload = {"sub": user.username, "exp": expiration}

    jwt_token = jwt.encode(jwt_payload, JWT_SECRET_KEY, algorithm=JWT_ALGORITH)

    return jwt_token


async def check_jwt_token(token: str = Depends(oauth_schema)):
    try:
        jwt_payload = jwt.decode(token, JWT_SECRET_KEY, algorithms=JWT_ALGORITH)
        username = jwt_payload.get("sub")
        expiration = jwt_payload.get("exp")

        if time.time() < expiration:
            is_valid = await db_check_jwt_username(username)
            if is_valid:
                return True
            else:
                return False
    except Exception as e:
        raise HTTPException(status_code=HTTP_401_UNAUTHORIZED)


# print(get_hashed_password("pass1"))
