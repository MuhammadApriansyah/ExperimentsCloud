from pathlib import Path


class StorageService:

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
