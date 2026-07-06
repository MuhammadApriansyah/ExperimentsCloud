from pathlib import Path
import shutil

from .backend import StorageBackend
from app.storage.key_builder import StorageKeyBuilder


class LocalStorage(StorageBackend):

    def __init__(self, root: Path):
        self.root = Path(root)

    def resolve(self, key: str | Path) -> Path:
        return self.root / Path(key)

    def key(
        self,
        user_id: int,
        stored_name: str,
    ) -> str:
        return StorageKeyBuilder.user_file(
            user_id,
            stored_name,
        )

    def file_path(
        self,
        user_id: int,
        stored_name: str,
    ) -> Path:
        return self.resolve(
            self.key(
                user_id,
                stored_name,
            )
        )

    def save(
        self,
        source,
        destination,
    ):

        target = self.resolve(destination)

        target.parent.mkdir(
            parents=True,
            exist_ok=True,
        )

        if hasattr(source, "save"):
            source.save(target)
        else:
            shutil.copy2(
                Path(source),
                target,
            )

        return target

    def exists(self, path):
        return self.resolve(path).exists()

    def delete(self, path):
        target = self.resolve(path)

        if target.exists():
            target.unlink()

    def open(self, path):
        return self.resolve(path).open("rb")
