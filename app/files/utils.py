import uuid


def generate_stored_name(extension: str) -> str:
    extension = extension.lower().lstrip(".")
    return f"{uuid.uuid4()}.{extension}"

