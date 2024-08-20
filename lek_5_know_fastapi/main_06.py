from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def read_root():
    return {"Hello": "World"}


@app.get("/users/{user_id}/orders/{order_id}")
async def read_item(user_id: int, order_id: int):
    # обработка данных
    return {"user_id": user_id, "order_id": order_id}


@app.get("/items/")
async def read_item(skip: int = 0, limit: int = 10):
    return {"skip": skip, "limit": limit}
