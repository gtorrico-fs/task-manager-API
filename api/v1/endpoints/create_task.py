from datetime import datetime, timezone

from fastapi import APIRouter, status

from core.database import get_collection
from schemas.tasks import CreateTask, TaskOut
from utils.mongo import serialize_task

router = APIRouter(prefix="/tareas", tags=["Tareas"])


@router.post("", response_model=TaskOut, status_code=status.HTTP_201_CREATED)
def crear_tarea(tarea: CreateTask):
    """Registra una nueva tarea."""
    documento = tarea.model_dump()
    documento["fecha_creacion"] = datetime.now(timezone.utc)

    coleccion = get_collection()
    resultado = coleccion.insert_one(documento)
    creada = coleccion.find_one({"_id": resultado.inserted_id})
    return serialize_task(creada)
