from fastapi import FastAPI
from app.routers import router1, router2, routerVersion
import json


app = FastAPI()

app.include_router(router1.router)
app.include_router(router2.router)
app.include_router(routerVersion.router)


@app.get("/")
def read_root():
    return "Deployment Version Manager"
