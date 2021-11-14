from fastapi.security import HTTPBasic
from tus_app import app
from tus_app.Routers import cv, register, login

auth = HTTPBasic()

app.include_router(cv.router)
app.include_router(register.router)
app.include_router(login.router)
