from pathlib import Path

from flask import current_app

from app.storage.key_builder import StorageKeyBuilder


class StorageService:

    @staticmethod
    def user_directory(user_id: int) -> Path:
        return (
            current_app.config["USER_STORAGE"]
            / str(user_id)
        )

    @staticmethod
    def object_key(
        user_id: int,
        stored_name: str,
    ) -> Path:
        return (
            current_app.config["USER_STORAGE"]
            / str(user_id)
            / stored_name
        )

    @staticmethod
    def ensure_directory(path: Path):
        path.mkdir(
            parents=True,
            exist_ok=True,
        )

    @staticmethod
    def save(uploaded_file, destination: Path):
        StorageService.ensure_directory(
            destination.parent
        )

        uploaded_file.save(destination)

    @staticmethod
    def exists(path: Path):
        return path.exists()

    @staticmethod
    def delete(path: Path):
        if path.exists():
            path.unlink()
