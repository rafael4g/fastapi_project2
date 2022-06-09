from typing import List, Optional

from pydantic import BaseModel

from fastapi import FastAPI, Path, Query

app = FastAPI(
    title="Api-Fast",
    description="Estudos sobre FastApi e classes",
    version="0.0.1",
    contact={"name": "Rafael D Silva", "email": "neromad@outlook.com"},
    license_info={"name": "MIT"},
)

users = []


class User(BaseModel):
    email: str
    is_active: bool
    bio: Optional[str]


@app.get("/users", response_model=List[User])
async def get_users():
    return users


@app.post("/users")
async def create_user(user: User):
    users.append(user)
    return "Success"


# Query(None, max_length=5) limit de caracteres
@app.get("/users/{id}")
async def get_user(
    id: int = Path(
        ..., description="The id of the user your want to retrieve.", gt=2
    ),
    q: str = Query(None, max_length=5),
):
    return {"user": users[id], "query": q}
