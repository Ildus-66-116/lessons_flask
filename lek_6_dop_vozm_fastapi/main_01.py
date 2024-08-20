from typing import List
import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    price: float
    is_offer: bool = None


class User(BaseModel):
    username: str
    full_name: str = None


class Order(BaseModel):
    items: List[Item]
    user: User


if __name__ == "__main__":
    uvicorn.run("main_01:app", host="127.0.0.1", port=8000, reload=True)
