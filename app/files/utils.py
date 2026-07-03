from pathlib import Path
import uuid


def generate_stored_name(extension: str) -> str:

    extension = extension.lower().lstrip(".")

    return f"{uuid.uuid4()}.{extension}"


def user_directory(user_id: int) -> Path:

    from app.files.constants import USER_STORAGE

    return USER_STORAGE / str(user_id)
