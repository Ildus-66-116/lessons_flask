import databases
import sqlalchemy
import uvicorn
from fastapi import FastAPI
from pydantic import Field, BaseModel

DATABASE_URL = "sqlite:///mydatabase_lek_6.db"
# DATABASE_URL = "postgresql://user:password@localhost/dbname"

database = databases.Database(DATABASE_URL)

metadata = sqlalchemy.MetaData()

users = sqlalchemy.Table(
    "users",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("name", sqlalchemy.String(32)),
    sqlalchemy.Column("email", sqlalchemy.String(128)),
)
engine = sqlalchemy.create_engine(
    DATABASE_URL, connect_args={"check_same_thread": False}
)  # только для Sqlite
metadata.create_all(engine)

app = FastAPI()


class UserIn(BaseModel):
    name: str = Field(max_length=32)
    email: str = Field(max_length=128)


class User(BaseModel):
    id: int
    name: str = Field(max_length=32)
    email: str = Field(max_length=128)


@app.get("/fake_users/{count}")
async def create_note(count: int):
    for i in range(1, count + 1):
        query = users.insert().values(name=f"user{i}", email=f"mail{i}@mail.ru")
        await database.execute(query)
    return {"message": f"{count} fake users create"}


if __name__ == "__main__":
    uvicorn.run("main_07:app", host="127.0.0.1", port=8000, reload=True)
