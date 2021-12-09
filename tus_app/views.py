from fastapi.security import HTTPBasic
from tus_app import app
from tus_app.Routers import cv, register, login,review, log

auth = HTTPBasic()

app.include_router(cv.router)
app.include_router(register.router)
app.include_router(login.router)
app.include_router(review.router)
app.include_router(log.router)