from pathlib import Path

from app.constants.storage import (
    ALLOWED_EXTENSIONS,
    MAX_UPLOAD_SIZE,
)


class FileValidator:

    @staticmethod
    def validate_extension(filename: str):

        extension = Path(filename).suffix.lower().lstrip(".")

        if extension not in ALLOWED_EXTENSIONS:

            raise InvalidFileExtension(
                "File extension is not allowed."
            )

    @staticmethod
    def validate_size(file_size: int):

        if file_size > MAX_UPLOAD_SIZE:

            raise FileTooLarge(
                "File size exceeds maximum limit."
            )
