from pydantic import BaseModel
from fastapi import Query


class User(BaseModel):
    firstname: str
    lastname: str
    username: str
    password: str
    email: str = Query(
        ..., regex="^([a-zA-Z0-9_\-\.]+)@([a-zA-Z0-9_\-\.]+)\.([a-zA-Z]{2,5})$"
    )
