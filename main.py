from fastapi import FastAPI
from core.config import settings
from api.v1.router import api_router

app = FastAPI(
    title=settings.app_name,
    version=settings.app_version,
    description="REST API for managing tasks"
)

@app.get("/")
def read_root():
    return {"app": settings.app_name, "version": settings.app_version}

app.include_router(api_router, prefix=settings.api_v1_prefix)
