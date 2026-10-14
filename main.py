from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.openapi.docs import get_swagger_ui_html, get_redoc_html
from core.config import settings
from api.v1.router import api_router

app = FastAPI(
    title=settings.app_name,
    version=settings.app_version,
    description="REST API for managing tasks",
    docs_url=None,  # Disable default docs
    redoc_url=None  # Disable default redoc
)

@app.get("/")
def read_root():
    return {"app": settings.app_name, "version": settings.app_version}

@app.get("/docs", include_in_schema=False)
async def custom_swagger_ui_html():
    """Custom Swagger UI with Vercel Web Analytics"""
    html = get_swagger_ui_html(
        openapi_url=app.openapi_url,
        title=f"{app.title} - Swagger UI",
        swagger_js_url="https://cdn.jsdelivr.net/npm/swagger-ui-dist@5/swagger-ui-bundle.js",
        swagger_css_url="https://cdn.jsdelivr.net/npm/swagger-ui-dist@5/swagger-ui.css",
        swagger_favicon_url="https://fastapi.tiangolo.com/img/favicon.png",
        swagger_ui_parameters={"syntaxHighlight.theme": "obsidian"}
    )
    # Inject Vercel Analytics script before closing body tag
    return HTMLResponse(
        content=html.body.decode().replace(
            "</body>",
            '<script defer src="https://cdn.vercel-insights.com/v1/script.js"></script></body>'
        )
    )

@app.get("/redoc", include_in_schema=False)
async def custom_redoc_html():
    """Custom ReDoc with Vercel Web Analytics"""
    html = get_redoc_html(
        openapi_url=app.openapi_url,
        title=f"{app.title} - ReDoc",
        redoc_js_url="https://cdn.jsdelivr.net/npm/redoc@next/bundles/redoc.standalone.js",
        redoc_favicon_url="https://fastapi.tiangolo.com/img/favicon.png"
    )
    # Inject Vercel Analytics script
    return HTMLResponse(
        content=html.body.decode().replace(
            "</body>",
            '<script defer src="https://cdn.vercel-insights.com/v1/script.js"></script></body>'
        )
    )

app.include_router(api_router, prefix=settings.api_v1_prefix)
