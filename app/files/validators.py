from pathlib import Path

from flask import current_app

class FileValidator:

    @staticmethod
    def validate_extension(filename: str):

        extension = Path(filename).suffix.lower().lstrip(".")

        if extension not in current_app.config["ALLOWED_EXTENSIONS"]:

            raise InvalidFileExtension(
                "File extension is not allowed."
            )

    @staticmethod
    def validate_size(file_size: int):

        if file_size > current_app.config["MAX_UPLOAD_SIZE"]:

            raise FileTooLarge(
                "File size exceeds maximum limit."
            )
