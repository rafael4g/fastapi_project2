from typing import List, Optional

from pydantic import BaseModel

from fastapi import FastAPI, Path, Query

from api import users, courses, sections

app = FastAPI(
    title="Api-Fast",
    description="Estudos sobre FastApi e classes",
    version="0.0.1",
    contact={"name": "Rafael D Silva", "email": "neromad@outlook.com"},
    license_info={"name": "MIT"},
)

app.include_router(users.router)
app.include_router(courses.router)
app.include_router(sections.router)