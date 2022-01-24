from pydantic import BaseModel, Field
from typing import Optional





class Item(BaseModel):
    name: str
    quantity: int
    price: float
    description: str
    owner:str


class ItemDelete(BaseModel):
    id: int = Field()
