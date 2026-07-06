from abc import ABC, abstractmethod
from pathlib import Path


class StorageBackend(ABC):

    @abstractmethod
    def save(self, source: Path, destination: str) -> str:
        ...

    @abstractmethod
    def delete(self, path: str) -> None:
        ...

    @abstractmethod
    def exists(self, path: str) -> bool:
        ...

    @abstractmethod
    def open(self, path: str) -> Path:
        ...

    @abstractmethod
    def url(self, path: str) -> str:
        ...
