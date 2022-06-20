from fastapi import FastAPI, Depends, HTTPException
from routes.v1 import Blog_v1
from starlette.status import HTTP_401_UNAUTHORIZED
from fastapi.security import OAuth2PasswordRequestForm
from models.jwt_user import JWTUser
from utils.db_object import db
from utils.security import authenticate_user, create_jwt_token


Blog = FastAPI(
    title="inventory API Documentation",
    description="it is an inventory Blog API",
    version="1.0.0",
)

Blog.include_router(
    Blog_v1,
    prefix="/v1"
    # dependencies=[Depends(check_jwt_token)]
)


@Blog.on_event("startup")
async def startup():
    await db.connect()


@Blog.on_event("shutdown")
async def shutdown():
    await db.disconnect()


@Blog.post("/token", tags=["Security"])
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    jwt_user_dict = {"username": form_data.username, "password": form_data.password}
    jwt_user = JWTUser(**jwt_user_dict)
    user = await authenticate_user(jwt_user)

    if user is None:
        raise HTTPException(status_code=HTTP_401_UNAUTHORIZED)

    jwt_token = create_jwt_token(user)
    return {"access_token": jwt_token}
