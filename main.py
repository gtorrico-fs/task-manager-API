from fastapi import FastAPI
from core.config import settings

app = FastAPI(
    title=settings.app_name,
    version=settings.app_version,
    description="REST API for managing tasks"
)

@app.get("/")
def read_root():
    return {"app": settings.app_name, "version": settings.app_version}
