from enum import Enum
from pydantic import BaseModel, ConfigDict, Field
from typing import Optional
from datetime import datetime

class Prioridad(str, Enum):
    baja = "baja"
    media = "media"
    alta = "alta"

class Estado(str, Enum):
    pendiente = "pendiente"
    en_progreso = "en_progreso"
    completada = "completada"

class Proyecto(BaseModel):
    nombre: str = Field(..., min_length=1, examples=["Sistema de Inventario"])
    codigo: str = Field(..., min_length=1, examples=["INV-001"])

class CreateTask(BaseModel):
    # use_enum_values: se guardan strings simples ("alta") en MongoDB, no objetos Enum
    model_config = ConfigDict(use_enum_values=True)

    titulo: str = Field(..., min_length=1, max_length=150, examples=["Diseñar base de datos"])
    descripcion: str = Field("", examples=["Definir colecciones y relaciones"])
    prioridad: Prioridad = Prioridad.media
    estado: Estado = Estado.pendiente
    fecha_limite: Optional[datetime] = None
    responsable: str = Field(..., min_length=1, examples=["Ana Pérez"])
    etiquetas: list[str] = Field(default_factory=list, examples=[["backend", "mongodb"]])
    proyecto: Proyecto

class TaskOut(BaseModel):
    id: str
    titulo: str
    descripcion: str = ""
    prioridad: Prioridad
    estado: Estado
    fecha_creacion: datetime
    fecha_limite: Optional[datetime] = None
    responsable: str
    etiquetas: list[str] = []
    proyecto: Proyecto
