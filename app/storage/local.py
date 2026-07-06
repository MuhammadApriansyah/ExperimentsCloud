from pathlib import Path
import shutil

from .backend import StorageBackend


class LocalStorage(StorageBackend):

    def __init__(self, root: Path):
        self.root = Path(root)

    def _resolve(self, destination: str | Path) -> Path:
        return self.root / Path(destination)

    def save(self, source, destination: str | Path):

        target = self._resolve(destination)

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

    def exists(self, path: str | Path) -> bool:
        return self._resolve(path).exists()

    def delete(self, path: str | Path):
        target = self._resolve(path)

        if target.exists():
            target.unlink()

    def open(self, path: str | Path):
        return self._resolve(path).open("rb")

    def file_path(
        self,
        user_id: int,
        stored_name: str,
    ):
        return (
            Path(str(user_id))
            / stored_name
        )
