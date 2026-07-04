from pathlib import Path
import uuid

from app.constants.storage import USER_STORAGE


def generate_stored_name(extension: str) -> str:
    extension = extension.lower().lstrip(".")
    return f"{uuid.uuid4()}.{extension}"

