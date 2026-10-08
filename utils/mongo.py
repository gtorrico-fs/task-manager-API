

def serialize_task(doc: dict) -> dict:
    """Convierte un documento de MongoDB al formato de respuesta (`_id` -> `id`)."""
    doc = dict(doc)
    doc["id"] = str(doc.pop("_id"))
    return doc
