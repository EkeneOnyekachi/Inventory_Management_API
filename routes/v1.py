from fastapi import FastAPI, Body, Header, File, APIRouter, Depends
from fastapi.responses import RedirectResponse, HTMLResponse
from models.user import User
from models.item import Item, ItemDelete
from datetime import  datetime, date
from starlette.status import HTTP_201_CREATED
from starlette.responses import Response
from fastapi.security import OAuth2PasswordRequestForm
from utils.security import authenticate_user, create_jwt_token, check_jwt_token
from utils.security import get_hashed_password
from utils.db_functions import (db_insert_user, db_check_user,
                                db_get_item_with_id, db_insert_item,
                                db_update_item, db_get_all_item,
                                db_get_user_items,db_delete_item_with_id)
from utils.db import  execute, fetch




Blog_v1 = APIRouter()



#confirm
@Blog_v1.post("/registration", status_code=HTTP_201_CREATED, tags=["User"])
async def users_registration(user: User):
    user_info = user.dict()
    user_info["password"] = get_hashed_password(user_info["password"])
    user_obj = User(**user_info)
    new_user = await db_insert_user(user_obj)
    return {"result":"Registration successful"}


#confirm
@Blog_v1.post("/login",tags=["User"])
async def get_users_validation(email: str = Body(...), password: str = Body(...)
,jwt: bool = Depends(check_jwt_token)):
    result = await db_check_user(email)
    return {"is_valid": result}



#confirm
@Blog_v1.post("/item", status_code=HTTP_201_CREATED,response_model_include=["id", "owner"], tags=["Item"])
async def add_item(item: Item,jwt: bool = Depends(check_jwt_token)):
    await db_insert_item(item)
    return {"result": "item added successful"}

#confirm
@Blog_v1.get("/item", tags=["Item"])
async def get_all_item(jwt: bool = Depends(check_jwt_token)):
    item = await db_get_all_item()
    return item


#confirm
@Blog_v1.get("/{owner}/items",  tags=["Item"])
async def get_user_items(owner: str,jwt: bool = Depends(check_jwt_token)):
    items = await db_get_user_items(owner)
    return {"user items": items}



#confirm
@Blog_v1.get("/item/{id}", response_model=Item, tags=["Item"])
async def get_item_by_id(id: int,jwt: bool = Depends(check_jwt_token)):
     item = await db_get_item_with_id(id)
     return item

#confirm
@Blog_v1.patch("/item/{id}", tags=["Item"])
async def update_item(id: int,name: str, quantity: int, price: float, description: str,
    jwt: bool = Depends(check_jwt_token)):
    await db_update_item(id, name, quantity, price, description)
    return{"result": "item is updated"}



@Blog_v1.delete("/item/{id}", tags=["Item"])
async def delete_item(id: int,jwt: bool = Depends(check_jwt_token)):
    await db_delete_item_with_id(id)
    return {"item deleted"}




