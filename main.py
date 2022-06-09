from fastapi import FastAPI

from api import courses, sections, users
from db.db_setup import engine
from db.models import course, user

user.Base.metadata.create_all(bind=engine)
course.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Api-Fast",
    description="Estudos sobre FastApi e classes",
    version="0.0.1",
    contact={"name": "Rafael", "email": "neromad@outlook.com"},
    license_info={"name": "MIT"},
)

app.include_router(users.router)
app.include_router(courses.router)
app.include_router(sections.router)
