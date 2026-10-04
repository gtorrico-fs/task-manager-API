import importlib
import pkgutil

from fastapi import APIRouter

from api.v1 import endpoints

api_router = APIRouter()

# Registro automático de cada funcionalidad (módulos de endpoints/ que definan `router`)
for _, nombre_modulo, _ in pkgutil.iter_modules(endpoints.__path__):
    modulo = importlib.import_module(f"{endpoints.__name__}.{nombre_modulo}")
    router = getattr(modulo, "router", None)
    if router is not None:
        api_router.include_router(router)