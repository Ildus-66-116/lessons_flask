import databases
import sqlalchemy
import uvicorn
from fastapi import FastAPI

DATABASE_URL = "sqlite:///mydatabase_lek_6.db"
# DATABASE_URL = "postgresql://user:password@localhost/dbname"

database = databases.Database(DATABASE_URL)

metadata = sqlalchemy.MetaData()

...

engine = sqlalchemy.create_engine(DATABASE_URL)
metadata.create_all(engine)

app = FastAPI()


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


if __name__ == "__main__":
    uvicorn.run("main_05:app", host="127.0.0.1", port=8000, reload=True)
