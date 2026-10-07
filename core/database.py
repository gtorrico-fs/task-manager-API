from pymongo import MongoClient
from pymongo.collection import Collection

from core.config import settings

# tz_aware=True para que las fechas leídas de MongoDB incluyan zona horaria (UTC)
client = MongoClient(settings.mongodb_uri, tz_aware=True)
db = client[settings.mongodb_db]


def get_collection() -> Collection:
    """Devuelve la colección `tareas`."""
    return db[settings.mongodb_collection]